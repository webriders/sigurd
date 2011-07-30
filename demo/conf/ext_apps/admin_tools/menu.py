from django.core.urlresolvers import reverse
from admin_tools.menu import items, Menu


class Menu(Menu):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.children += [
            items.MenuItem('Admin Home', reverse('admin:index')),
            items.MenuItem('Web-Site', '/'),
        ]