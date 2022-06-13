# -*- coding: utf-8 -*-

from odoo import fields, models


class SecondIndustry(models.Model):
    _name = 'crm.second.industry'
    _description = 'pipeline 二级行业model'
    _rec_name = 'second_industry_name'

    second_industry_name = fields.Char(string='二级行业名称', index=True)
    parent_id = fields.Many2one('crm.first.industry', string='父id')
