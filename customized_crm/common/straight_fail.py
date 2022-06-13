# -*- coding: utf-8 -*-

from odoo import fields, models


class StraightFail(models.Model):
    _name = 'crm.straight.fail'
    _description = '直客输单原因model'
    _rec_name = 'straight_failed_reason'

    straight_failed_reason = fields.Char(string='直客输单原因', index=True)
