# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class appointment(models.Model):
    _name = 'appsy.appointment'

    date = fields.Date()
    diagnose = fields.Char()
    numAppointment = fields.Integer()
    price = fields.Float()
    client_id = fields.Many2one('appsy.client', string="Clients")
    psychologist_id = fields.Many2one('appsy.psychologist', string="Psychologist")
    
    @api.constrains('price')
    def _check_something(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("The price cannot be negative")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
