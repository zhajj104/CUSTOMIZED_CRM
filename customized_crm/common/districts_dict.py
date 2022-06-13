#!/usr/bin/env python
# -*- coding:utf-8 -*-

from odoo import fields, models, api


class DistrictsDict(models.Model):
    _name = 'crm.districts.dict'
    _description = '地区表'
    _rec_name = 'name'

    address_code = fields.Char(string='地址编码', required=True)
    name = fields.Char(string='区域')
    parent_id = fields.Char(string='父区域ID')
    district_type = fields.Char(string="地区类型")
    last_modified_time = fields.Datetime(string="最后修改时间", index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())

    def name_get(self):
        return [(item.id, '%s' % (item.name)) for item in self]
