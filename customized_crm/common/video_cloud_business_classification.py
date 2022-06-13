# -*- coding: utf-8 -*-

from odoo import fields, models


class VideoCloudBusinessClassification(models.Model):
    _name = 'crm.video.cloud.business.classification'
    _description = '视频云商机分类'
    _rec_name = 'video_cloud_business_classification'

    video_cloud_business_classification = fields.Char(string='视频云商机分类', index=True)
