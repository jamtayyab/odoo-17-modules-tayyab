# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateTimeOffKkn(http.Controller):
#     @http.route('/update_time_off_kkn/update_time_off_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_time_off_kkn/update_time_off_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_time_off_kkn.listing', {
#             'root': '/update_time_off_kkn/update_time_off_kkn',
#             'objects': http.request.env['update_time_off_kkn.update_time_off_kkn'].search([]),
#         })

#     @http.route('/update_time_off_kkn/update_time_off_kkn/objects/<model("update_time_off_kkn.update_time_off_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_time_off_kkn.object', {
#             'object': obj
#         })

