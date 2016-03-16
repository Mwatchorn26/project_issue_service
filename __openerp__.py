# -*- coding: utf-8 -*-
{
    'name': "project_issue_service",

    'summary': """
        Service and warranty additions for Project Issues""",

    'description': """
        This module adds Issue Resolution, Issue Dates, Costs, Service Team members, and Customer Site Contacts.
    """,

    'author': "Michael Watchorn",
    'website': "http://www.theWatchornGroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'project_issue', 'sale','hr'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/hr_employee.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
