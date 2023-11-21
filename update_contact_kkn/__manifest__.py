# -*- coding: utf-8 -*-
{
    "name": "Update Contact KKN",
    "summary": """
       This Module upgrades the Contact Module""",
    "license": "LGPL-3",
    "category": "Customizations",
    "version": "17.0.1.0.0",
    "author": "KKN Developers",
    "maintainers": ["Muhammad Tayyab", "Muhammad Muzafar", "Muhammad Husnain"],
    "website": "https://www.kknetworks.com.pk",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence_data.xml",
        "views/res_district.xml",
        "views/res_region.xml",
        "views/res_tier.xml",
        "views/res_station.xml",
        "views/res_partner.xml",
        "data/data.xml",
        "data/res.station.csv",
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}
