# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class clientResource(models.Model):
    _name = 'appsy.clientResource'

    typeDiagnose = fields.Char()
    client = fields.Many2one('appsy.client', string ="Client")
    resource = fields.Many2one('appsy.resource', string="Resource")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
