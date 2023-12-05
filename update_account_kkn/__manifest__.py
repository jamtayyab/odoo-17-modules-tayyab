# -*- coding: utf-8 -*-
{
    "name": "update_account_kkn",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Customizations",
    "version": "17.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "sale", "update_contact_kkn"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/templates.xml",
        "views/account_move_view.xml",
        "views/account_payment_view.xml",
        "views/res_partner.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
}
