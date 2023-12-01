# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessDenied


class StockLocation(models.Model):
    _inherit = "stock.location"

    street = fields.Char(tracking=True)
    station_id = fields.Many2one(
        "res.station",
        "Station",
        default=lambda self: self.env["res.station"].search([("name", "=", "Lahore")]),
        tracking=True,
    )
    zip = fields.Char(
        related="station_id.zip", change_default=True, store=True, tracking=True
    )
    district_id = fields.Many2one(
        related="station_id.district_id", store=True, tracking=True
    )
    state_id = fields.Many2one(related="station_id.state_id", store=True, tracking=True)
    country_id = fields.Many2one(
        related="station_id.state_id.country_id", store=True, tracking=True
    )
    city_code = fields.Char(
        related="station_id.district_id.code", tracking=True, readonly=True, store=True
    )
