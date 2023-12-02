# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class Employee(models.Model):
    _inherit = "hr.employee"

    station_id = fields.Many2one(
        "res.station",
        string="Station",
        required=True,
        inverse="_inverse_work_contact_details",
    )
    unique_id = fields.Char(
        string="Unique ID",
        related="work_contact_id.unique_id",
        readonly=True,
        tracking=True,
        store=True,
    )

    @api.constrains("mobile_phone")
    def _check_fields_length(self):
        for record in self:
            if record.mobile_phone and len(record.mobile_phone) != 12:
                # _logger.error("%s  ", record.mobile)
                raise ValidationError(
                    _("Please enter correct Mobile number. It should be 12 characters.")
                )

    # overrides the inverse function for res.partner data creation
    def _inverse_work_contact_details(self):
        for employee in self:
            if not employee.work_contact_id:
                employee.work_contact_id = (
                    self.env["res.partner"]
                    .sudo()
                    .create(
                        {
                            "email": employee.work_email,
                            "mobile": employee.mobile_phone,
                            "name": employee.name,
                            "image_1920": employee.image_1920,
                            "company_id": employee.company_id.id,
                            "contact_type": "employee",
                            "company_type": "person",
                            "station_id": employee.station_id.id,
                            "phone": employee.work_phone,
                        }
                    )
                )
                # if partner created now create location for it for inventory purpose
                if employee.work_contact_id and employee.unique_id:
                    location_id = self.env["stock.location"].search(
                        [
                            ("name", "=", "Employee"),
                            ("unique_id", "not in", [_("New"), "N/A"]),
                        ],
                        limit=1,
                    )
                    location_vals = {
                        "name": f"{employee.unique_id}-{employee.name}",
                        "usage": "employee",
                        "location_id": location_id.id,
                        "station_id": employee.station_id.id,
                        "street": employee.work_contact_id.street,
                    }
                    location_id = (
                        self.env["stock.location"].sudo().create(location_vals)
                    )
                    if location_id:
                        employee.work_contact_id.property_stock_customer = location_id

                    _logger.info("Location Created: %s", location_id)

            else:
                _logger.info(
                    "changed: %s",
                    {
                        "email": employee.work_email,
                        "mobile": employee.mobile_phone,
                        "phone": employee.work_phone,
                        "station_id": employee.station_id.id,
                    },
                )
                employee.work_contact_id.sudo().write(
                    {
                        "email": employee.work_email,
                        "mobile": employee.mobile_phone,
                        "phone": employee.work_phone,
                        "station_id": employee.station_id.id,
                    }
                )
