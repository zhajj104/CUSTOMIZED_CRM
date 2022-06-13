# -*- coding: utf-8 -*-

from odoo import fields, models


class Unit(models.Model):
    _name = 'crm.unit'
    _description = '单位'
    _rec_name = 'unit'

    unit = fields.Char(string='单位', index=True)
