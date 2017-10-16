#coding=utf-8


from odoo import models, fields, api

import re

# 直播房间
class LivingRoom(models.Model):
    _name = 'living.room'
    _description = u'直播房间信息'

    name = fields.Char('直播间名称', required=True)
    # 用id作为房间号
    # room_id = fields.Integer('房间号')
    type = fields.Many2one('living.type', '直播类型')
    living_url = fields.Char('直播地址')
    living_users = fields.One2many(comodel_name='living.living_user_ids', inverse_name='living_room_id' , string='主播表')
    online_users = fields.One2many(comodel_name='living.online_user_ids', inverse_name='living_room_id' , string='在线用户表')

    living_user_ids = fields.Char("主播ids", compute='get_living_ids')
    living_user_nick = fields.Char("主播昵称", compute='get_living_info')
    living_user_city = fields.Char("主播城市", compute='get_living_info')


    image = fields.Binary('封面图片')
    click_nums = fields.Integer('人气', default=0)
    online_nums = fields.Integer('在线人数')


    @api.returns
    def afun(self):
        return self.living_users

    # 计算字段方法一
    @api.onchange('online_users')
    def _online_count(self):
        # 测试
        nums = len(self.online_users)
        self.online_nums = nums
        # console.log
        print("在线人数：%s" % nums)

    @api.model
    def get_living_ids(self):
        record_set = self.search([])
        pattern = re.compile('\d+')
        # 每个房间的主播列表
        for rec in record_set:
            ids_list = pattern.findall(str(rec.living_users))
            users_list = []
            # 可能有多个主播
            for id in ids_list:
                res_users = rec.env["living.living_user_ids"].\
                    search([("id", "=", id)]).living_user_id
                userds_list.append(",".join(pattern.findall(str(res_users))))
            rec.living_user_ids =  ",".join(users_list)
            return

    @api.model
    def get_living_info(self):
        record_set = self.search([])
        for rec in record_set:
            id = rec.living_user_ids
            user_record = rec.env["res.users"].search([("id", "=", id)])
            rec.living_user_nick = user_record.nick_name
            rec.living_user_city = user_record.city
            return user_record.city + user_record.nick_name

# 主播id表
class LivingUserIds(models.Model):
    _name = 'living.living_user_ids'
    _description = u'主播id表'

    living_room_id = fields.Many2one('living.room', '房间id')
    living_user_id = fields.Many2one('res.users', '主播id')


# 在线用户id表
class OnlineUserIds(models.Model):
    _name = 'living.online_user_ids'
    _description = u'在线用户id表'

    living_room_id = fields.Many2one('living.room', '房间id')
    online_user_id = fields.Many2one('res.users', '用户id')


# 直播列表
class LivingType(models.Model):
    _name = 'living.type'
    _description = u'直播类型'

    name = fields.Char('类型名称')
    desc = fields.Char('类型描述')