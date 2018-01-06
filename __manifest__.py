# -*- coding: utf-8 -*-
{
    'name': "exercise",

    'summary': """Module developed as a technical demonstration for recruitment purposes""",

    'description': """
    This module extends the Sales Management module to add a text field on sales.order, have
    it displayed in the view form and in the related report and can be translated.
    """,

    'author': "Florian Mortgat",
    'website': "https://github.com/FlorianMortgat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/views.xml',
        # 'security/ir.model.access.csv',
        #'views/templates.xml',
        'report/sale_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
}
