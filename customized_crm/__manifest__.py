# -*- coding: utf-8 -*-
{
    'name': "customized_crm",
    'sequence': 1,
    'category': 'CRM-ODOO应用',
    'summary': """This module will customize a CRM application to adapt to domestic personnel, including four modules: customer, contact, pipeline and product""",
    'description': """本模块将自定义一个CRM应用用来适配国内人员，包含客户、联系人、Pipeline和产品等四个模块""",
    'author': "zhajj",
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
    'license': 'LGPL-3',
}
