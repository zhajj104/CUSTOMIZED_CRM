# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseForm(models.Model):
    _name = 'crm.purchase.form'
    _description = '项目采购形式model'
    _rec_name = 'purchase_form'

    purchase_form = fields.Char(string='项目采购形式', index=True)
