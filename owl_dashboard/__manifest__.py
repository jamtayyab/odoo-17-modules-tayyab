# -*- coding: utf-8 -*-
{
    "name": "Owl dashboard",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "license": "LGPL-3",
    "author": "Odoo Community Association (OCA)",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sales",
    "application": True,
    "installable": True,
    "version": "17.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "web", "sale", "board"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "owl_dashboard/static/src/components/**/*.js",
            "owl_dashboard/static/src/components/**/*.xml",
            "owl_dashboard/static/src/components/**/*.scss",
        ],
    },
}
