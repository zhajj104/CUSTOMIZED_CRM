# -*- coding: utf-8 -*-

from odoo import fields, models


class DevelopmentStage(models.Model):
    _name = 'crm.development.stage'
    _description = '发展阶段'
    _rec_name = 'development_stage'

    development_stage = fields.Char(string='发展阶段', index=True)
