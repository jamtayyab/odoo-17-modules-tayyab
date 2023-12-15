# -*- coding: utf-8 -*-
{
    "name": "update_crm_kkn",
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
    "depends": ["base", "crm", "sale", "update_account_kkn","sale_crm"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/crm_stages.xml",
        "views/crm_stages.xml",
        "views/views.xml",
        "views/templates.xml",
        # "views/crm_lead_view_kk.xml",
        "views/kk_branch_type.xml",
        "views/kk_sale_type.xml",
        "views/kk_lead_sources.xml",
        "views/kk_requested_medium.xml",
        "views/kk_crm_form.xml",
        "views/crm_lead2opportunity.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
    "application": True,
}
