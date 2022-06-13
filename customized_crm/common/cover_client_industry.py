# -*- coding: utf-8 -*-

from odoo import fields, models


class CoverClientIndustry(models.Model):
    _name = 'crm.cover.client.industry'
    _description = '覆盖客户所属行业'
    _rec_name = 'covering_client_industry'

    covering_client_industry = fields.Char(string='覆盖客户所属行业', index=True)
