# -*- coding: utf-8 -*-
from odoo import http

# class Appsy(http.Controller):
#     @http.route('/appsy/appsy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/appsy/appsy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('appsy.listing', {
#             'root': '/appsy/appsy',
#             'objects': http.request.env['appsy.appsy'].search([]),
#         })

#     @http.route('/appsy/appsy/objects/<model("appsy.appsy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('appsy.object', {
#             'object': obj
#         })