import os

from django.conf import settings
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .decorators import user_is_superuser
from .forms import DatasetCreateForm, DatasetUpdateForm
from .models import Dataset


@user_is_superuser
def new_dataset(request):
    if request.method == "POST":
        form = DatasetCreateForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            # form.save()
            return redirect("datasetlist")

    else:
        form = DatasetCreateForm()

    return render(
        request=request,
        template_name='dataset/new_dataset.html',
        context={
            "object": "Dataset",
            "form": form
        }
    )


class DatasetListView(generic.ListView):
    model = Dataset
    context_object_name = 'dataset_list'
    template_name = 'dataset/dataset.html'


def download_file(request, file_id):
    # Retrieve the file from the list using the file_id
    file = get_object_or_404(Dataset, id=file_id)

    # Construct the file path based on the file's relative path and the MEDIA_ROOT setting
    file_path = os.path.join(settings.MEDIA_ROOT, file.zipfile.name)

    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Create an HTTP response containing the file contents
    response = HttpResponse(
        file_contents, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file.zipfile.name

    return response
