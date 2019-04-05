JET_INDEX_DASHBOARD = 'main_dashboard.index.CustomIndexDashboard'

JET_DEFAULT_THEME = 'light-blue'

JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [
    {'label': 'User Managment', 'app_label': 'user', 'items': [
    	{'name': 'user.user', 'label': 'User Info'},
    ]},
    {'label': 'Permission Managment', 'app_label': 'auth', 'items': [
        {'name': 'auth.group', 'label': 'Group Info'},
    ]},
    {'label': 'Item View', 'app_label': 'main_dashboard', 'items': [
        {'label': 'Item view', 'url': '/souq/item'},
    ]}
]
