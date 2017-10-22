#coding=utf-8
{
    'name': 'qd live',
    'description': '清大直播',
    'author': 'mrc',
    'depends': ['base'],
    'application': True,
    'sequence':"0",
    'data': [
        'security/ir.model.access.csv',
        # 'security/user_access_rules.xml',
        'views/live_menu.xml',
        'views/live_user.xml',
        'views/live.live.xml',
        'views/live_cls.xml',
        'views/live_circle.xml',
        'views/live_index.xml',
        'templates/template.xml',
    ],
    # 'demo': [
    #         'demo/demo_live_type.xml',
    #         'demo/demo_live_room.xml',
    #     ]
 }
