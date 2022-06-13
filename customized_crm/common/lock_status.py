# -*- coding: utf-8 -*-

from odoo import fields, models


class LockStatus(models.Model):
    _name = 'crm.lock.status'
    _description = '锁定状态'
    _rec_name = 'lock_status'

    lock_status = fields.Char(string='锁定状态', index=True)
