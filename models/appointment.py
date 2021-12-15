# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class appointment(models.Model):
    _name = 'appsy.appointment'

    date = fields.Date()
    diagnose = fields.Char()
    numAppointment = fields.Integer()
    price = fields.Float()
    client = fields.Many2one('appsy.client',string="Clients")
    psychologist = fields.Many2one('appsy.psychologist', string="Psychologist")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
