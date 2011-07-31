from os import path
from django.views.generic import TemplateView, ListView, CreateView, RedirectView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404
from web.models import Application, ApplicationConfig, DownloadsItem
from web.forms import ApplicationConfigForm


class HomeView(TemplateView):
    template_name = 'pages/home/home.html'

home = HomeView.as_view()


class ConfigsList(ListView):
    template_name = 'pages/configs_list.html'
    context_object_name = 'applications_list' # we will group configs by applications
    model = Application

    def get_queryset(self):
        return self.model.objects.filter(published=True)

configs_list = ConfigsList.as_view()


class AddConfig(CreateView):
    template_name = 'pages/add_config.html'
    form_class = ApplicationConfigForm

    def get_success_url(self):
        return reverse('add_config_success')

add_config = AddConfig.as_view()


class AddConfigSuccess(TemplateView):
    template_name = 'pages/add_config_success.html'

add_config_success = AddConfigSuccess.as_view()


class ConfigDownloader(RedirectView):
    permanent = False

    def get_redirect_url(self, app_slug, config_slug=None, **kwargs):
        if config_slug:
            config = get_object_or_404(ApplicationConfig, application__slug=app_slug, slug=config_slug)
        else:
            configs = ApplicationConfig.objects.filter(application__slug=app_slug)

            if not configs:
                raise Http404('Configs not found!')

            try:
                config = configs.get(is_master=True)
            except ApplicationConfig.MultipleObjectsReturned:
                config = configs.filter(is_master=True)[0]
            except ApplicationConfig.DoesNotExist:
                config = configs[0]
            
        config.downloads += 1
        config.save()

        return config.archive.url

download_config = ConfigDownloader.as_view()


class DownloadsView(ListView):
    template_name = 'pages/downloads_list.html'
    model = DownloadsItem
    context_object_name = 'downloads'

downloads = DownloadsView.as_view()