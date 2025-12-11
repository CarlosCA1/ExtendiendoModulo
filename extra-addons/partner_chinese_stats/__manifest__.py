# -*- coding: utf-8 -*-
{
    'name': "partner_chinese_stats",
    'summary': "Extiende contactos con Signo Chino y Fidelización",
    'description': """
Este módulo extiende el modelo res.partner añadiendo:
- Fecha de nacimiento
- Edad (calculada automáticamente)
- Signo del horóscopo chino (calculado automáticamente)
- Código de Socio
- Nivel de Fidelidad (Premium, Gold, Estándar)
""",
    'author': "Empleado sufridor",
    'website': "https://www.nocobrolosuficiente.com",
    'category': 'Contacts',
    'version': '0.2',

    'depends': ['base', 'contacts'],

    'data': [
        'views/views.xml',
    ],
}

