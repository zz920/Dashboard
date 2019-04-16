JET_INDEX_DASHBOARD = 'main_dashboard.index.CustomerIndexDashboard'

# JET_DEFAULT_THEME = 'light-blue'

JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [
    {'label': 'USER MANAGEMENT', 'items':[
        {'label': 'USER ACCOUNTS MANAGEMENT', 'url': '/user/user', 'permissions': ['user.user']},
        {'label': 'GROUP PERMISSION MANAGEMENT', 'url': '/auth/group', 'permissions': ['auth.group']},
    ]},
    {'label': 'ITEM MANAGEMENT', 'items': [
        {'label': 'COMMON ITEM VIEW', 'url': '/souq/item'},
        {'label': 'HOT ITEMS BY CATEGORY', 'url': '/souq/category'},
        {'label': 'HOT ITEMS BY SELLER', 'url': '/souq/seller'},
    ]},
]
