# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectFail(models.Model):
    _name = 'crm.project.fail'
    _description = '项目分销输单原因model'
    _rec_name = 'project_failed_reason'

    project_failed_reason = fields.Char(string='项目分销输单原因', index=True)
