from django.views.generic import TemplateView, ListView, DetailView
from web.models import Application
from web.forms import ApplicationConfigForm


class HomeView(TemplateView):
    template_name = 'pages/home.html'

home = HomeView.as_view()


class ApplicationsList(ListView):
    template_name = 'pages/applications_list.html'
    context_object_name = 'applications_list'
    queryset = Application.objects.filter(published=True)

applications_list = ApplicationsList.as_view()


class AppConfigDetail(DetailView):
    template_name = 'pages/app_config_detail.html'

    def get_object(self, queryset=None):
        return None
    
    def get_context_data(self, **kwargs):
        context = super(AppConfigDetail, self).get_context_data(**kwargs)

        context['app_config_form'] = ApplicationConfigForm()

        return context

add_app_config = AppConfigDetail.as_view()