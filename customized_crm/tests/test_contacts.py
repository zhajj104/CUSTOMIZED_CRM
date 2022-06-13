# -*- coding: utf-8 -*-

from odoo.tests import tagged, common, logging


@tagged('contacts')
class TestContacts(common.TransactionCase):
    # 测试部门
    TEST_MODEL = 'crm.contacts'

    def setUp(self):
        super(TestContacts, self).setUp()

        self.phone = {
            'phone': '12345678909',
        }

        self.telephone = {
            'telephone': '027-1234567',
        }

        self.mail = {
            'mail': '3564665@qq.com',
        }

    def test_validate_field(self):
        logging.info("手机号码、电话、邮箱校验开始测试")

        self.contacts = {
            'customer_name': 'xxx公司',
            'name': '张三',
            'sex': '0',
            'department': '总部',
            'position': '总经理',
            'phone': self.phone.get('phone'),
            'telephone': self.telephone.get('telephone'),
            'mail': self.mail.get('mail'),
        }

        self.created_contacts = self.env[self.TEST_MODEL].create(self.contacts)

        validate_phone = self.env[self.TEST_MODEL].validate_field_phone(self.created_contacts.phone)
        validate_telephone = self.env[self.TEST_MODEL].validate_field_telephone(self.created_contacts.telephone)
        validate_mail = self.env[self.TEST_MODEL].validate_field_mail(self.created_contacts.mail)

        # 断言
        self.assertEqual(validate_phone, True, msg="手机号码校验测试不通过")
        self.assertEqual(validate_telephone, True, msg="电话校验测试不通过")
        self.assertEqual(validate_mail, True, msg='邮箱校验测试不通过')

        logging.info("手机号码、电话、邮箱校验测试结束")
