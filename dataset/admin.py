from django.contrib import admin

from .models import Dataset, Disease, Modality

admin.site.register(Dataset)
admin.site.register(Disease)
admin.site.register(Modality)
