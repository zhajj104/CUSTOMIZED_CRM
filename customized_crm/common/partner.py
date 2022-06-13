# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _name = 'crm.partner'
    _description = '合作伙伴'
    _rec_name = 'name'

    name = fields.Char(string='合作伙伴名称')
