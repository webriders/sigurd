# -*- coding: UTF-8 -*-

from django.db import models
from datetime import datetime, date

class Application(models.Model):
    slug = models.SlugField(max_length=64, verbose_name=u'Slug')
    url = models.URLField(max_length=256, blank=True, null=True, verbose_name=u'URL')
    published = models.BooleanField(blank=True, verbose_name='Visible on apps page')

    def __unicode__(self):
        return self.slug


class ApplicationConfig(models.Model):
    published = models.BooleanField(blank=True, verbose_name='Visible on configs page')
    application = models.ForeignKey(Application, verbose_name=u'Application')
    title = models.CharField(max_length=256, verbose_name=u'Config name')
    description = models.TextField(max_length=3096, blank=True, null=True, verbose_name=u'Ddescription')
    slug = models.SlugField(max_length=64, verbose_name=u'Slug')
    author_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Author name')
    author_email = models.EmailField(max_length=128, blank=True, null=True, verbose_name=u'Author e-mail')
    supported_versions = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Supported versions')
    file_name = models.FileField(upload_to='.', verbose_name=u'Archive with configuration')
    views = models.IntegerField(default=0, verbose_name=u"Views count")
    downloads = models.IntegerField(default=0, verbose_name=u"Downloads count")
    is_master = models.BooleanField(blank=True, verbose_name=u'Is master (default)')

    def __unicode__(self):
        return self.title or self.slug
