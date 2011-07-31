from django import forms
from web.models import ApplicationConfig


class ApplicationConfigForm(forms.ModelForm):
    class Meta:
        model = ApplicationConfig
        fields = ('application', 'title', 'description', 'slug', 'supported_versions',
                  'archive', 'author_name', 'author_email',)

    VALID_ARCHIVE_EXTENSIONS = ('.tar.gz', '.tgz',)

    def get_archive_extension(self, archive):
        for ext in self.VALID_ARCHIVE_EXTENSIONS:
            if archive.name.endswith(ext):
                return ext
        return None

    def clean_archive(self):
        archive = self.cleaned_data['archive']
        if not self.get_archive_extension(archive):
            raise forms.ValidationError("Supported archive formats: " + ', '.join(self.VALID_ARCHIVE_EXTENSIONS))
        return archive

    def save(self, commit=True):
        app_slug = self.cleaned_data['application'].slug
        config_slug = self.cleaned_data['slug']
        archive = self.cleaned_data['archive']
        extension = self.get_archive_extension(archive)[1:]

        name = "%(app_slug)s__%(config_slug)s.%(extension)s"\
             % dict(app_slug=app_slug, config_slug=config_slug, extension=extension)
        self.instance.archive.name = name

        return super(ApplicationConfigForm, self).save(commit)
