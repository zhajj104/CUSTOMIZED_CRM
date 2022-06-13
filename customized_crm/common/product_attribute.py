# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProductAttribute(models.Model):
    _name = 'crm.product.attribute'
    _description = '产品属性'
    _rec_name = 'product_attribute'

    product_attribute = fields.Char(string='产品属性')