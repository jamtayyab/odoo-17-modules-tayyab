# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateEmployeeKkn(http.Controller):
#     @http.route('/update_employee_kkn/update_employee_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_employee_kkn/update_employee_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_employee_kkn.listing', {
#             'root': '/update_employee_kkn/update_employee_kkn',
#             'objects': http.request.env['update_employee_kkn.update_employee_kkn'].search([]),
#         })

#     @http.route('/update_employee_kkn/update_employee_kkn/objects/<model("update_employee_kkn.update_employee_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_employee_kkn.object', {
#             'object': obj
#         })

