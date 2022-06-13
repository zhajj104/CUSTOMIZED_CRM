# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductLine(models.Model):
    _name = 'crm.product.line'
    _description = '产品线'
    _rec_name = 'product_line'

    product_line = fields.Char(string='产品线', index=True)
