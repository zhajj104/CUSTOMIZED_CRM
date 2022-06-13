# -*- coding: utf-8 -*-

from odoo import fields, models


class BusinessSource(models.Model):
    _name = 'crm.business.source'
    _description = 'pipeline 商机来源model'
    _rec_name = 'source_name'

    source_name = fields.Char(string='商机来源', index=True)
