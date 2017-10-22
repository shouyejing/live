#coding=utf-8


from odoo import models, fields, api


# 课程
class Course(models.Model):
    _name =  'live.course'
    _description = u'课程信息'

    name = fields.Char('课程名称')
    desc = fields.Char('课程描述')
    detail = fields.Text('课程详情')
    students = fields.Integer('学习人数', default=0)
    fav_nums = fields.Integer('收藏人数', default=0)
    image = fields.Binary('封面图片')
    click_nums = fields.Integer('人气', default=0)