# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateAccountKkn(http.Controller):
#     @http.route('/update_account_kkn/update_account_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_account_kkn/update_account_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_account_kkn.listing', {
#             'root': '/update_account_kkn/update_account_kkn',
#             'objects': http.request.env['update_account_kkn.update_account_kkn'].search([]),
#         })

#     @http.route('/update_account_kkn/update_account_kkn/objects/<model("update_account_kkn.update_account_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_account_kkn.object', {
#             'object': obj
#         })

