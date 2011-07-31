from datetime import datetime
from django.db import models


class Application(models.Model):
    slug = models.SlugField(max_length=64, unique=True, verbose_name=u'Slug')
    url = models.URLField(max_length=256, blank=True, null=True, verbose_name=u'URL')
    published = models.BooleanField(blank=True, verbose_name='Visible on apps page')

    def get_configs(self):
        return ApplicationConfig.objects.filter(application=self, published=True)

    def __unicode__(self):
        return self.slug


class ApplicationConfig(models.Model):
    published = models.BooleanField(blank=True, verbose_name="Visible on configs page")
    publish_date = models.DateTimeField(default=datetime.now())
    application = models.ForeignKey(Application)
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=3096, blank=True, null=True)
    slug = models.SlugField(max_length=64, help_text="Config unique ID")
    author_name = models.CharField(max_length=128, blank=True, null=True)
    author_email = models.EmailField(max_length=128, blank=True, null=True, verbose_name="Author e-mail", help_text="We will not publish it")
    supported_versions = models.CharField(max_length=128, blank=True, null=True, help_text="Supported application versions, e.g.: \"1.3.1-2.5\", or \"newer than 1.6.3\"")
    archive = models.FileField(upload_to='.', verbose_name=u'Archive with config', help_text="Only .tar.gz and .tgz is supported for now")
    downloads = models.IntegerField(default=0, verbose_name=u"Downloads count")
    is_master = models.BooleanField(blank=True, verbose_name=u'Is master (default)')

    class Meta:
        unique_together = ("application", "slug")
    
    def __unicode__(self):
        return self.title or self.slug


class DownloadItem(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    archive = models.FileField(upload_to='downloads/')

    def get_archive_name(self):
        import os.path
        return os.path.basename(self.archive.name)

    def __unicode__(self):
        return self.title or self.archive.url

    class Meta:
        verbose_name = u'Downloads'
        verbose_name_plural = verbose_name
