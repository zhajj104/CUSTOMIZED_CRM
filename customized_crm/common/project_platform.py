# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectPlatform(models.Model):
    _name = 'crm.project.platform'
    _description = '项目所属平台model'
    _rec_name = 'platform'

    platform = fields.Char(string='项目所属平台', index=True)
