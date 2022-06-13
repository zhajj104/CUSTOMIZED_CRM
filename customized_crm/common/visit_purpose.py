# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VisitPurpose(models.Model):
    _name = 'crm.visit.purpose'
    _description = '拜访目的'
    _rec_name = 'visit_purpose'

    visit_purpose = fields.Char(string='拜访目的')
