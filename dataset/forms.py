from django import forms

from .models import Dataset


class DatasetCreateForm(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "disease",
            "modality",
            "description",
            "reference",
            "measurable_index",
            "zipfile",
        ]


class DatasetUpdateForm(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "disease",
            "modality",
            "description",
            "reference",
            "measurable_index",
            "zipfile",
        ]


class DatasetFull(forms.ModelForm):
    class Meta:
        model = Dataset

        fields = [
            "title",
            "disease",
            "modality",
            "description",
            "reference",
            "measurable_index",
            "zipfile",
        ]
