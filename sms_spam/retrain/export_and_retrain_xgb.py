"""
retrain/export_and_retrain_xgb.py
----------------------------------
Run whenever you want to retrain XGBoost on accumulated feedback.

Usage (from project root):
    python retrain/export_and_retrain_xgb.py
"""

import os, sys, django, joblib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spam_classifier.settings")
django.setup()

from model_app.models import FeedbackEntry

MODELS_DIR = os.path.join(BASE, "ml_models")


def main():
    from xgboost import XGBClassifier

    vectorizer = joblib.load(os.path.join(MODELS_DIR, "vectorizer.pkl"))
    encoder    = joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))
    old_model  = joblib.load(os.path.join(MODELS_DIR, "xgboost_model.pkl"))

    entries = FeedbackEntry.objects.select_related("prediction").filter(is_exported=False)
    if not entries.exists():
        print("No new feedback. Exiting.")
        return

    texts  = [e.prediction.input_text for e in entries]
    labels = [e.correct_label for e in entries]
    print(f"Training on {len(texts)} new feedback entries …")

    X = vectorizer.transform(texts).toarray()
    y = encoder.transform(labels)

    new_model = XGBClassifier(
        n_estimators=old_model.n_estimators + 50,
        max_depth=old_model.max_depth,
        learning_rate=old_model.learning_rate,
        eval_metric="mlogloss",
    )
    new_model.fit(X, y)

    out = os.path.join(MODELS_DIR, "xgboost_model.pkl")
    joblib.dump(new_model, out)
    print(f"✅ Model saved → {out}")
    entries.update(is_exported=True)
    print("Feedback rows marked exported.")


if __name__ == "__main__":
    main()
