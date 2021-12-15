# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class psychologist(models.Model):
    _name = 'appsy.psychologist'
    _inherit = res.users
    
    office = fields.Char()
    specialization = fields.Char()
    resourceIds = fields.One2many('appsy.resource', 'psychologist', string="Resources")
    appointmentIds = fields.One2many('appsy.appointment', 'psychologist', string="Appointments")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100