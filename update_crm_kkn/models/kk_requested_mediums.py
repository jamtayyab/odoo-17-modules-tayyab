from odoo import models, fields, api

class RequestedMediums(models.Model):
    _name = 'kk.requested.medium'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'requested_medium'


    requested_medium = fields.Char(string= 'Requested Medium', tracking=True, required = True)
    current_user = fields.Char(string='Created By', tracking=True, readonly=True)

    @api.onchange('requested_medium')
    def set_user_name(self):
        self.current_user = self.env.user.name

