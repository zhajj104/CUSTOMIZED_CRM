# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductAttributionSystem(models.Model):
    _name = 'crm.product.attribution.system'
    _description = '产品归属系统'
    _rec_name = 'product_attribution_system'

    product_attribution_system = fields.Char(string='产品归属系统', index=True)
