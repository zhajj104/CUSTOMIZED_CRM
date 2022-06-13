# -*- coding: utf-8 -*-

from odoo import fields, models


class FiscalYear(models.Model):
    _name = 'crm.fiscal.year'
    _description = '财年'
    _rec_name = 'fiscal_year'

    fiscal_year = fields.Char(string='财年')
