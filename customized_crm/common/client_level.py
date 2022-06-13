# -*- coding: utf-8 -*-

from odoo import fields, models


class ClientLevel(models.Model):
    _name = 'crm.client.level'
    _description = '客户级别'
    _rec_name = 'client_level'

    client_level = fields.Char(string='客户级别')
    parent_id = fields.Many2one('crm.client.type', string='父id')
