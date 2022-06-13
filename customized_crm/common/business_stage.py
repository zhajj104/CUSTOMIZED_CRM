# -*- coding: utf-8 -*-

from odoo import fields, models, api


class BusinessStage(models.Model):
    _name = 'crm.business.stage'
    _description = 'CRM Pipeline 商机阶段model'
    _rec_name = 'stage_name'
    _order = 'sequence, stage_name, id'

    stage_id = fields.Integer(string='阶段编号')
    stage_name = fields.Char(string='商机阶段', index=True)
    win_probability = fields.Integer(string='赢率')
    stage_type = fields.Many2one('crm.stage.status', string='阶段类型')
    business_process_id = fields.Integer(string='商机流程分组id')
    sequence = fields.Integer(string='Sequence', default=1)
    fold = fields.Boolean(string='折叠')

    def name_get(self):
        res = []
        for record in self:
            display_name = "%s  %s%s" % (record.stage_name, record.win_probability, '%')
            add_data = (record.id, display_name)
            res.append(add_data)
        return res
