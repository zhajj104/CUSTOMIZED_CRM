# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import datetime


class Common(models.Model):
    _name = 'crm.common'
    _description = 'CRM公共方法'
    _auto = False

    def get_created_time(self):
        """
        获取当前时间
        """
        time = datetime.now()
        return time
