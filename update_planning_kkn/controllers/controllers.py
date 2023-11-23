# -*- coding: utf-8 -*-
# from odoo import http


# class UpdatePlanningKkn(http.Controller):
#     @http.route('/update_planning_kkn/update_planning_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_planning_kkn/update_planning_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_planning_kkn.listing', {
#             'root': '/update_planning_kkn/update_planning_kkn',
#             'objects': http.request.env['update_planning_kkn.update_planning_kkn'].search([]),
#         })

#     @http.route('/update_planning_kkn/update_planning_kkn/objects/<model("update_planning_kkn.update_planning_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_planning_kkn.object', {
#             'object': obj
#         })

