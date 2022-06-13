# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BusinessRecordSystem(models.Model):
    _name = 'crm.business.record.system'
    _description = '商机业务类型-系统'
    _rec_name = 'business_record_type_system'

    business_record_type_system = fields.Char(string='商机业务类型-系统')
