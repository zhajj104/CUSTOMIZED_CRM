# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Transactions(models.Model):
    _name = 'crm.transactions'
    _description = '交易方'
    _rec_name = 'transaction'

    transaction = fields.Char(string='交易方')
