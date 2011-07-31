from os import path
from django.views.generic import TemplateView, ListView, CreateView, RedirectView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from web.models import Application, ApplicationConfig
from web.forms import ApplicationConfigForm


class HomeView(TemplateView):
    template_name = 'pages/home/home.html'

home = HomeView.as_view()


class ApplicationsList(ListView):
    template_name = 'pages/applications_list.html'
    context_object_name = 'applications_list'
    queryset = Application.objects.filter(published=True)

applications_list = ApplicationsList.as_view()


class AddAppConfig(CreateView):
    template_name = 'pages/add_app_config.html'
    form_class = ApplicationConfigForm

    def get_success_url(self):
        return reverse('add_app_config_success')

add_app_config = AddAppConfig.as_view()


class AddAppConfigSuccess(TemplateView):
    template_name = 'pages/add_app_config_success.html'

add_app_config_success = AddAppConfigSuccess.as_view()


class ConfigDownloader(RedirectView):
    permanent = False

    def get_redirect_url(self, config_id, **kwargs):
        config = get_object_or_404(ApplicationConfig, id=config_id)

        if not config.archive:
            raise Http404

        config.downloads += 1
        config.save()
        return config.archive.url

config_downloader = ConfigDownloader.as_view()
