# -*- coding: utf-8 -*-
from odoo import http

# class CustomContacts(http.Controller):
#     @http.route('/custom_contacts/custom_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_contacts/custom_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_contacts.listing', {
#             'root': '/custom_contacts/custom_contacts',
#             'objects': http.request.env['custom_contacts.custom_contacts'].search([]),
#         })

#     @http.route('/custom_contacts/custom_contacts/objects/<model("custom_contacts.custom_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_contacts.object', {
#             'object': obj
#         })