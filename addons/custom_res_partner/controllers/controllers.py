# -*- coding: utf-8 -*-
from odoo import http

# class CustomResPartner(http.Controller):
#     @http.route('/custom_res_partner/custom_res_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_res_partner/custom_res_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_res_partner.listing', {
#             'root': '/custom_res_partner/custom_res_partner',
#             'objects': http.request.env['custom_res_partner.custom_res_partner'].search([]),
#         })

#     @http.route('/custom_res_partner/custom_res_partner/objects/<model("custom_res_partner.custom_res_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_res_partner.object', {
#             'object': obj
#         })