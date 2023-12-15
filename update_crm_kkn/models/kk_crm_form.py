# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UpdateCrmForm(models.Model):
    _inherit = "crm.lead"
    _rec_name = "sale_type"

    stage_name = fields.Char(
        related="stage_id.name", string="Stage Name", store=True, tracking=True
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency", string="currency", required=True
    )
    sale_type = fields.Many2one(
        comodel_name="kk.sale.type", string="Sale Type", required=True
    )
    branch_type = fields.Many2one(
        comodel_name="kk.branch.type", string="Branch Type", required=True
    )
    source = fields.Many2one(
        comodel_name="kk.lead.source", string="Branch", required=True
    )
    free_of_cost = fields.Selection(
        selection=[("YES", "YES"), ("NO", "NO")],
        string="FOC",
        help="Free Of Cost (FOC)",
        required=True,
    )
    redundant_link = fields.Selection(
        selection=[("YES", "YES"), ("NO", "NO")],
        string="Redundant Link",
        help="Backup link incase one link goes down",
        required=True,
    )
    product = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    cost = fields.Monetary(string="Cost", currency_field="currency_id")
    sale_price = fields.Monetary(string="Sale Price", currency_field="currency_id")
    expected_revenue_mrc = fields.Monetary(
        string="MRC", help="Expected Revenue (MRC)", currency_field="currency_id"
    )
    taxes = fields.Many2one(comodel_name="account.tax")
    one_time_cost_otc = fields.Monetary(
        string="OTC", help="One Time Cost (OTC)", currency_field="currency_id"
    )
    survey_person = fields.Many2one(comodel_name="hr.employee", string="Survey Person")
    sales_person = fields.Many2one(comodel_name="res.users", string="Sales Person")
    approx_won_date = fields.Date(
        string="Approx. Won Date",
        help="Till when you can make this lead to reach won stage",
    )
    lead_company = fields.Many2one(comodel_name="res.company", string="Lead Company")
    requested_medium = fields.Many2one(
        comodel_name="kk.requested.medium", string="Requested Medium"
    )
    approved_medium = fields.Many2one(
        comodel_name="kk.requested.medium", string="Approved Medium"
    )

    # Address Data
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

    @api.onchange("product")
    def fill_name(self):
        if self.product:
            self.name = self.product.name
            self.cost = self.product.standard_price
            self.sale_price = self.product.lst_price
