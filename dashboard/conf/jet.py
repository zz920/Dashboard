from django.utils.translation import ugettext_lazy as _

JET_INDEX_DASHBOARD = 'main_dashboard.index.CustomerIndexDashboard'

# JET_DEFAULT_THEME = 'light-blue'

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = False

JET_SIDE_MENU_ITEMS = [
    {'label': _('USER MANAGEMENT'), 'items':[
        {'label': _('USER ACCOUNTS MANAGEMENT'), 'url': '/user/user', 'permissions': ['user.user']},
        {'label': _('GROUP PERMISSION MANAGEMENT'), 'url': '/auth/group', 'permissions': ['auth.group']},
    ]},
    {'label': _('ITEM MANAGEMENT'), 'items': [
        {'label': _('COMMON ITEM VIEW'), 'url': '/souq/item'},
        {'label': _('HOT ITEMS BY CATEGORY'), 'url': '/souq/category'},
        {'label': _('HOT ITEMS BY SELLER'), 'url': '/souq/seller'},
        {'label': _('SINGLE ITEMS ANALYSIS'), 'url': '/souq/singleitem'}
    ]},
]
