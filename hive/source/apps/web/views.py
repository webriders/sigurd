from django.views.generic import TemplateView, ListView
from web.models import Application


class HomeView(TemplateView):
    template_name = 'pages/home.html'

home = HomeView.as_view()


class ApplicationsList(ListView):
    template_name = 'pages/applications_list.html'
    context_object_name = 'applications_list'
    model = Application

    def get_context_data(self, **kwargs):
        context = super(ApplicationsList, self).get_context_data(**kwargs)


        return context

applications_list = ApplicationsList.as_view()