from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        # if self.partner_id.employee:
        #     print(self.partner_id)
        res = super().button_validate()
        print("res", res)

        return res
