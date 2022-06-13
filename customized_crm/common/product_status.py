# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductStatus(models.Model):
    _name = 'crm.product.status'
    _description = '上下架'
    _rec_name = 'product_status'

    product_status = fields.Char(string='上下架', index=True)
