from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import CsvModelForm
from .models import ResourceIndex, Grants, Metadata
import csv
import time

# Create your views here.
def upload_file_view(request):
    #return HttpResponse('Upload File')
    #if request.method == 'POST':
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # file is saved
        form.save()
        form = CsvModelForm()
        print(request.FILES)
        name = "csv/" + request.FILES['file_name'].name
        print(name)
        file_obj = ResourceIndex.objects.filter(file_name=name)
        print(file_obj)
        with open(settings.MEDIA_ROOT+ "/" + name) as csv_file:
            data = csv.reader(csv_file)
            next(data)
            for row in data:
                Grants.objects.create(
                budgetFor=row[0],
                type=row[1],
                fiscalYear=row[2],
                indicators=row[3],
                budgetType=row[4],
                value=row[5],
                resource_id=file_obj[0]
                )
        if request.FILES['metadata_file']:
            meta_name = "metadata/" + request.FILES['metadata_file'].name
            with open(settings.MEDIA_ROOT+ "/" + meta_name) as csv_file:
                data = csv.reader(csv_file)
                #next(data)
                for row in data:
                    Metadata.objects.create(
                    heading=row[0],
                    description=row[1],
                    resource_id=file_obj[0]
                    )
                    
        messages.success(request, "Data Added Successfully")
    return render(
        request, 
        'scheme/upload.html',
        {'form': form})