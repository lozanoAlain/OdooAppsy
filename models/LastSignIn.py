# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LastSignIn(models.Model):
   _name = 'appsy.lastSingIn'
   
   lastSignIn = fields.Datetime()
   idUser = fields.Many2One('res.user',String = 'User')
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100