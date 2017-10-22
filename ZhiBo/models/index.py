#coding=utf-8


from odoo import models, fields, api


# 直播房间
class Banner(models.Model):
    _name = 'live.banner'
    _description = u'轮播图'

    name = fields.Char('轮播图名称')
    image = fields.Binary("图片")
    redirect_link = fields.Char("跳转链接")