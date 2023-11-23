# -*- coding: utf-8 -*-
{
    "name": "Update Recruitment KKN",
    "summary": """
       Purpose was to close all the quickcreate in the the Recruitment Module""",
    "license": "LGPL-3",
    "category": "Customizations",
    "version": "17.0.1.0.0",
    "author": "KKN Developers",
    "maintainers": ["Muhammad Tayyab", "Muhammad Muzafar", "Muhammad Husnain"],
    "website": "https://www.kknetworks.com.pk",
    "depends": ["base", "hr_recruitment","hr_referral"],
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

