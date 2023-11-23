# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateFrontdesk(http.Controller):
#     @http.route('/update_frontdesk/update_frontdesk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_frontdesk/update_frontdesk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_frontdesk.listing', {
#             'root': '/update_frontdesk/update_frontdesk',
#             'objects': http.request.env['update_frontdesk.update_frontdesk'].search([]),
#         })

#     @http.route('/update_frontdesk/update_frontdesk/objects/<model("update_frontdesk.update_frontdesk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_frontdesk.object', {
#             'object': obj
#         })

