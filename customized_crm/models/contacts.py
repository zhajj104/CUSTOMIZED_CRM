# -*- coding: utf-8 -*-
from datetime import datetime
import re
from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class Contacts(models.Model):
    _name = 'crm.contacts'
    _description = 'CRM 联系人模块'
    _rec_name = 'name'

    # 邮箱合法性正则
    MAIL_REGEXP = re.compile(
        r'^[0-9a-zA-Z_-]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}[\.]{0,1}[cn]{0,2}$'
    )
    # 座机合法性正则 （须包含区号）
    TEL_REGEXP = re.compile(r'^0\d{2,3}-\d{7,8}$')
    # 手机号合法性正则 （需为11位整数）
    PHONE_REGEXP = re.compile(r'^\d{11}$')

    customer_name = fields.Char(string='客户名称')
    customer_name_id = fields.Many2one('crm.clients', string='客户名称id')
    name = fields.Char(string='姓名')
    sex = fields.Selection([('男', '男'), ('女', '女')], string='性别')
    department = fields.Char(string='部门')
    position = fields.Char(string='职务')
    phone = fields.Char(string='手机')
    telephone = fields.Char(string='电话')
    mail = fields.Char(string='邮箱')
    address = fields.Text(string='地址')
    business_card = fields.Many2many('ir.attachment', string='名片')
    company_name = fields.Char(string='公司名称')
    age = fields.Integer(string='年龄')
    birthday = fields.Datetime(string='生日')
    birthday_year = fields.Integer(string='生日-年')
    birthday_month = fields.Integer(string='生日-月')
    birthday_day = fields.Integer(string='生日-日')
    nation = fields.Char(string='民族')
    hometown = fields.Char(string='籍贯')
    graduated_school = fields.Char(string='毕业院校')
    hobby = fields.Text(string='个人爱好')
    resume = fields.Text(string='工作简历')
    living_habit = fields.Text(string='生活习惯')
    family_situation = fields.Text(string='家庭情况')
    key_relatives = fields.Text(string='其他关键亲属')
    social_relationship = fields.Text(string='社会关系')
    experience = fields.Text(string='工作经历')
    position_situation = fields.Text(string='岗位情况')
    motivation = fields.Char(string='动机')
    company_worth = fields.Char(string='如何呈现公司价值')
    data_own_department = fields.Char(string='归属部门')
    data_own_department_id = fields.Many2one('crm.department', string="归属部门ID")
    principal = fields.Char(string='负责人')
    principal_id = fields.Many2one('crm.user', string='负责人id')
    business_type = fields.Char(string='业务类型', default='集团-业务类型')
    creator = fields.Char(string='创建人')
    creator_id = fields.Many2one('crm.user', string='创建人id')
    create_time = fields.Datetime(string='创建时间', default=lambda self: self.env['crm.common'].get_created_time())
    last_modified_time = fields.Datetime(string='最后修改时间', index=True,
                                         default=lambda self: self.env['crm.common'].get_created_time())
    principal_department = fields.Char(string='负责人主属部门', related="principal_id.major_department")

    @api.model
    def create(self, vals):
        self.validate_fields(vals)
        return super().create(vals)

    def write(self, vals):
        self.validate_fields(vals)
        return super().write(vals)

    def validate_fields(self, vals):
        """
        验证手机号码、电话、邮箱合法性
        """
        if 'phone' in vals and vals['phone'] and not self.validate_field_phone(vals['phone']):
            raise ValidationError("手机号码输入格式不正确，应为11位整数")
        if 'telephone' in vals and vals['telephone'] and not self.validate_field_telephone(vals['telephone']):
            raise ValidationError("电话输入格式不正确，若为座机，须包含区号")
        if 'mail' in vals and vals['mail'] and not self.validate_field_mail(vals['mail']):
            raise ValidationError("邮箱输入格式不正确")

    def validate_field_phone(self, phone):
        """
        验证手机号码
        """
        if self.PHONE_REGEXP.match(phone):
            return True
        return False

    def validate_field_telephone(self, telephone):
        """
        验证电话号码
        """
        if self.TEL_REGEXP.match(telephone):
            return True
        if self.PHONE_REGEXP.match(telephone):
            return True
        return False

    def validate_field_mail(self, mail):
        """
        验证邮箱
        """
        if self.MAIL_REGEXP.match(mail):
            return True
        return False

    def read(self, fields=None, load='_classic_read'):
        datas = super().read(fields=fields, load=load)
        if len(self.ids) == 1:
            for data in datas:
                if data.get('birthday_day') and not data.get('birthday') and 0 not in [data.get('birthday_year'),
                                                                                       data.get('birthday_month'),
                                                                                       data.get('birthday_day')]:
                    if data.get('birthday_month') < 10:
                        birthday_month = "0%s" % (data.get('birthday_month'))
                    else:
                        birthday_month = str(data.get('birthday_month'))
                    if data.get('birthday_day') < 10:
                        birthday_day = "0%s" % (data.get('birthday_day'))
                    else:
                        birthday_day = str(data.get('birthday_day'))
                    birthday = "%s-%s-%s" % (data.get('birthday_year'), birthday_month, birthday_day)
                    data['birthday'] = datetime.strptime(birthday, "%Y-%m-%d")
        return datas
