# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateHrRecruitmentKkn(http.Controller):
#     @http.route('/update_hr_recruitment_kkn/update_hr_recruitment_kkn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_hr_recruitment_kkn/update_hr_recruitment_kkn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_hr_recruitment_kkn.listing', {
#             'root': '/update_hr_recruitment_kkn/update_hr_recruitment_kkn',
#             'objects': http.request.env['update_hr_recruitment_kkn.update_hr_recruitment_kkn'].search([]),
#         })

#     @http.route('/update_hr_recruitment_kkn/update_hr_recruitment_kkn/objects/<model("update_hr_recruitment_kkn.update_hr_recruitment_kkn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_hr_recruitment_kkn.object', {
#             'object': obj
#         })

