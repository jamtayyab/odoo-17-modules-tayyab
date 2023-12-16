# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResDistrict(models.Model):
    _inherit = "res.bank"

    # Address Data
    station_id = fields.Many2one("res.station", "Station", )
    zip = fields.Char(related="station_id.zip", change_default=True, store=True, string = "zip")
    district_id = fields.Many2one(related="station_id.district_id", store=True)
    state_id = fields.Many2one(related="station_id.state_id", store=True, string='Province')
    country_id = fields.Many2one(related="station_id.state_id.country_id", store=True,string='Country')


    @api.constrains('phone')
    def phone_validation(self):
        # Improved Validation
        for record in self:
            if not re.match('^((\+923)?(923)?(03)?)([0-9]{9})$',str(record.phone)):
                raise ValidationError(
                    _("Number Format is not correct. Accepted formats are :\n +923001234567 or 923001234567 or 03001234567")
                )

            # if record.phone and len(record.phone) != 12:
            #     # _logger.error("%s  ", record.phone)
            #     raise ValidationError(
            #         _("Please enter correct Mobile number. It should be 12 characters.")
            #     )