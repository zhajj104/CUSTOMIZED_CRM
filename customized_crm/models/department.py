# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Department(models.Model):
    _name = 'crm.department'
    _description = '部门'
    _rec_name = 'dept_name'
    _parent_name = 'dept_parent_id'

    dept_name = fields.Char(string='部门名称')
    dept_code = fields.Char(string='部门编码')
    dept_parent_path = fields.Text(string='部门祖先路径')
    owner = fields.Char(string='负责人')
    owner_id = fields.Many2one('crm.user', string='负责人ID')
    lock_status = fields.Char(string="锁定状态")
    lock_status_id = fields.Many2one('crm.lock.status', string="锁定状态ID")
    life_status = fields.Char(string="生命状态")
    life_status_id = fields.Many2one('crm.life.status', string="生命状态ID")
    dept_children = fields.Char(string='部门子部门序列')
    dept_children_id = fields.Many2one('crm.department', string='部门子部门序列ID')
    manager = fields.Char(string='部门负责人')
    manager_id = fields.Many2one('crm.user', string='部门负责人ID')
    owner_department = fields.Char(string='负责人所在部门')
    dept_parent = fields.Char(string='上级部门')
    dept_parent_id = fields.Many2one('crm.department', string='上级部门ID')
    data_own_department = fields.Char(string='归属部门')
    data_own_department_id = fields.Many2one('crm.department', string='归属部门ID')
    dept_id = fields.Char(string='部门ID')
    dept_status = fields.Selection([('启用', '启用'), ('停用', '停用')], string="部门状态")
    record_type = fields.Char(string="业务类型")
    assistant = fields.Char(string='助理')
    assistant_id = fields.Many2one('crm.user', string='助理ID')
    out_owner = fields.Char(string='外部负责人')
    out_owner_id = fields.Many2one('crm.user', string='外部负责人ID')
    created_by = fields.Char(string="创建人")
    created_by_id = fields.Many2one('crm.user', string="创建人ID")
    create_time = fields.Datetime(string="创建时间", default=lambda self: self.env['crm.common'].get_created_time())
    last_modified_by = fields.Char(string="最后修改人")
    last_modified_by_id = fields.Many2one('crm.user', string="最后修改人")
    last_modified_time = fields.Datetime(string="最后修改时间", index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())
    relevant_team = fields.Char(string='相关团队')

    @api.depends('dept_id')
    def _get_dept_id(self):
        for record in self:
            if record.dept_id:
                record.dept = self.env['crm.department'].search([('dept_id', '=', record.dept_id)]).id
            else:
                record.dept = record.id

    dept = fields.Integer(string='本部门ID', compute=_get_dept_id, store=True)

    def set_manager(self):
        view_id = (self.env.ref('customized_crm.dc_department_manager_form')).id
        action = {
            'name': '设置部门负责人',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.department',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
            'views': [(view_id, 'form')],
            'view_id': view_id,
        }
        return action

    def set_assistant(self):
        view_id = (self.env.ref('customized_crm.dc_department_assistant_form')).id
        action = {
            'name': '设置部门负责人',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.department',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
            'views': [(view_id, 'form')],
            'view_id': view_id,
        }
        return action
