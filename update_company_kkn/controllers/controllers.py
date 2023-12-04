# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateCompanyKkn(http.Controller):
#     @http.route('/update_company_kkn/update_company_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_company_kkn/update_company_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_company_kkn.listing', {
#             'root': '/update_company_kkn/update_company_kkn',
#             'objects': http.request.env['update_company_kkn.update_company_kkn'].search([]),
#         })

#     @http.route('/update_company_kkn/update_company_kkn/objects/<model("update_company_kkn.update_company_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_company_kkn.object', {
#             'object': obj
#         })

