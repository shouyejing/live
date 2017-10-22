# coding=utf-8


from odoo import http
from odoo.http import request

import os
import json
import base64
import qrcode


from api163 import  channel_create, channel_update, channel_delete, channel_list


class MyController(http.Controller):
    # 创建频道
    @http.route('/app/channel/create', type='http', auth='public')
    def channel_create(self, name=None, uid=None, type=0):
        if not (name and uid):
            return '{"msg": "创建失败：缺少参数", "code": 999}'

        channel_name = u"三融科技-%s"%name
        response = channel_create(channel_name, type)
        res_dict = json.loads(response)
        if res_dict.get("code") == 200:
            ret = res_dict.get("ret")
            cid = ret.get("cid")
            # 创建房间
            live_rec = request.env["live.room"].sudo().create({
                "cid": cid,
                "name": channel_name
            })
            live_rec.live_url = ret.get("rtmpPullUrl")
            # 添加主播
            request.env["live.live_user_ids"].sudo().create({
                "live_room_id": live_rec.id,
                "live_user_id": uid
            })

        return response

    # 修改频道
    @http.route('/app/channel/update', type='http', auth='public')
    def channel_update(self, name=None, cid=None, type=0):
        if not (name and cid):
            return '{"msg": "修改失败：缺少参数", "code": 999}'
        pass

    # 删除频道
    @http.route('/app/channel/delete', type='http', auth='public')
    def channel_delete(self, cid=None):
        if cid == None:
            return '{"msg": "删除失败：缺少参数", "code": 999}'
        response = channel_delete(cid)
        res_dict = json.loads(response)
        if res_dict.get("code") == 200:
            request.env["live.room"].sudo().search([("cid", "=", cid)]).unlink()
        return response

    # 获取频道列表
    @http.route('/app/channel/list', type='json', auth='public', methods=['GET'])
    def channel_list(self):
        response = channel_list()
        return response

    # @http.route('/http', type='http', auth="none")
    # def xhttp(self):
    #     return self.xmagic()
    #
    # @http.route('/json', type='json', auth="none")
    # def xjson(self):
    #     return self.xmagic(reqtype='json')

    # @http.route('/todo/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{} ({})</h1>'.format(name, type(name).__name__)

    # # 指定类型
    # @http.route('/todo/<int:id>/', auth='public', website=True)
    # def teacher_id(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    #
    # # 用模块作参数
    # @http.route('/teacher/<model("todo.teachers"):id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return http.request.render('todo_task.biography', {
    #         'person': id
    #     })

    @http.route('/generate', auth='public', website=True)
    def generate(self, text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()

        BASE_DIR = os.environ.get("HOME")
        path = BASE_DIR + '/odoo-dev/custom-addons/ZhiBo/static/img/test.png'

        img.save(path)
        with open(path, "rb") as f:
            b = f.read()
        b64 = base64.b64encode(b)
        img =  "data:image/png;base64," + b64
        return http.request.render("ZhiBo.qrcode", {"img": img})
