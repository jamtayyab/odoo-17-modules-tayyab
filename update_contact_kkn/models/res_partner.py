# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)
ADDRESS_FIELDS = ("street", "street2", "zip", "city", "state_id", "country_id")


class ResPartner(models.Model):
    _inherit = "res.partner"

    company_type = fields.Selection(
        string="Company Type",
        selection=[("person", "Individual"), ("company", "Company")],
        compute="_compute_company_type",
        inverse="_write_company_type",
        store=True,
    )
    contact_type = fields.Selection(
        [
            ("customer", "Customer"),
            ("vendor", "Vendor"),
            ("employee", "Employee"),
            ("installation_poc", "Installation POC"),
            ("billing_poc", "Billing POC"),
            ("portal", "Portal User"),
            ("other", "Other"),
        ],
        string="Contact Type",
        default="vendor",
        required=True,
        tracking=True,
    )
    # contact_sub_type = fields.Selection(
    #     [
    #         ("residential", "Residential"),
    #         ("small_business", "Small Business"),
    #         ("corporate", "Corporate"),
    #         ("carriers_operators", "Carriers/Operators"),
    #     ],
    #     string="Contact Sub Type",
    #     default=False,
    #     tracking=True,
    # )

    # customer_subscription_model = fields.Selection(
    #     [("pre_paid", "Pre Paid"), ("post_paid", "Post Paid")],
    #     string="Subscription Model",
    #     default="pre_paid",
    #     tracking=True,
    # )

    unique_id = fields.Char(
        string="Unique Id",
        default=lambda self: _("New"),
        readonly=True,
        required=True,
        tracking=True,
    )

    pta_registered = fields.Selection(
        [("registered", "Registered"), ("unregistered", "Unregistered")],
        string="PTA Registered",
        default="unregistered",
        tracking=True,
    )

    gstn = fields.Char(string="GSTN", tracking=True)
    tax_status = fields.Selection(
        [("registered", "Registered"), ("unregistered", "Unregistered")],
        string="Tax Status",
        default="unregistered",
        tracking=True,
    )
    cnic = fields.Char(string="CNIC")
    station_id = fields.Many2one("res.station", "Station", tracking=True)
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

    start_date = fields.Date(string="Starting Date", default=fields.Date.context_today)
    active_status = fields.Boolean(string="Active Status", default=True)

    # @api.onchange("station_id")
    # def _onchange_district(self):
    #     self.district_id = self.station_id.district_id
    # for address type contact
    @api.constrains("cnic", "mobile", "vat")
    def _check_fields_length(self):
        for record in self:
            if record.cnic and len(record.cnic) != 15:
                _logger.error("%s  ", record.cnic)
                raise ValidationError(
                    _("Please enter correct CNIC number. It should be 15 characters.")
                )
            if record.mobile and len(record.mobile) != 12:
                _logger.error("%s  ", record.mobile)
                raise ValidationError(
                    _("Please enter correct Mobile number. It should be 12 characters.")
                )
            if record.vat and len(record.vat) != 9:
                _logger.error("%s  ", record.vat)
                raise ValidationError(
                    _(
                        "Please enter correct NTN/PSTN number. It should be 9 characters."
                    )
                )

    # default get method to get default values
    # @api.model
    # def default_get(self, fields_list):
    #     defaults = super().default_get(fields_list)
    #     print(defaults)
    #     # if defaults.get("contact_type"):
    #     #     self.contact_type = defaults.get("contact_type")
    #     return defaults

    # method override
    @api.onchange("mobile", "country_id", "company_id")
    def _onchange_mobile_validation(self):
        pass

    @api.onchange("type")
    def address_type(self):
        # print(self.env.context)
        address_dict = {
            "contact": self.env.context.get("default_contact_type") or "other",
            "invoice": "billing_poc",
            "delivery": "installation_poc",
            "followup": "other",
            "other": "other",
        }
        if address_dict.get(self.type):
            self.contact_type = address_dict.get(self.type)

    @api.onchange("cnic")
    def _onchange_cnic(self):
        if self.cnic:
            search_cnic = self.env["res.partner"].search_count(
                [("cnic", "=", self.cnic), ("id", "not in", self.ids)]
            )
            if search_cnic > 0:
                raise ValidationError(_("CNIC No Already Exist"))

    @api.onchange("vat")
    def _onchange_vat(self):
        if self.vat:
            search_vat = self.env["res.partner"].search_count(
                [("vat", "=", self.vat), ("id", "not in", self.ids)]
            )
            if search_vat > 0:
                raise ValidationError(_("NTN Number Already Exist"))

    @api.onchange("tax_status")
    def onchange_tax_status(self):
        if self.tax_status == "unregistered":
            self.pta_registered = False

    # @api.onchange("contact_type")
    # def onchange_contact_type(self):
    #     if self.contact_type and self.contact_type != "customer":
    #         self.customer_subscription_model = False
    #         self.contact_sub_type = False

    @api.model_create_multi
    def create(self, vals_list):
        _logger.error("%s", self.env.context)
        for vals in vals_list:
            if vals.get("unique_id", _("New")) == _("New"):
                id_type = vals.get("company_type")
                contact_type = vals.get("contact_type")
                # contact_sub_type = vals.get("contact_sub_type", False)
                # _logger.error(
                #     "%s      %s        %s  ", id_type, contact_type, contact_sub_type
                # )
                # vals["unique_id"] = self._generate_unique_id(
                #     id_type, contact_type, contact_sub_type
                # )
                vals["unique_id"] = self._generate_unique_id(id_type, contact_type)

        return super(ResPartner, self).create(vals_list)

    def _generate_unique_id(self, id_type, contact_type):
        unique_id_sequence_mapping = {
            ("person", "customer"): "res.partner.customer",
            ("person", "vendor"): "res.partner.vendor",
            ("person", "employee"): "res.partner.employee",
            ("person", "other"): "res.partner.other",
            ("person", "installation_poc"): "res.partner.installation.poc",
            ("person", "billing_poc"): "res.partner.billing.poc",
            ("person", "portal"): "res.partner.portal.user",
            ("company", "customer"): "res.partner.comp.customer",
            ("company", "vendor"): "res.partner.comp.vendor",
            ("company", "employee"): "res.partner.comp.employee",
            ("company", "other"): "res.partner.other",
            ("company", "installation_poc"): "res.partner.comp.installation.poc",
            ("company", "billing_poc"): "res.partner.comp.billing.poc",
            ("company", "portal"): "res.partner.comp.portal.user",
            ("company"): "res.partner.company",
        }

        if sequence := unique_id_sequence_mapping.get((id_type, contact_type)):
            unique_id = self.env["ir.sequence"].next_by_code(sequence)
            # logger for debugging

            # _logger.error(
            #     "%s   %s     %s  %s  ",
            #     contact_type,
            #     contact_sub_type,
            #     sequence,
            #     unique_id,
            # )
            return unique_id or _("New")
        return "N/A"

    @api.model
    def write(self, vals):
        if any(
            field in vals
            for field in ["company_type", "contact_type", "contact_sub_type"]
        ):
            id_type = vals.get("company_type", self.company_type)
            contact_type = vals.get("contact_type", self.contact_type)
            # contact_sub_type = vals.get("contact_sub_type", self.contact_sub_type)

            # logger for debugging

            # _logger.error(
            #     "%s   %s     %s  ", contact_type, contact_sub_type, id_type
            # )

            # if contact_type != "customer":
            #     vals["contact_sub_type"] = ""
            #     contact_sub_type = False

            vals["unique_id"] = self._generate_unique_id(id_type, contact_type)
        return super().write(vals)
