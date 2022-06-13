# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class User(models.Model):
    _name = 'crm.user'
    _description = 'CRM 人员模块'
    _rec_name = 'nick_name'

    nick_name = fields.Char(string='系统名(昵称)')
    itcode_old = fields.Char(string='ITcode(旧)')
    record_area = fields.Char(string='业务范围')
    company_code = fields.Char(string='公司代码')
    area = fields.Char(string='区域')
    platform = fields.Char(string='平台')
    city = fields.Char(string='所在城市')
    division = fields.Char(string='事业部')
    user_job = fields.Char(string='人员角色')
    user_job_id = fields.Many2one('crm.user.job', string='人员角色id')
    storage_technology_manager = fields.Selection([('是', '是'), ('否', '否'), ('其他', '其他')], string='存储技术经理')
    storage_technology_user = fields.Selection([('是', '是'), ('否', '否'), ('其他', '其他')], string='存储技术人员')
    product_attribute = fields.Char(string='产品属性')
    product_attribute_id = fields.Many2one('crm.product.attribute', string='产品属性id')
    if_open_sales = fields.Selection([('true', '是'), ('false', '否')], string='是否开单销售')
    leader = fields.Char(string='汇报对象')
    leader_id = fields.Many2one('crm.user', string='汇报对象id')
    work_phone = fields.Char(string='办公电话')
    msn = fields.Char(string='msn')
    qq_account = fields.Char(string='qq号码')
    password = fields.Char(string='密码')
    profile_image = fields.Char(string='头像')
    date_of_first_ployment = fields.Datetime(string='就业日期')
    weixin_account = fields.Char(string='微信号码')
    employee_create_time = fields.Datetime(string='员工创建时间')
    owner_department = fields.Char(string='负责人所在部门')
    lock_status = fields.Char(string='锁定状态')
    lock_status_id = fields.Many2one('crm.lock.status', string='锁定状态id')
    working_states = fields.Char(string='心情')
    full_name = fields.Char(string='姓名')
    user_id = fields.Char(string='员工ID')
    extension_number = fields.Char(string='办公电话扩展分机号')
    date_of_joining = fields.Datetime(string='入职日期')
    employee_number = fields.Char(string='ITcode')
    position = fields.Char(string='职位')
    employee_status = fields.Selection([('启用', '启用'), ('禁用', '禁用')], string='员工状态')
    birthday = fields.Datetime(string='生日')
    stop_time = fields.Datetime(string='停用时间')
    description = fields.Char(string='基本信息描述')
    email = fields.Char(string='邮箱')
    owner = fields.Char(string='负责人', index=True)
    owner_id = fields.Many2one('crm.user', string='负责人id')
    is_active = fields.Selection([('true', '是'), ('false', '否')], string='激活')
    life_status = fields.Char(string='生命状态')
    life_status_id = fields.Many2one('crm.life.status', string='生命状态id')
    sex = fields.Selection([('男', '男'), ('女', '女')], string='性别')
    major_department = fields.Char(string='主属部门')
    major_department_id = fields.Many2one('crm.department', string='主属部门ID')
    is_pause_login = fields.Selection([('true', '是'), ('false', '否')], string='禁止登录')
    record_type = fields.Char(string='业务类型')
    name_spell = fields.Char(string='拼音')
    saml2_name_id = fields.Char(string='单点登录账号')
    phone = fields.Char(string='手机')
    language = fields.Char(string='语言')
    language_id = fields.Many2one('crm.language', string='语言id')
    vice_departments = fields.Char(string='附属部门')
    vice_departments_id = fields.Many2one('crm.department', string='附属部门ID')
    login_number = fields.Char(string='登录账号')
    creator = fields.Char(string='创建人')
    creator_id = fields.Many2one('crm.user', string='创建人id')
    data_own_department = fields.Char(string='归属部门')
    data_own_department_id = fields.Many2one('crm.department', string='归属部门ID')
    out_owner = fields.Char(string='外部负责人')
    out_owner_id = fields.Many2one('crm.user', string='外部负责人id')
    last_modifier = fields.Char(string='最后修改人')
    last_modifier_id = fields.Many2one('crm.user', string='最后修改人id')
    create_time = fields.Datetime(string='创建时间', default=lambda self: self.env['crm.common'].get_created_time())
    last_modified_time = fields.Datetime(string='最后修改时间', index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())
    relevant_team = fields.Char(string='相关团队')

    @api.model
    def search_panel_select_range(self, field_name):
        field = self._fields[field_name]
        supported_types = ['many2one']
        if field.type not in supported_types:
            raise UserError(
                _('Only types %(supported_types)s are supported for category (found type %(field_type)s)') % ({
                    'supported_types': supported_types, 'field_type': field.type}))

        Comodel = self.env[field.comodel_name]
        fields = ['display_name']
        parent_name = Comodel._parent_name if Comodel._parent_name in Comodel._fields else False
        if parent_name:
            fields.append(parent_name)
        domain = []
        if Comodel._name == 'crm.department':
            domain = [('dept_status', '=', '启用')]
        return {
            'parent_field': parent_name,
            'values': Comodel.with_context(hierarchical_naming=False).search_read(domain, fields),
        }
