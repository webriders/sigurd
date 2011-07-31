from django.core.urlresolvers import reverse
from admin_tools.menu import items, Menu

class CustomMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children.append(items.MenuItem(
            title=u'Main',
            url=reverse('admin:index')
        ))
        self.children.append(items.MenuItem(
            title=u'Web-Site',
            url='/'
        ))
        self.children.append(items.Bookmarks(title=u'Bookmarks'))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass