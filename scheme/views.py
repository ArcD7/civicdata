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
    if request.method == 'POST':
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
        else:
            #form = "This name already exists"
            form.add_error('name', 'This name already exists')
            # print(form.errors)
            # return render(
            #     request, 
            #     'scheme/upload.html',
            #     )
    else:
        form = CsvModelForm()
    
    return render(
    request, 
    'scheme/upload.html',
    {'form': form})

def dataset_home(request, name):
    file_id = ResourceIndex.objects.get(name=name)
    print(file_id)
    return render(request, 
                'scheme/dataset.html', 
                {
                    'name':file_id.name,
                    'description':file_id.description,
                    'tags':file_id.tags,
                    'uploaded_at':file_id.uploaded_at
                }
            )

def dataset_download(request, name):
    print(name)
    file_id = ResourceIndex.objects.filter(name=name)
    print("File_ID", file_id[0].resource_id)
    files = FileManagement.objects.filter(resource_id=file_id[0].resource_id) 
    print(files[0].file_name.name, files[0].file_name.path)
    filename = files[0].file_name.name.split("/")
    print(filename)
    filepath = files[0].file_name.path
    print(filepath)
    import mimetypes
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='text/csv')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = f"attachment; filename={filename[1]}"
    # Return the response value
    return response