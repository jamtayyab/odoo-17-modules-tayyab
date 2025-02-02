# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class UpdateLocationForm(models.Model):
    _name = "stock.location"
    _inherit = ["stock.location", "mail.thread", "mail.activity.mixin"]
    name = fields.Char("Location Name", required=True, tracking=True)
    complete_name = fields.Char(
        "Full Location Name",
        compute="_compute_complete_name",
        store=True,
        tracking=True,
    )
    location_id = fields.Many2one(
        "stock.location",
        "Parent Location",
        index=True,
        ondelete="cascade",
        check_company=True,
        help="The parent location that includes this location. Example : The 'Dispatch Zone' is the 'Gate 1' parent "
        "location.",
        tracking=True,
    )
    # Unique ID for location form
    unique_id = fields.Char(
        string="Unique ID",
        tracking=True,
        required=True,
        readonly=True,
        default=lambda self: _("New"),
    )
    is_pop = fields.Boolean("Is POP?")

    # New Type in usage Pop
    usage = fields.Selection(
        selection_add=[
            ("supplier", "Vendor Location"),
            ("view", "View"),
            ("internal", "Internal Location"),
            ("customer", "Customer Location"),
            ("employee", "Employee Location"),
            ("pop", "POP"),
            ("exchange", "Exchange"),
            ("storeconsumed", "Store Consumed"),
            ("inventory", "Inventory Loss"),
            ("production", "Production"),
            ("costcenter", "Cost Center"),
            ("transit", "Transit Location"),
        ],
        string="Location Type",
        default="internal",
        index=True,
        required=True,
        help="* Vendor Location: Virtual location representing the source location for products coming from your vendors"
        "\n* View: Virtual location used to create a hierarchical structures for your warehouse, aggregating its child locations ; can't directly contain products"
        "\n* Internal Location: Physical locations inside your own warehouses,"
        "\n* Customer Location: Virtual location representing the destination location for products sent to your customers"
        "\n* Inventory Loss: Virtual location serving as counterpart for inventory operations used to correct stock levels (Physical inventories)"
        "\n* Production: Virtual counterpart location for production operations: this location consumes the components and produces finished products"
        "\n* Transit Location: Counterpart location that should be used in inter-company or inter-warehouses operations",
        tracking=True,
        ondelete={
            "supplier": "set default",
            "view": "set default",
            "internal": "set default",
            "employee": "set default",
            "customer": "set default",
            "pop": "set default",
            "exchange": "set default",
            "storeconsumed": "set default",
            "inventory": "set default",
            "production": "set default",
            "costcenter": "set default",
            "transit": "set default",
        },
    )
    partner_latitude = fields.Float("Geo Latitude", digits=(16, 6), tracking=True)
    partner_longitude = fields.Float("Geo Longitude", digits=(16, 6), tracking=True)
    date_localization = fields.Date(string="Geolocation Date", tracking=True)

    def _generate_id(self, city_id):
        unique_code = self.env["ir.sequence"].next_by_code(
            "stock.location.sequenece"
        ) or _("New")
        station = self.env["res.station"].browse(city_id)

        if unique_code == _("New") or not station:
            return unique_code
        code = f"{station.district_id.code}-{unique_code}"
        return code

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # _logger.error("%s      ", vals_list)
            if vals.get("unique_id", _("New")) == _("New"):
                vals["unique_id"] = self._generate_id(vals["station_id"])
                # _logger.error("%s      %s   ", vals["unique_id"], self)

        return super().create(vals_list)

    # def write(self, vals):
    #     if "city_id" in vals:
    #         vals["unique_id"] = self.generat_id(vals["city_id"])
    #         _logger.error("%s ", vals["city_id"])

    #     return super().write(vals)

    # Find Location of given Data
    @api.model
    def _geo_localize(self, street="", zip="", city="", state="", country=""):
        geo_obj = self.env["base.geocoder"]
        search = geo_obj.geo_query_address(
            street=street, zip=zip, city=city, state=state, country=country
        )
        result = geo_obj.geo_find(search, force_country=country)
        if result is None:
            search = geo_obj.geo_query_address(city=city, state=state, country=country)
            result = geo_obj.geo_find(search, force_country=country)
        return result

    # Get address along city, state adn country and write latitude, longitude
    def geo_localize_location(self):
        # We need country names in English below
        for partner in self.with_context(lang="en_US"):
            if result := self._geo_localize(
                partner.street,
                partner.zip_id,
                partner.city_id.name,
                partner.state_id.name,
                partner.country_id.name,
            ):
                partner.write(
                    {
                        "partner_latitude": result[0],
                        "partner_longitude": result[1],
                        "date_localization": fields.Date.context_today(partner),
                    }
                )
        return True
