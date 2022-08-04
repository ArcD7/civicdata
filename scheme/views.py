from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import CsvModelForm
from .models import ResourceIndex, Grants, Metadata, FileManagement


def index(request):
    
    all_datasets =[]
    get_all_data = ResourceIndex.objects.all()
    for files in get_all_data:
        name = files.name
        all_datasets.append(name)
    return render(request, "scheme/index.html", {"datasets": all_datasets})


def upload_file_view(request):
    #if request.method == 'POST':
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        tags = form.cleaned_data['tags']
        metadata_file = form.cleaned_data['metadata_file']
        
        # Lets get the dataset files that were uploaded
        files = request.FILES.getlist('file_name')
        file_instance = ResourceIndex.objects.create(
                file_name=name,
                metadata_file=metadata_file,
                name=name,
                description=description,
                tags=tags
            )
        print(file_instance, file_instance.resource_id)
        
        for f in files:
            FileManagement.objects.create(
                file_name=f, 
                resource_id=file_instance
            )
        form = CsvModelForm()
        messages.success(request, "Data Added Successfully")
    return render(
        request, 
        'scheme/upload.html',
        {'form': form})