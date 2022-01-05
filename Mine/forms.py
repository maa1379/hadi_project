from django import forms

from .models import Madan


class MadanForm(forms.ModelForm):
    class Meta:
        model = Madan
        fields = (
            "name",
            "location",
            "description",
            "stone_type",
            "country",
            "state",
            "province",
            "city",
        )
        labels = {
            "name": "نام معدن",
            "location": "لوکیشن",
            "description": "توضیحات",
            "stone_type": "نوع سنگ",
            "country": "کشور",
            "state": "منطقه",
            "province": "استان",
            "city": "شهذ",
        }
