# -*- coding: utf-8 -*-

from odoo import models, fields


class custom_res_partner(models.Model):
    _inherit = 'res.partner'
    _description = 'Contacts Custom'

    updated = fields.Boolean()
    diary = fields.One2many('res.partner.number', 'client', string='Diary')


class res_partner_number(models.Model):
    _name = 'res.partner.number'
    _description = 'Saving numbers of contacts'
    _rec_name = 'client'

    client = fields.Many2one(
        'res.partner', domain="[('customer','=', True)]", string='Client')
    save_number = fields.Char(string='Phone')
    is_active = fields.Boolean(string='Active')
    is_main = fields.Boolean(string='Main')
