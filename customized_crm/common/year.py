# -*- coding: utf-8 -*-

from odoo import fields, models


class Year(models.Model):
    _name = 'crm.year'
    _description = '年份'
    _rec_name = 'year'

    year = fields.Char(string='年份')
