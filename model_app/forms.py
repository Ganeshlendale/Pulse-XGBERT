from django import forms

MODEL_CHOICES = [
    ("xgboost", "XGBoost (fast, TF-IDF)"),
    ("distilbert", "DistilBERT (deep learning)"),
]

LABEL_CHOICES = [
    ("financial", "Financial"),
    ("fraud", "Fraud"),
    ("lottery", "Lottery"),
    ("not_spam", "Not Spam"),
    ("otp", "OTP"),
    ("promotion", "Promotion"),
]


class PredictForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Paste your message here …"}),
        label="Input Text",
    )
    model_choice = forms.ChoiceField(choices=MODEL_CHOICES, label="Model")


class FeedbackForm(forms.Form):
    correct_label = forms.ChoiceField(choices=LABEL_CHOICES, label="Correct Label")
    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Any extra notes? (optional)"}),
        required=False,
        label="Notes",
    )
