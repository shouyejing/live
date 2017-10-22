#coding=utf-8


from datetime import datetime


from odoo import models, fields, api
from datetime import datetime


# 个人信息
class UserInfo(models.Model):
    '扩展res.users'
    _inherit = 'res.users'

    nick_name = fields.Char('昵称')
    introduce = fields.Text('自我介绍', default='这家伙很懒,什么都没有留下。')
    gender = fields.Selection(
        [
            ('male', '男'),
            ('female', '女'),
        ],
        '性别',
        default='male'
    )
    birthday = fields.Date('生日')
    city = fields.Char('城市')
    job = fields.Char('职业')
    class_id = fields.Many2one('live.cls_info', '班级')
    gold = fields.Integer('金币', default=0)
    prize = fields.Integer('奖品', default=0)
    #每个用户有多个动态
    tag_ids = fields.One2many('live.tag', 'user_id', '动态')


# 教师信息
class Teacher(models.Model):
    _name = 'live.teacher'
    _description = u'教师信息'
    
    # org  = fields.One2many('live.org', 'org_id', '所属机构')
    name = fields.Char('教师姓名', required=True)
    work_years = fields.Integer('工作年限', default=0)
    work_company = fields.Char('就职公司')
    work_position = fields.Char('公司职位')
    points = fields.Char('教学特点')
    click_nums = fields.Integer('点击数', default=0)
    fav_nums = fields.Integer('收藏数', default=0)

    
# 邮箱验证码    
class EmailVerifyRecord(models.Model):
    _name = 'live.email_verifyrecord'
    _description = u'邮箱验证码'
    
    code = fields.Char('邮箱验证码')
    email = fields.Char('邮箱')
    send_type = fields.Selection(
        [
            ('register', '注册'),
            ('forget', '找回密码')
        ], 
        '验证码类型',
        default='forget'   
    )
    send_time = fields.Datetime.now('发送时间')