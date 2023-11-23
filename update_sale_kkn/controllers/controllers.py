# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateSaleKkn(http.Controller):
#     @http.route('/update_sale_kkn/update_sale_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_sale_kkn/update_sale_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_sale_kkn.listing', {
#             'root': '/update_sale_kkn/update_sale_kkn',
#             'objects': http.request.env['update_sale_kkn.update_sale_kkn'].search([]),
#         })

#     @http.route('/update_sale_kkn/update_sale_kkn/objects/<model("update_sale_kkn.update_sale_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_sale_kkn.object', {
#             'object': obj
#         })

