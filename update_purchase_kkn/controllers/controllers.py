# -*- coding: utf-8 -*-
# from odoo import http


# class UpdatePurchaseKkn(http.Controller):
#     @http.route('/update_purchase_kkn/update_purchase_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_purchase_kkn/update_purchase_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_purchase_kkn.listing', {
#             'root': '/update_purchase_kkn/update_purchase_kkn',
#             'objects': http.request.env['update_purchase_kkn.update_purchase_kkn'].search([]),
#         })

#     @http.route('/update_purchase_kkn/update_purchase_kkn/objects/<model("update_purchase_kkn.update_purchase_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_purchase_kkn.object', {
#             'object': obj
#         })

