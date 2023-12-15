# -*- coding: utf-8 -*-
{
    "name": "Update Inventory KKN",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """
        Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Customizations",
    "version": "17.0.0.0",
    # any module necessary for this one to work correctly
    "post_init_hook": "_auto_post_init",
    "depends": [
        "base",
        "stock",
        "update_company_kkn",
        "update_contact_kkn",
        "base_geolocalize",
        "stock_picking_batch",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        # "data/stock_location.xml",
        "views/views.xml",
        "views/templates.xml",
        "views/product_template_view.xml",
        "views/stock_picking_view.xml",
        "views/stock_scrap_view.xml",
        "views/stock_warehouse_orderpoint_view.xml",
        "views/stock_quant_package_view.xml",
        "views/stock_lot_view.xml",
        "views/stock_picking_batch_view.xml",
        # "views/switchport_view.xml",
        "views/update_location.xml",
        "views/update_contact_stock_location_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
    "application": True,
    "installable": True,
}
