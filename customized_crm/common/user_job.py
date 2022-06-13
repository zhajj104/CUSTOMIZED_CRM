# -*- coding: utf-8 -*-

from odoo import fields, models, api

class UserJob(models.Model):
    _name = 'crm.user.job'
    _description = '人员角色'
    _rec_name = 'user_job'

    user_job = fields.Char(string='人员角色')