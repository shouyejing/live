#coding=utf-8
{
    'name': 'qd living',
    'description': '直播',
    'author': 'mrc',
    'depends': ['base'],
    'application': True,
    'sequence':"0",
    'data': [
        'security/ir.model.access.csv',
        # 'security/user_access_rules.xml',
        'views/living_menu.xml',
        'views/living_user.xml',
        'views/living_living.xml',
        'views/living_cls.xml',
        'views/living_circle.xml',
        'views/living_index.xml',
    ],
    'demo': [
            'demo/demo_living_type.xml',
            'demo/demo_living_room.xml',
        ]
 }
