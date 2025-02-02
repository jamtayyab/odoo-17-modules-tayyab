# -*- coding: utf-8 -*-
{
    "name": "Update Sale KKN",
    "summary": """
       Purpose was to close all the quickcreate in the the Sale Module""",
    "license": "LGPL-3",
    "category": "Customizations",
    "version": "17.0.1.0.0",
    "author": "KKN Developers",
    "maintainers": ["Muhammad Tayyab", "Muhammad Muzafar"],
    "website": "https://www.kknetworks.com.pk",
    "depends": ["base", "sale", "sale_management"],
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/account.xml",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}
