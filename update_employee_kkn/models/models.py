# -*- coding: utf-8 -*-


from odoo import models, fields, api

class update_employee_kkn(models.Model):
    _inherit = 'hr.employee'

    station_id = fields.Many2one('res.station', string='Station', required=True)
