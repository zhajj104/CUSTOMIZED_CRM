# -*- coding: utf-8 -*-

from odoo import fields, models


class BusinessProcess(models.Model):
    _name = 'crm.business.process'
    _description = '商机流程model'
    _rec_name = 'process_name'

    process_name = fields.Char(string='业务模式', index=True)
    process_group = fields.Integer(string='业务模式分组')
