from django import forms

from .models import Dataset


class DatasetCreateForm(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "description",
            "zipfile",
        ]


class DatasetUpdateForm(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "description",
            "zipfile",
        ]


class DatasetFull(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "description",
            "zipfile",
        ]
