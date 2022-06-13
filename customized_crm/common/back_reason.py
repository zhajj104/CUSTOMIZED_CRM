# -*- coding: utf-8 -*-

from odoo import fields, models


class BackReason(models.Model):
    _name = 'crm.back.reason'
    _description = '销售人员退回原因'
    _rec_name = 'back_reason'

    back_reason = fields.Char(string='销售人员退回原因', index=True)
