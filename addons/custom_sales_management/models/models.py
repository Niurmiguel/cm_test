# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_sales_management(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Custom'

    sale_type = fields.Selection([
        ('recorded', 'Recorded'),
        ('signed', 'Signed')
    ], string="Type of sale")

    call_id = fields.Char(string="Call ID",
                          help='Registered caller ida')
