# -*- coding: utf-8 -*-

from odoo import fields, models


class TotalFail(models.Model):
    _name = 'crm.total.fail'
    _description = '总代输单原因model'
    _rec_name = 'total_failed_reason'

    total_failed_reason = fields.Char(string='总代输单原因', index=True)
