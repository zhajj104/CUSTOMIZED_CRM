# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountSource(models.Model):
    _name = 'crm.account.source'
    _description = '来源'
    _rec_name = 'account_source'

    account_source = fields.Char(string='来源', index=True)
