# -*- coding: utf-8 -*-

from odoo import fields, models


class UnionChannel(models.Model):
    _name = 'crm.union.channel'
    _description = '是否为联盟渠道'
    _rec_name = 'union_channel'

    union_channel = fields.Char(string='联盟渠道', index=True)
