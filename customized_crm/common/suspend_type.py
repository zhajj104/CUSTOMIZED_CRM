# -*- coding: utf-8 -*-

from odoo import fields, models


class SuspendType(models.Model):
    _name = 'crm.suspend.type'
    _description = '中止类型model'
    _rec_name = 'suspend_type'

    suspend_type = fields.Char(string='中止类型', index=True)
