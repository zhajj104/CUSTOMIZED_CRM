# -*- coding: utf-8 -*-

from odoo import fields, models


class LifeStatus(models.Model):
    _name = 'crm.life.status'
    _description = '生命状态'
    _rec_name = 'life_status'

    life_status = fields.Char(string='生命状态', index=True)
