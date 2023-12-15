
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Saletype(models.Model):
    _name = 'kk.sale.type'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'sale_type'

    sale_type = fields.Char(string= 'Sale Type', required=True, tracking=True,)
    current_user = fields.Char(string='Created By', readonly=True, tracking=True,)

    @api.onchange('sale_type')
    def set_user_name(self):
        self.current_user = self.env.user.name


