# -*- coding: utf-8 -*-

from odoo import fields, models


class FirstIndustry(models.Model):
    _name = 'crm.first.industry'
    _description = 'pipeline 一级行业model'
    _rec_name = 'first_industry_name'

    first_industry_name = fields.Char(string='一级行业名称', index=True)
