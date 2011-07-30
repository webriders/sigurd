from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard
from admin_tools.utils import get_admin_site_name


class IndexDashboard(Dashboard):
    # we want a 2 columns layout
    columns = 2

    def init_with_context(self, context):
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
            ]
        ))