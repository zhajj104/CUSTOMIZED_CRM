# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BusinessDetail(models.Model):
    _name = 'crm.business.detail'
    _description = '商机明细'
    _rec_name = 'name'

    name = fields.Char(string="商机明细编码")
    expected_sale_amount = fields.Float(string="预计落单金额（元）")
    product_line_cadres = fields.Char(string="产品线本部")
    product_line_division = fields.Char(string="产品线事业部")
    third_party_outsource = fields.Selection([('是', '是'), ('否', '否')], string="是否第三方外购")
    group_product = fields.Char(string="集团产品")
    record_type = fields.Char(string="业务类型")
    principal = fields.Char(string="负责人")
    principal_id = fields.Many2one('crm.user', string='负责人id')
    remark = fields.Char(string="备注")
    creator = fields.Char(string="创建人")
    creator_id = fields.Many2one('crm.user', string='创建人id')
    last_modifier = fields.Char(string="最后修改人")
    last_modifier_id = fields.Many2one('crm.user', string="最后修改人id")
    created_time = fields.Datetime(string="创建时间", default=lambda self: self.env['crm.common'].get_created_time())
    last_modified_time = fields.Datetime(string="最后修改时间", index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())
    quantity = fields.Integer(string="数量")
    sale_price = fields.Float(string="销售单价（元）")

    business_id = fields.Char(string="商机")
    business_detail_id = fields.Many2one('crm.pipeline', string='商机id')
    product_id = fields.Char(string="产品线名称")
    product_detail_id = fields.Many2one('crm.products', string='产品线名称id')

    category = fields.Char(string="分类")
    discount = fields.Float(string='折扣(%)')
    owner_department = fields.Char(string='负责人所在部门')

    def write(self, vals):
        vals['last_modified_time'] = self.env['crm.common'].get_created_time()
        return super().write(vals)

    def go_to_business_detail_form(self):
        """
        查看商机明细详情页
        """
        view_id = (self.env.ref('customized_crm.dc_crm_business_detail_form')).id
        action = {
            'name': '商机明细',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.business.detail',
            'view_mode': 'tree,form',
            'target': 'new',
            'views': [(view_id, 'form')],
            'view_id': view_id,
            'res_id': self.id,
            'context': dict(self.env.context, form_view_custom_mode='readonly')
        }
        return action
