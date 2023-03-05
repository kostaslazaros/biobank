from django.urls import path

from . import views

urlpatterns = [

    path("new_dataset/", views.new_dataset, name="dataset-create"),
    path("datasetlist/", views.DatasetListView.as_view(), name="datasetlist"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
