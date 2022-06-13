#!/usr/bin/env python
# -*- coding:utf-8 -*-

from odoo import fields, models


class ClientType(models.Model):
    _name = 'crm.client.type'
    _rec_name = 'name'
    _description = '客户类型'

    name = fields.Char(string='客户级别', index=True)
    parent_id = fields.Char(string='父行业ID')
    client_type = fields.Char(string="客户类型", index=True)

    def name_get(self):
        return [(item.id, '%s' % (item.name)) for item in self]
