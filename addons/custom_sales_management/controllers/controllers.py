# -*- coding: utf-8 -*-
from odoo import http

# class CustomSalesManagement(http.Controller):
#     @http.route('/custom_sales_management/custom_sales_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_management/custom_sales_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_management.listing', {
#             'root': '/custom_sales_management/custom_sales_management',
#             'objects': http.request.env['custom_sales_management.custom_sales_management'].search([]),
#         })

#     @http.route('/custom_sales_management/custom_sales_management/objects/<model("custom_sales_management.custom_sales_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_management.object', {
#             'object': obj
#         })