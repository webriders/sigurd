from django import forms
from web.models import ApplicationConfig

class ApplicationConfigForm(forms.ModelForm):
    class Meta:
        model = ApplicationConfig
        fields = ('application', 'title', 'description', 'slug', 'supported_versions',
                  'file_name', 'author_name', 'author_email', )
