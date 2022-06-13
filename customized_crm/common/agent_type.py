# -*- coding: utf-8 -*-

from odoo import fields, models


class AgentType(models.Model):
    _name = 'crm.agent.type'
    _description = '代理类型'
    _rec_name = 'agent_type'

    agent_type = fields.Char(string='代理类型', index=True)
