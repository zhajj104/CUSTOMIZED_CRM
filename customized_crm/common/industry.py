#!/usr/bin/env python
# -*- coding:utf-8 -*-

from odoo import fields, models


class Industry(models.Model):
    _name = 'crm.industry'
    _description = '行业分类表'
    _rec_name = 'name'

    name = fields.Char(string='行业分类')
    parent_id = fields.Char(string='父行业ID')
    industry_type = fields.Char(string="行业级别")
    last_modified_time = fields.Datetime(string="最后修改时间", index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())

    def name_get(self):
        return [(item.id, '%s' % (item.name)) for item in self]
