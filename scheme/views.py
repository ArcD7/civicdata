from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CsvModelForm
from .models import ResourceIndex, FileManagement

import zipfile
import os

# View that will display all the datasets.
def index(request):
    
    all_datasets =[]
    get_all_data = ResourceIndex.objects.all()
    for files in get_all_data:
        name = files.name
        all_datasets.append(name)
    return render(request, "scheme/index.html", {"datasets": all_datasets})

# View that will let users upload their datasets.
def upload_file_view(request):
    # Form submission should only be a POST request.
    if request.method == 'POST':
        form = CsvModelForm(request.POST, request.FILES)
        if form.is_valid():
            # Get data from the form
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            tags = form.cleaned_data['tags']
            metadata_file = form.cleaned_data['metadata_file']
            
            # Add string data to the database.
            files = request.FILES.getlist('file_name')
            file_instance = ResourceIndex.objects.create(
                    file_name=name,
                    metadata_file=metadata_file,
                    name=name,
                    description=description,
                    tags=tags
                )
            #print(file_instance, file_instance.resource_id)
            
            # Add all uploaded files to the database.
            for f in files:
                FileManagement.objects.create(
                    file_name=f, 
                    resource_id=file_instance
                )
            # Reset the form after submission.
            form = CsvModelForm()
            messages.success(request, "Data Added Successfully")
            
            # return render(
            # request, 
            # 'scheme/upload.html',
            # {'form': form})
            return redirect(index)
    else:
        form = CsvModelForm()
    
    return render(
    request, 
    'scheme/upload.html',
    {'form': form})

# Homepage for each dataset that will show it's details.
def dataset_home(request, name):
    file_id = ResourceIndex.objects.get(name=name)
    files = FileManagement.objects.filter(resource_id=file_id.resource_id)
    if file_id.metadata_file:
        metafile = True
    else:
        metafile = False
    return render(request, 
                'scheme/dataset.html', 
                {
                    'name':file_id.name,
                    'description':file_id.description,
                    'tags':file_id.tags,
                    'uploaded_at':file_id.uploaded_at,
                    "num_files":files,
                    "metadata":metafile,
                }
            )

# Download resource files for a dataset.
def dataset_download(request, name):
    # Get the required data from the dataset.
    file_id = ResourceIndex.objects.get(name=name)
    files = FileManagement.objects.filter(resource_id=file_id.resource_id) 
    
    # Create a Zip file.
    zip_file = f"media/csv/{file_id.name}.zip"
    
    # Open the Zip file and append csv's.
    with zipfile.ZipFile(zip_file, "w") as archive:
        for f in files:
            filename = f.file_name.name.split("/")
            filepath = f.file_name.path
            archive.write(filepath, arcname=filename[1])
        # If metadata.csv exists append it to the zip file.
        if file_id.metadata_file:
            metadata_path = file_id.metadata_file.path
            archive.write(metadata_path, arcname="metadata.csv")
    
    zf = open(zip_file, 'rb')
    response = HttpResponse(zf, content_type="application/zip")
    response['Content-Disposition'] = f"attachment; filename={name}.zip"
    return response

# Delete dataset and its files.
def dataset_delete(request, name):
    # Get the required data from the dataset.
    file_id = ResourceIndex.objects.get(name=name)
    files = FileManagement.objects.filter(resource_id=file_id.resource_id)
    
    # Delete resource files.
    if files.exists():
        for f in files:
            filepath = f.file_name.path
            os.remove(filepath)
    # Delete metadata file.
    if file_id.metadata_file:
        metadata_path = file_id.metadata_file.path
        os.remove(metadata_path)

    # Delete file instance.
    file_id.delete()
    messages.success(request, "Dataset Deleted Successfully")
    return redirect(index)