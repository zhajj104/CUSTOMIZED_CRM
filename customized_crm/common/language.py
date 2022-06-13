# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Language(models.Model):
    _name = 'crm.language'
    _description = '语言'
    _rec_name = 'language'

    language = fields.Char(string='语言')