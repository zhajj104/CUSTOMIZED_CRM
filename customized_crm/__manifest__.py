# -*- coding: utf-8 -*-
{
    'name': "customized_crm",
    'sequence': 1,
    'category': 'CRM-ODOO应用',
    'summary': """CUSTOMIZED-CRM""",
    'description': """CUSTOMIZED-CRM""",
    'author': "zhajj",
    'website': "http://www.yourcompany.com",
    # for the full list
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'images': [
        'static/images/main_screenshot.png'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/pipeline_tree.xml',
        'views/pipeline_form.xml',
        'views/contacts_tree.xml',
        'views/contacts_form.xml',
        'views/clients_tree.xml',
        'views/clients_form.xml',
        'views/sub_table.xml',
        'views/products_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}
