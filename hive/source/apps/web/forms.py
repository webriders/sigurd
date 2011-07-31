from django import forms
from web.models import ApplicationConfig

class ApplicationConfigForm(forms.ModelForm):
    class Meta:
        model = ApplicationConfig
        fields = ('application', 'title', 'description', 'slug', 'supported_versions',
                  'file_name', 'author_name', 'author_email', )

    def get_archive_ext(self):
        archive = self.cleaned_data['file_name']
        extensions = ('.tar.gz', '.tgz')

        for ext in extensions:
            if archive.name.endswith(ext):
                return ext
        return None

    def clean_file_name(self):
        correct_ext  = self.get_archive_ext()
        if not correct_ext:
            raise forms.ValidationError("Archive must be in one of such formats: " + ', '.join(extensions))

        return self.cleaned_data['file_name']

    def save(self, commit=True):
        app_slug = self.cleaned_data['application'].slug
        config_slug =  self.cleaned_data['slug']
        extension = self.get_archive_ext()[1:]

        name = "(%(app_slug)s)__%(config_slug)s.%(extension)s"\
             % dict( app_slug=app_slug, config_slug=config_slug, extension=extension)
        self.instance.file_name.name = name

        return super(ApplicationConfigForm, self).save(commit)
