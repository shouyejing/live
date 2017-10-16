#coding=utf-8


from odoo import models, fields, api


import re

# 朋友圈
class MateCircle(models.Model):
    _name = 'living.cls.circle'
    _description = u'同学圈'

    tag_id = fields.Char()
    name = fields.Char()
    content = fields.Char()
    image_ids = fields.Char()

    @api.model
    def get_tags(self):
        pass
# 动态
class Tag(models.Model):
    _name = 'living.tag'
    _description = u'动态'

    content = fields.Text('说说内容')
    images = fields.One2many('living.image_store', 'tag_id', '说说图片库')
    praise = fields.One2many('living.praise', 'tag_id', '赞')
    comment = fields.One2many('living.comment', 'tag_id', '评论')
    click_nums = fields.Integer('点击量', default=0)

    user_id = fields.Many2one('res.users', '用户id')
    cls_id = fields.Many2one('living.cls_info', '班级id')

    name = fields.Char(compute="get_info")
    image_ids = fields.Char(compute="get_info")
    image = fields.Binary(compute="get_info")

    @api.model
    def get_info(self):
        pattern = re.compile('\d+')
        for rec in self:
            if rec.user_id:
                id = ",".join(pattern.findall(str(rec.user_id)))
                rec.name = rec.env["res.users"].search([("id", "=", id)]).name
            else:
                id = ",".join(pattern.findall(str(rec.cls_id)))
                rec.name = rec.env["living.cls_info"].search([("id", "=", id)]).name
                rec.image = rec.env["living.cls_info"].search([("id", "=", id)]).image

            rec.image_ids = ",".join(pattern.findall(str(rec.images)))

        return "hello world"


# tag图片仓库
class ImageStore(models.Model):
    _name = 'living.image_store'
    _description = u'动态图片仓库'

    tag_id = fields.Many2one('living.tag', '动态id')
    image = fields.Binary('说说图片')


# 评论
class Comment(models.Model):
    _name = 'living.comment'
    _description = u'评论'

    user_id = fields.Many2one('res.users', '用户id')
    tag_id = fields.Many2one('living.tag', '动态id')
    content = fields.Text('评论内容')


# 赞
class Praise(models.Model):
    _name = 'living.praise'
    _description = u'赞'

    user_id = fields.Many2one('res.users', '用户id')
    tag_id = fields.Many2one('living.tag', '动态id')