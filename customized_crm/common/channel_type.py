# -*- coding: utf-8 -*-

from odoo import fields, models


class ChannelType(models.Model):
    _name = 'crm.channel.type'
    _description = '渠道类型'
    _rec_name = 'channel_type'

    channel_type = fields.Char(string='渠道类型', index=True)
