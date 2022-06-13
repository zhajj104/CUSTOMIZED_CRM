# -*- coding: utf-8 -*-
from odoo import fields, models


class Products(models.Model):
    _name = 'crm.products'
    _description = '产品模块'
    _rec_name = 'product_name'

    product_attribution_system = fields.Char(string='产品归属系统')
    product_attribution_system_id = fields.Many2one('crm.product.attribution.system', string='产品归属系统ID')
    product_no = fields.Char(string='产品编号')
    product_name = fields.Char(string='产品名称')
    headquarters = fields.Char(string='本部')
    bu = fields.Char(string='事业部')
    brand = fields.Char(string='品牌')
    category = fields.Char(string='分类')
    category_id = fields.Many2one('crm.product.category', string='分类ID')
    product_description = fields.Text(string='产品概述')
    remark = fields.Text(string='备注')
    cloud_native = fields.Selection([('是', '是'), ('否', '否')], string='云原生')
    digital_native = fields.Selection([('是', '是'), ('否', '否')], string='数字原生')

    off_shelves_time = fields.Datetime(string='下架时间')
    price = fields.Float(string='标准价格')
    mnemonic_code = fields.Char(string='助记码')
    barcode = fields.Char(string='条形码')
    maintenance_period = fields.Integer(string='保养周期（天）')
    order_field = fields.Integer(string='排序')
    product_line = fields.Char(string='产品线')
    product_line_id = fields.Many2one('crm.product.line', string='产品线ID')
    unit = fields.Char(string='单位')
    unit_id = fields.Many2one('crm.unit', string='单位ID')

    product_status = fields.Char(string='上下架')
    product_status_id = fields.Many2one('crm.product.status', string='上下架ID')
    replacement_period = fields.Integer(string='更换周期（天）')
    product_code = fields.Char(string='产品编码')
    on_shelves_time = fields.Datetime(string='上架时间')
    safety_stock = fields.Integer(string='安全库存')
    general_channel_sellers_award = fields.Float(string='普通渠道销售员奖励')
    sales_department_profit = fields.Float(string='销售部门利润')

    chinese_brand = fields.Char(string='中文品牌')
    english_brand = fields.Char(string='英文品牌')
    approver_phone = fields.Char(string='审批人手机')
    is_third_party_outsource = fields.Selection([('是', '是'), ('否', '否')], string="是否第三方外购")
    is_video_cloud_business = fields.Selection([('是', '是'), ('否', '否')], string="是否为视频云商机")

    video_cloud_business_classification = fields.Char(string="视频云商机分类")
    video_cloud_business_classification_id = fields.Many2one('crm.video.cloud.business.classification',
                                                             string="视频云商机分类ID")
    product_native_type = fields.Char(string='产品原生类型')
    model = fields.Char(string='型号')
    owner_department = fields.Char(string='负责人所在部门')
    owner = fields.Char(string='负责人')
    owner_id = fields.Many2one('crm.user', string='负责人ID')
    lock_status = fields.Char(string="锁定状态")
    lock_status_id = fields.Many2one('crm.lock.status', string="锁定状态ID")
    life_status = fields.Char(string="生命状态")
    life_status_id = fields.Many2one('crm.life.status', string="生命状态ID")
    technical_parameter = fields.Text(string='技术参数')
    record_type = fields.Char(string="业务类型")
    product_spec = fields.Char(string="规格属性")
    create_time = fields.Datetime(string="创建时间", default=lambda self: self.env['crm.common'].get_created_time())
    created_by = fields.Char(string="创建人")
    created_by_id = fields.Many2one('crm.user', string="创建人ID")
    data_own_department = fields.Char(string="归属部门")
    data_own_department_id = fields.Many2one('crm.department', string="归属部门ID")
    out_owner = fields.Char(string="外部负责人")
    out_owner_id = fields.Many2one('crm.user', string="外部负责人ID")
    last_modified_by = fields.Char(string="最后修改人")
    last_modified_by_id = fields.Many2one('crm.user', string="最后修改人ID")
    last_modified_time = fields.Datetime(string="最后修改时间", index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())

    product_detail_ids = fields.One2many('crm.business.detail', 'product_detail_id', string='商机明细')
