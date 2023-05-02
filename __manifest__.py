# -*- coding: utf-8 -*-
{
    'name': "Materials",

    'summary': """
        Module Material""",

    'description': """
        Management Material 
    """,

    'author': "Indah Mutiah Utami. MZ",
    'website': "",

    'category': 'Uncategorized',
    'sequence': -100,
    'version': '0.1',

		# Depencicy
    'depends': ['base','asset','board'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        # 'security/access_groups.xml',
        # 'security/record_rules.xml',
        'security/ir.model.access.csv',
        'views/menuitem_materials.views.xml',
        'views/supplier.views.xml',
        'views/material.views.xml',
        
        
    ],
    

    'assets': {
        'web.assets_backend': [
            'materials/static/src/js/app_window_title.js',
            'materials/static/src/js/user_menu.js',
            'materials/static/src/js/dialog.js',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False

}