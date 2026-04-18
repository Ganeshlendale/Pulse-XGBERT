from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "gundeveloper/pulse-xgbert-distilbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
