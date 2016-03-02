# -*- coding: utf-8 -*-
{
    'name': "Project Issue Service",

    'summary': """
        This module adds many extras to the Project Issue module.
        """,

    'description': """
        There are many extra, like costs, and multiple contacts.
    """,

    'author': "Michael Watchorn",
    'website': "http://www.thewatchorngroup.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project.issue', 'sale'],
    'data': [
             #"views/views.xml",
             #"data/project_issue_service_data.xml",
             #"security/ir.model.access.csv"],
    'demo': [],
    'tests': [],
}
