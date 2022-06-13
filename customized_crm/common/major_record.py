# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MajorRecord(models.Model):
    _name = 'crm.major.record'
    _description = '主业务类型'
    _rec_name = 'major_record_type'

    major_record_type = fields.Char(string='主业务类型')
