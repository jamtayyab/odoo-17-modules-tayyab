# -*- coding: utf-8 -*-
{
    "name": "Update Employee KKN",
    "summary": """
    Purpose was to to close all the quickcreate in the the Employee Module""",
    "license": "LGPL-3",
    "category": "Customizations",
    "version": "17.0.1.0.0",
    "author": "KKN Developers",
    "maintainers": ["Muhammad Tayyab", "Muhammad Muzafar", "Muhammad Husnain"],
    "website": "https://www.kknetworks.com.pk",
    "depends": ["base", "hr", "update_contact_kkn", "planning","hr_holidays","hr_skills"],
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
