from admin_tools.dashboard.modules import ModelList
from admin_tools.utils import get_admin_site_name
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard

class IndexDashboard(Dashboard):
    # we want a 2 columns layout
    columns = 2

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administration'),
            models=('django.contrib.*','social_auth.*'),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Sigurd project website'),
                    'url': 'http://sigurd.webriders.com.ua',
                    'external': True,
                },
                {
                    'title': _('Django Dash 2011'),
                    'url': 'http://djangodash.com',
                    'external': True,
                },
            ]
        ))


