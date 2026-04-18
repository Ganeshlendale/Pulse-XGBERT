"""
ml_engine.py
------------
Singleton loader for both ML models.
Import `xgb_predict` or `distilbert_predict` in your views.
"""

import os
import logging
import joblib
import numpy as np

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "ml_models")

# ---------------------------------------------------------------------------
# XGBoost + TF-IDF pipeline (lazy singleton)
# ---------------------------------------------------------------------------
_xgb_model = None
_vectorizer = None
_encoder = None


def _load_xgb():
    global _xgb_model, _vectorizer, _encoder
    if _xgb_model is None:
        logger.info("Loading XGBoost artefacts …")
        _xgb_model = joblib.load(os.path.join(MODELS_DIR, "xgboost_model.pkl"))
        _vectorizer = joblib.load(os.path.join(MODELS_DIR, "vectorizer.pkl"))
        _encoder = joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))
        logger.info("XGBoost artefacts loaded.")


def xgb_predict(text: str) -> dict:
    """
    Returns {"label": str, "confidence": float, "all_probs": dict}
    """
    _load_xgb()
    vec = _vectorizer.transform([text]).toarray()
    pred_idx = _xgb_model.predict(vec)
    label = _encoder.inverse_transform(pred_idx)[0]

    confidence = None
    all_probs = {}
    if hasattr(_xgb_model, "predict_proba"):
        proba = _xgb_model.predict_proba(vec)[0]
        classes = _encoder.classes_
        all_probs = {cls: round(float(p), 4) for cls, p in zip(classes, proba)}
        confidence = round(float(proba[pred_idx[0]]), 4)

    return {"label": label, "confidence": confidence, "all_probs": all_probs}


# ---------------------------------------------------------------------------
# DistilBERT (lazy singleton — only loaded when requested)
# ---------------------------------------------------------------------------
_db_model = None
_db_tokenizer = None
_db_id2label = None


def _load_distilbert():
    global _db_model, _db_tokenizer, _db_id2label
    if _db_model is None:
        try:
            import torch
            from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

            MODEL_NAME = "Ganeshlendale/pulse-xgbert-distilbert"
            logger.info(f"Loading DistilBERT artefacts from Hugging Face ({MODEL_NAME}) …")
            _db_tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_NAME)
            _db_model = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)
            _db_model.eval()

            _db_id2label = _db_model.config.id2label if hasattr(_db_model.config, 'id2label') else {}
            logger.info("DistilBERT artefacts loaded from Hugging Face.")
        except ImportError as e:
            raise RuntimeError(
                "transformers / torch not installed. "
                "Run: pip install transformers torch safetensors"
            ) from e


def distilbert_predict(text: str) -> dict:
    """
    Returns {"label": str, "confidence": float, "all_probs": dict}
    """
    import torch

    _load_distilbert()
    inputs = _db_tokenizer(
        text, return_tensors="pt", truncation=True, max_length=512, padding=True
    )
    with torch.no_grad():
        logits = _db_model(**inputs).logits
    proba = torch.softmax(logits, dim=-1)[0].tolist()
    pred_idx = int(torch.argmax(logits, dim=-1).item())

    raw_label = _db_id2label.get(str(pred_idx), f"LABEL_{pred_idx}")
    # If label_encoder is available, convert LABEL_N → human name
    _load_xgb()
    try:
        label = _encoder.classes_[pred_idx]
    except IndexError:
        label = raw_label

    all_probs = {}
    for i, p in enumerate(proba):
        try:
            cls = _encoder.classes_[i]
        except IndexError:
            cls = _db_id2label.get(str(i), f"LABEL_{i}")
        all_probs[cls] = round(p, 4)

    return {"label": label, "confidence": round(proba[pred_idx], 4), "all_probs": all_probs}
