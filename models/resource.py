# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class resource(models.Model):
    _name = 'appsy.resource'
    
    dateAdded = fields.Date()
    link = fields.Char()
    tittle = fields.Chart()
    psychologist = fields.Many2one('appsy.psychologist', string="Psychologist")
    clientResourceIds = fields.One2many('appsy.clientResource','resource', string="Resources")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
