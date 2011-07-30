from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.finders import BaseStorageFinder
from django.conf import settings


class StaticRootFinder(BaseStorageFinder):
    storage = FileSystemStorage(settings.PROJECT_STATIC_ROOT, settings.STATIC_URL)