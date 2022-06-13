# -*- coding: utf-8 -*-

from odoo import fields, models


class DistributeFail(models.Model):
    _name = 'crm.distribute.fail'
    _description = '分销输单原因model'
    _rec_name = 'distribute_failed_reason'

    distribute_failed_reason = fields.Char(string='分销输单原因', index=True)
