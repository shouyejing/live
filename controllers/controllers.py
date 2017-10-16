# coding=utf-8

from odoo import http


import json


class MyController(http.Controller):
    @http.route('/living/api', type='http', auth='public')
    def index(self):
        Banner = http.request.env['living.banner']
        banner = Banner.search_read([], ['id','name'])

        Living_room = http.request.env['living.room']
        living_room = Living_room.search_read([], ['id','name'])

        query_set = {
            'banner': banner,
            'living_room': living_room
        }

        response = json.dumps(query_set, ensure_ascii=False)
        return response

    @http.route('/http', type='http', auth="none")
    def xhttp(self):
        return self.xmagic()

    @http.route('/json', type='json', auth="none")
    def xjson(self):
        return self.xmagic(reqtype='json')

    def xmagic(self, reqtype='http'):
        l = ['a', 'b', 'c']
        if reqtype == 'http':
            return str(l)
        else:
            return l
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