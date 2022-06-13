# -*- coding: utf-8 -*-

from odoo.tests import tagged, common, logging


@tagged('clients')
class ClientsTest(common.TransactionCase):
    # 测试部门
    def setUp(self):
        super(ClientsTest, self).setUp()

    def test_create_client(self):
        logging.info("创建客户测试开始")

        self.clients = {
            'client_name': '测试公司一',
            'client_number': '222222',
            'client_type': '1',
            'client_level': '10',
        }

        self.created_clients = self.env['crm.clients'].create(self.clients)
        self.assertIsNotNone(self.created_clients.id, msg="数据未正常保存")

        logging.info("创建客户测试结束")