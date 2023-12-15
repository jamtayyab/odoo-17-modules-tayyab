# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KKBranchTypes(models.Model):
    _name = 'kk.branch.type'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    kk_branch = fields.Char(string='Branch Name', required=True, tracking=True)
    current_user = fields.Char(string='Created By', readonly = True, tracking=True)

    @api.onchange('kk_branch')
    def set_user_name(self):
        current_user_ = self.env.user
        self.current_user = current_user_.name
