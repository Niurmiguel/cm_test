# -*- coding: utf-8 -*-

from odoo import models

class custom_stock(models.Model):
    _inherit = 'product.template'
    _description = 'Custom Stock'