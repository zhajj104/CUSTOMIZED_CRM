# -*- coding: utf-8 -*-

from odoo import fields, models


class StageStatus(models.Model):
    _name = 'crm.stage.status'
    _description = '阶段状态model'
    _rec_name = 'stage_status'

    stage_status = fields.Char(string='阶段状态', index=True)
