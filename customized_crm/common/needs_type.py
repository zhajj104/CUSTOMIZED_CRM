# -*- coding: utf-8 -*-

from odoo import fields, models


class NeedsType(models.Model):
    _name = 'crm.needs.type'
    _description = '需求类型'
    _rec_name = 'needs_type'

    needs_type = fields.Char(string='需求类型', index=True)
