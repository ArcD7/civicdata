from pickle import TRUE
from re import T
from django.db import models

# Create your models here.
class ResourceIndex(models.Model):
    resource_id = models.AutoField(primary_key=True)
    # metadata_id = models.IntegerField(null=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    tags = models.CharField(max_length=128, null=True, blank=True)
    file_name = models.FileField(upload_to ='csv')
    metadata_file = models.FileField(upload_to ='metadata', default=None, blank=True)
    
    class Meta:
        db_table = 'Index'

class Grants(models.Model):
    budgetFor = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    fiscalYear = models.CharField(max_length=128)
    indicators = models.CharField(max_length=128)
    budgetType = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    resource_id = models.ForeignKey(ResourceIndex, on_delete=models.CASCADE, db_column='resource_id')
    
    class Meta:
        db_table = 'Grants'

class Metadata(models.Model):
    heading = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    resource_id = models.ForeignKey(ResourceIndex, on_delete=models.CASCADE, db_column='resource_id')
    
    class Meta:
        db_table = 'Metadata'
