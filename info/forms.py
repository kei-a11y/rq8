# kk10/forms.py
from django import forms
from .models import AutomationRequest

class AutomationRequestForm(forms.ModelForm):
    class Meta:
        model = AutomationRequest
        fields = ["system_name", "industry", "other_industry", "manual_file", "contact_info", "other"]
        labels = {
            "manual_file": "もし可能であればそのシステムのマニュアル情報等を添付してください",
        }
        widgets = {
            "system_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "manual_file": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "industry": forms.Select(attrs={"class": "form-control", "required": True}),
            "other_industry": forms.TextInput(attrs={"class": "form-control", "placeholder": "その他の業態を入力してください"}),

            "contact_info": forms.TextInput(attrs={"class": "form-control"}),
            "other": forms.Textarea(attrs={"class": "form-control", "placeholder": "任意入力", "rows":4}),
        }

