from admin_tools.dashboard.modules import ModelList
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard

class IndexDashboard(Dashboard):
    # we want a 2 columns layout
    columns = 2

    def init_with_context(self, context):
        # append an app list module for "Administration"
        self.children.append(ModelList(
            title = _('Administration'),
            deletable=False,
            draggable=True,
            collapsible=True,
            include_list=('django.contrib',)
        ))

