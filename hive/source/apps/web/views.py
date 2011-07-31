from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse
from web.models import Application
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
