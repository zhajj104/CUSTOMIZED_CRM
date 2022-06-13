# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import fields, models, api


class Clients(models.Model):
    _name = 'crm.clients'
    _description = 'CRM 客户模块'
    _rec_name = 'client_name'

    client_number = fields.Char(string='客户编号')

    crm_number = fields.Char(string='CRM编号')
    client_type = fields.Char(string='客户类型')
    client_type_id = fields.Many2one('crm.client.type', string='客户类型ID')
    industry_classification = fields.Char(string='行业一级分类')
    industry_classification_id = fields.Many2one('crm.first.industry', string='行业一级分类ID')
    channel_type = fields.Char(string='渠道类型')
    channel_type_id = fields.Many2one('crm.channel.type', string='渠道类型ID')
    union_channel = fields.Char(string='联盟渠道')
    union_channel_id = fields.Many2one('crm.union.channel', string='联盟渠道ID')
    business_manager = fields.Char(string='商务经理')
    business_manager_id = fields.Many2one('crm.user', string='商务经理ID')
    erp_client_number = fields.Char(string='ERP客户编号')
    client_name = fields.Char(string='客户名称', required=True)
    client_level = fields.Char(string='客户级别')
    client_level_id = fields.Many2one('crm.client.level', string='客户级别ID')
    secondary_classification = fields.Char(string='行业二级分类')
    secondary_classification_id = fields.Many2one('crm.second.industry', string='行业二级分类ID')
    related_core_channel = fields.Char(string='关联核心渠道')
    client_manager = fields.Char(string='客户经理')
    client_manager_id = fields.Many2one('crm.user', string='客户经理ID')
    group_leader = fields.Char(string='组长')
    group_leader_id = fields.Many2one('crm.user', string='组长ID')
    telephone = fields.Char(string='电话')
    fax = fields.Char(string='传真')
    client_url = fields.Char(string='网址')
    created_by = fields.Char(string="创建人")
    created_by_id = fields.Many2one('crm.user', string="创建人ID")
    create_time = fields.Datetime(string='创建时间', default=lambda self: self.env['crm.common'].get_created_time())

    country = fields.Char(string='国家')
    country_id = fields.Many2one('crm.districts.dict', string='国家ID')
    province = fields.Char(string='省')
    province_id = fields.Many2one('crm.districts.dict', string='省ID')
    city = fields.Char(string='市')
    city_id = fields.Many2one('crm.districts.dict', string='市ID')
    district = fields.Char(string='区')
    district_id = fields.Many2one('crm.districts.dict', string='区ID')
    address = fields.Char(string='详细地址')

    unified_social_credit_code = fields.Char(string='统一社会信用代码')
    legal_representative = fields.Char(string='法定代表人')
    registered_capital = fields.Char(string='注册资本')
    company_type = fields.Char(string='公司类型')
    registration_authority = fields.Char(string='登记机关')
    business_scope = fields.Text(string='经营范围')
    registration_status = fields.Char(string='登记状态')
    registered_address = fields.Char(string='注册地址')
    establishment_date = fields.Date(string='成立日期')
    registration_number = fields.Char(string='注册号')
    approved_date = fields.Date(string='核准日期')
    enterprise_qualification_annex = fields.Text(string='企业资质附件')

    back_reason = fields.Char(string='销售人员退回原因')
    back_reason_id = fields.Many2one('crm.back.reason', string='销售人员退回原因ID')

    next_followed_remark = fields.Text(string='下次跟进要点')
    is_er_enterprise = fields.Selection([('true', 'true'), ('false', 'false')], string='是否关联对接企业')
    email = fields.Char(string='邮件')
    biz_reg_name = fields.Selection([('true', 'true'), ('false', 'false')], string='工商注册')
    next_followed_time = fields.Datetime(string='下次跟进时间')
    remark = fields.Text(string='备注')
    partner_id = fields.Char(string='合作伙伴')
    out_owner = fields.Char(string='外部负责人')
    out_owner_id = fields.Many2one('crm.user', string='外部负责人ID')
    account_source = fields.Char(string='来源')
    account_source_id = fields.Many2one('crm.account.source', string='来源ID')

    staff_structure_diagram = fields.Char(string='人员架构图')
    agent_operating_brand = fields.Char(string='代理商经营品牌')
    acting_cooperative_brand = fields.Text(string='代理合作品牌')
    sellers_number = fields.Integer(string='销售人员数量')
    covering_client_industry = fields.Char(string='覆盖客户所属行业')
    covering_client_industry_id = fields.Many2one('crm.cover.client.industry', string='覆盖客户所属行业ID')
    client_owned_solution = fields.Text(string='客户自有解决方案')
    software_development_ability = fields.Selection([('有', '有'), ('无', '无')], string='软件开发能力')
    organization_chart = fields.Char(string='组织架构图')
    agent_top3_client_name = fields.Text(string='代理top3客户名称')
    technicians_number = fields.Integer(string='技术人员数量')
    agent_type = fields.Char(string='代理类型')
    agent_type_id = fields.Many2one('crm.agent.type', string='代理类型ID')
    technology_and_qualification_certificate = fields.Text(string='技术和资质证书')
    cloud_service_capabilities = fields.Selection([('有', '有'), ('无', '无')], string='云服务能力')

    pipeline_ids = fields.One2many('crm.pipeline', 'agent_name_id', string='Pipeline')
    contacts_ids = fields.One2many('crm.contacts', 'customer_name_id', string='联系人')

    last_modified_time = fields.Datetime(string='最后修改时间', index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        res = super(Clients, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        for i in res:
            for item in self._fields.keys():
                if item in i.keys() and (not i[item] or i[item] == ''):
                    i[item] = '--'
        return res

    # 国家
    @api.onchange('country')
    def _onchange_country(self):
        if self.country:
            self.province = False
            self.city = False
            self.district = False

    # 省
    @api.onchange('province')
    def _onchange_province(self):
        if self.province:
            self.city = False
            self.district = False

    # 市
    @api.onchange('city')
    def _onchange_city(self):
        if self.city:
            self.district = False

    def search_pipeline_detail(self):
        return {
            'name': '商机明细',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.pipeline',
            'view_mode': 'tree',
            'target': 'new',
            'views': [((self.env.ref('customized_crm.pipeline_tree')).id, 'tree')],
            'domain': [('agent_name', '=', self.client_name)],
            'view_id': (self.env.ref('customized_crm.pipeline_tree')).id,
            'search_view_id': (self.env.ref('customized_crm.pipeline_search')).id
        }
