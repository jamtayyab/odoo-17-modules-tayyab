# -*- coding: utf-8 -*-
{
    "name": "Update Front Desk",
    "summary": """
       Purpose was to to close all the quickcreate in the the frontDesk Module""",
    "license": "LGPL-3",
    "category": "Customizations",
    "version": "17.0.1.0.0",
    "author": "KKN Developers",
    "maintainers": ["Muhammad Tayyab", "Muhammad Muzafar", "Muhammad Husnain"],
    "website": "https://www.kknetworks.com.pk",
    "depends": ["base", "frontdesk"],
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
        'views/templates.xml',
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}


#
# # -*- coding: utf-8 -*-
# {
#     'name': "update_frontdesk",
#
#     'summary': "purpose was to to close all the quickcreate in the the FrontDesk Module",
#
#     'description': """
# Long description of module's purpose
#     """,
#
#     'author': "kk Developers",
#     'website': "https://www.kknetworks.com.pk",
#
#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Customizations',
#     'version': '0.1',
#
#     # any module necessary for this one to work correctly
#     'depends': ['base','frontdesk'],
#
#     # always loaded
#     'data': [
#         # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
#     "license": "LGPL-3",
# }
#
