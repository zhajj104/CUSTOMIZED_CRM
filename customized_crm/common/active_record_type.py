# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ActiveRecordType(models.Model):
    _name = 'crm.active.record.type'
    _description = '跟进类型'
    _rec_name = 'active_record_type'

    active_record_type = fields.Char(string='跟进类型')


