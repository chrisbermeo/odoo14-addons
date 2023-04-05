# -*- coding: utf-8 -*-
{
    'name': "Modo de pago en sale order",

    'summary': """
        Modulo de prueba para el curso de Odoo 14""",

    'description': """
        Modulo de prueba para el curso de Odoo 14
    """,

    'author': "Christian Bermeo",
    'website': "http://www.yourcompany.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order_view.xml'
    ],
}
