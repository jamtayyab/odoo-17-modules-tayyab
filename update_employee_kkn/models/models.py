# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = "hr.employee"

    station_id = fields.Many2one("res.station", string="Station", required=True)
    unique_id = fields.Char(
        string="unique_id",
        default=lambda self: _("New"),
        readonly=True,
        required=True,
        tracking=True,
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
                if employee.work_contact_id:
                    employee.unique_id = employee.work_contact_id.unique_id

            else:
                employee.work_contact_id.sudo().write(
                    {
                        "email": employee.work_email,
                        "mobile": employee.mobile_phone,
                        "phone": employee.work_phone,
                        "station_id": employee.station_id.id,
                    }
                )
