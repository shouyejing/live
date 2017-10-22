#coding=utf-8


from odoo import models, fields, api

import re

# 班级
class Classinfo(models.Model):
    _name = 'live.cls_info'
    _description = u'班级信息'

    name = fields.Char('班级名称', required=True)
    desc = fields.Text('班级描述')
    notice = fields.Text('班级通知')
    image = fields.Binary('图片')
    member = fields.One2many('live.cls_member', 'cls_id', '班级成员')
    manager = fields.One2many('live.cls_manager', 'cls_id', '班委成员')
    cls_nums = fields.Integer('班级人数', compute='_compute_cls_nums')

    # 每个班级有多个动态
    tag_ids = fields.One2many('live.tag', 'cls_id', '班级动态')
    act_ids = fields.One2many('live.cls_act', 'id', '班级活动')

    # 计算字段方法二(better)
    @api.depends('member')
    def _compute_cls_nums(self):
        for rec in self:
            rec.cls_nums = len(rec.member)


# 班级成员表
class ClsMember(models.Model):
    _name = 'live.cls_member'
    _description = u'班级id表'

    cls_id = fields.Many2one('live.cls_info', '班级id')
    cls_member= fields.Many2one('res.users', '用户id')


# 班委成员表
class ClsManager(models.Model):
    _name = 'live.cls_manager'
    _description = u'班委id表'

    cls_id = fields.Many2one('live.cls_info', '班级id')
    cls_manager = fields.Many2one('res.users', '用户id')


# 班级活动
class ClassActivity(models.Model):
    _name = 'live.cls_act'
    _description = u'班级活动'

    name = fields.Char('活动名称')
    desc = fields.Text('活动描述')
    notice = fields.Text('活动要求')
    date = fields.Date('活动时间')

