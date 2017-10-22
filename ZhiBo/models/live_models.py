#coding=utf-8


from odoo import models, fields, api


# 直播房间
class LiveRoom(models.Model):
    _name = 'live.room'
    _description = u'直播房间信息'

    cid = fields.Char()
    name = fields.Char('直播间名称', required=True)
    type = fields.Many2one('live.type', '直播类型')
    live_url = fields.Char('直播地址')
    live_users = fields.One2many(comodel_name='live.live_user_ids', inverse_name='live_room_id' , string='主播表')
    online_users = fields.One2many(comodel_name='live.online_user_ids', inverse_name='live_room_id' , string='在线用户表')

    live_user_nick = fields.Char(string="主播昵称", compute='get_live_info')
    live_user_city = fields.Char(string="主播城市", compute='get_live_info')

    image = fields.Binary('封面图片')
    click_nums = fields.Integer('人气')
    online_nums = fields.Integer('在线人数', compute="_online_count")

    @api.depends("online_users")
    def _online_count(self):
        for rec in self:
            rec.online_nums = len(rec.online_users)

    def get_live_info(self):
        for rec in self:
            users = rec.live_users.live_user_id
            rec.live_user_nick = users.nick_name
            rec.live_user_city = users.city


# 主播id表
class LiveUserIds(models.Model):
    _name = 'live.live_user_ids'
    _description = u'主播id表'

    live_room_id = fields.Many2one('live.room', '房间id')
    live_user_id = fields.Many2one('res.users', '主播id')


# 在线用户id表
class OnlineUserIds(models.Model):
    _name = 'live.online_user_ids'
    _description = u'在线用户id表'

    live_room_id = fields.Many2one('live.room', '房间id')
    online_user_id = fields.Many2one('res.users', '用户id')


# 直播列表
class LiveType(models.Model):
    _name = 'live.type'
    _description = u'直播类型'

    name = fields.Char('类型名称')
    desc = fields.Char('类型描述')