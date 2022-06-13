# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CommonController(http.Controller):
    # 获取模型的视图id
    @http.route('/model/selectModelViewId', type='json', auth='public')
    def select_model_view_id(self):
        model_name = http.request.params.get("model_name")
        view_type = http.request.params.get("view_type")
        name = http.request.params.get("name")
        sql = "SELECT id as viewId FROM ir_ui_view where name = '%s' and model= '%s' and type ='%s'" % \
              (str(name), str(model_name), str(view_type))
        cursor = request.env.cr
        cursor.execute(sql)
        view_id = cursor.dictfetchall()
        return {"code": "200", "msg": "success", 'id': view_id}
