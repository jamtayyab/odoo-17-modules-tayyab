# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LeadSource(models.Model):
    _name = 'kk.lead.source'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'lead_source'

    lead_source = fields.Char(string='Lead Source', required=True, tracking=True,)
    current_user = fields.Char(string='Created By', readonly=True, tracking=True,)

    @api.onchange('lead_source')
    def set_user_name(self):
        self.current_user = self.env.user.name






