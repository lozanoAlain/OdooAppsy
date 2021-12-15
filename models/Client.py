# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
    _name = 'appsy.client'
    _inherit = 'res.user'

    dateStart = fields.Date()
    appointmentIds = fields.One2Many('appsy.appointment','client',String = 'Appoinstments')
    clientResourceIds = fields.One2Many('appsy.clientResource','client',String = 'Resources')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100