# -*- coding: utf-8 -*-

from odoo import fields, models


class PaymentMode(models.Model):
    _name = 'crm.payment.mode'
    _description = '客户付款方式model'
    _rec_name = 'payment_mode'

    payment_mode = fields.Char(string='客户付款方式', index=True)
