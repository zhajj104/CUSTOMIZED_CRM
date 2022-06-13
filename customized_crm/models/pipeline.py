# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import fields, models, api


class Pipeline(models.Model):
    _name = 'crm.pipeline'
    _description = 'CRM Pipeline'
    _rec_name = 'business_name'

    business_name = fields.Char(string='商机名称', required=True)
    principal = fields.Char(string='负责人')
    principal_id = fields.Many2one('crm.user', string='负责人id')
    own_department = fields.Char(string='负责人所在部门', related='principal_id.data_own_department_id.dept_name', store=True)
    project_platform = fields.Char(string='项目所属平台')
    project_platform_id = fields.Many2one('crm.project.platform', string='项目所属平台id')
    business_process = fields.Char(string='商机流程')
    business_process_id = fields.Many2one('crm.business.process', string='商机流程id')
    process_group = fields.Integer(related='business_process_id.process_group', string='商机流程分组')
    amount = fields.Float(string='商机金额（元）')
    enduser_name = fields.Char(string='最终用户名称')
    enduser_name_id = fields.Many2one('crm.clients', string='最终用户名称id')
    agent_name = fields.Char(string='代理商名称')
    agent_name_id = fields.Many2one('crm.clients', string='代理商名称id')
    expected_sign_date = fields.Datetime(string='预计签约日期')
    created_time = fields.Datetime(string='创建时间', default=lambda self: self.env['crm.common'].get_created_time())
    last_modified_time = fields.Datetime(string='最后修改时间', index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())
    business_source = fields.Char(string='商机来源')
    business_source_id = fields.Many2one('crm.business.source', string='商机来源id')
    business_type = fields.Char(string='商机类型')
    business_area = fields.Char(string='商机区域')
    first_industry = fields.Char(string='用户一级行业')
    first_industry_id = fields.Many2one('crm.first.industry', string='一级行业id')
    second_industry = fields.Char(string='用户二级行业')
    second_industry_id = fields.Many2one('crm.second.industry', string='二级行业id')
    requirements_doc = fields.Char(string='需求文档')
    solution_doc = fields.Char(string='方案文档')
    pre_saling_support = fields.Char(string='售前支持')
    project_purchase_form = fields.Char(string='项目采购形式')
    project_purchase_form_id = fields.Many2one('crm.purchase.form', string='项目采购形式id')
    competitor = fields.Char(string='竞争对手')
    payment_mode = fields.Char(string='客户付款方式')
    payment_mode_id = fields.Many2one('crm.payment.mode', string='客户付款方式id')
    payment_terms = fields.Char(string='客户付款条款')
    expected_profit_rate = fields.Float(string='预计利润率')
    expected_profit = fields.Float(string='预计利润金额')
    expected_delivery_date = fields.Datetime(string='预计交货日期')
    success_summary = fields.Char(string='赢单总结')
    expected_income_date = fields.Datetime(string='预计确认收入时间')
    suspend_type = fields.Char(string='中止类型')
    suspend_type_id = fields.Many2one('crm.suspend.type', string='中止类型id')
    suspend_explain = fields.Char(string='中止说明')
    project_failed_reason = fields.Char(string='项目分销输单原因')
    project_failed_reason_id = fields.Many2one('crm.project.fail', string='项目分销输单原因id')
    straight_failed_reason = fields.Char(string='直客输单原因')
    straight_failed_reason_id = fields.Many2one('crm.straight.fail', string='直客输单原因id')
    total_failed_reason = fields.Char(string='总代输单原因')
    total_failed_reason_id = fields.Many2one('crm.total.fail', string='总代输单原因id')
    distribute_failed_reason = fields.Char(string='分销输单原因')
    distribute_failed_reason_id = fields.Many2one('crm.distribute.fail', string='分销输单原因id')
    closed_order_time = fields.Datetime(string='关单时间')
    sales_stage = fields.Char(string='商机阶段')
    stage_id = fields.Many2one(comodel_name='crm.business.stage', string='商机阶段id', ondelete='restrict', index=True,
                               group_expand='_read_group_stage_ids', default=1)
    kanban_state = fields.Selection([('normal', 'In Progress'),
                                     ('blocked', 'Blocked'),
                                     ('done', 'Ready for next stage')],
                                    string='Kanban State', default='normal')
    business_detail_ids = fields.One2many('crm.business.detail', 'business_detail_id', string="商机明细")
    active = fields.Boolean(default=True)
    data_own_department = fields.Char(string='归属部门')
    data_own_department_id = fields.Many2one('crm.department', string='归属部门id')
    creator = fields.Char(string='创建人')
    creator_id = fields.Many2one('crm.user', string='创建人id')

    @api.depends('stage_id')
    def _get_stage_status(self):
        """
        商机状态
        """
        for record in self:
            if record.stage_id.stage_type.stage_status == '赢单':
                record.stage_status = '赢单'
            elif record.stage_id.stage_type.stage_status == '无效':
                record.stage_status = '无效'
            elif record.stage_id.stage_type.stage_status == '输单':
                record.stage_status = '输单'
            else:
                record.stage_status = '进行中'

    stage_status = fields.Char(string='商机状态', compute=_get_stage_status, store=True)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """
        扩展stage_id
        """
        # 默认看板视图显示商机出现、方案交流、招投标及报价、中标及商务、赢单、输单、项目中止7种阶段
        domain = [('id', 'in', [1, 2, 3, 4, 5, 6, 7])]
        stage_ids = stages._search(domain, order=order, access_rights_uid=1)
        return stages.browse(stage_ids)

    def go_to_business_detail_tree(self):
        """
        返回商机明细列表页
        """
        view_id = (self.env.ref('customized_crm.dc_crm_business_detail_tree')).id
        search_view_id = (self.env.ref('customized_crm.dc_crm_business_detail_search')).id
        action = {
            'name': '商机明细',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.business.detail',
            'view_mode': 'tree,form',
            'target': 'new',
            'views': [(view_id, 'tree')],
            'view_id': view_id,
            'search_view_id': search_view_id,
        }
        return action

    def read(self, fields=None, load='_classic_read'):
        datas = super().read(fields=fields, load=load)
        if len(self.ids) == 1:
            for data in datas:
                if data.get('requirements_doc'):
                    if data.get('requirements_doc') != '[]':
                        data['requirements_doc'] = data.get('requirements_doc').split(',')[2].split(':')[1]
                    else:
                        data['requirements_doc'] = ''
                if data.get('solution_doc'):
                    if data.get('solution_doc') != '[]':
                        data['solution_doc'] = data.get('solution_doc').split(',')[2].split(':')[1]
                    else:
                        data['solution_doc'] = ''
        return datas

    def pipeline_invalid(self):
        """
        Pipeline作废
        """
        self.active = False

    def pipeline_recover(self):
        """
        Pipeline恢复
        """
        self.active = True
