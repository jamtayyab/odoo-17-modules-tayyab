from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    employee_id = fields.Many2one("hr.employee")
