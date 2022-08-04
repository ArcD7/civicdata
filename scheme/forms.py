from django import forms
from .models import Grants, ResourceIndex

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = ResourceIndex
        fields = ('file_name', 'metadata_file', 'name', 'description', 'tags')
        widgets = {
            'file_name': forms.ClearableFileInput(
                attrs={
                    'multiple': True
                    }
                )
            }