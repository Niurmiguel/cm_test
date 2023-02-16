# -*- coding: utf-8 -*-

from odoo import models

class custom_contacts(models.Model):
    _inherit = 'res.partner'

    def add_prospect_tag(self):
        category_id = self.env['res.partner.category'].search([['name', '=', 'Prospects'], ['active', '=', True]], limit=1).id

        for record in self:
            record.category_id = [category_id]