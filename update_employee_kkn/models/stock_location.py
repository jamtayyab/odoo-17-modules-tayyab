from odoo import api, fields, models

class StockLocation(models.Model):
    _inherit = "stock.location"
    employee_id = fields.Many2one("hr.employee")
