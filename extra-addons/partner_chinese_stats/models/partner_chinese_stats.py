# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class PartnerChineseStats(models.Model):
    _inherit = 'res.partner'

    f_nac = fields.Date("Fecha de nacimiento")
    edad = fields.Integer(
        string="Edad",
        readonly=True,
        compute="_calcular_edad",
        store=True
    )
    signo_chino = fields.Char(
        string="Signo Chino",
        readonly=True,
        compute="_calcular_chinada",
        store=True
    )

    # Nuevos campos de fidelización
    codigo_socio = fields.Char(string="Código de Socio")
    nivel_fidelidad = fields.Selection(
        [
            ('estandar', 'Estándar'),
            ('premium', 'Premium'),
            ('gold', 'Gold')
        ],
        string="Nivel de Fidelidad",
        readonly=True,
        compute="_calcular_fidelidad",
        store=True
    )

    # Funciones
    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                today = date.today()
                record.edad = today.year - record.f_nac.year - (
                    (today.month, today.day) < (record.f_nac.month, record.f_nac.day) # Sirve para comprobar si ya ha pasado el cumpleaños en el año actual. Resta 1 si es true.
                )
            else:
                record.edad = 0


    @api.depends('f_nac')
    def _calcular_chinada(self):
        signos = [
            "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
            "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
        ]
        for record in self:
            if record.f_nac:
                year = record.f_nac.year
                record.signo_chino = signos[(year - 4) % 12] # Se toma como referencia el año 4 d.C. como inicio del ciclo
            else:
                record.signo_chino = "Sin signo"

    @api.depends('codigo_socio')
    def _calcular_fidelidad(self):
        for record in self:
            if record.codigo_socio:
                if record.codigo_socio.startswith("G"):
                    record.nivel_fidelidad = 'gold'
                else:
                    record.nivel_fidelidad = 'premium'
            else:
                record.nivel_fidelidad = 'estandar'