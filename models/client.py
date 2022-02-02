# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class client(models.Model):
    _name = 'appsy.client'
    _inherit = 'appsy.users'

    dateStart = fields.Date()
    appointment_id = fields.One2many('appsy.appointment', 'client_id', String='Appointments')
    clientResourceIds = fields.One2many('appsy.clientresource', 'clients_id', String='Resources')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100