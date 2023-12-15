# -*- coding: utf-8 -*-

from odoo import models, fields, api


class update_crm_kkn(models.Model):
    _inherit= 'crm.lead'

#your core values.
# and your value as wel
# make a video of 5 min

#// your personal values at least 3

# //Development
# //Service Quality
# //Reliability
# //Customer care and support
# //Integrity  --- Inovation

##_________________________
# Core values on your desk All
# Customer Care & Support
# Innovation
# Reliability

    def action_survey(self):
        if self.crm_stage.stage_id.name == 'Opportunity':
            print("i was hit ")

