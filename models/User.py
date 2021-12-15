# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
     _name = 'res.user'
     _inherit = 'res.user'

     privilege = fields.Selection(String = 'Privilege')
     status = fields.Selection(String = 'Status')
     resources = fields.One2Many('appsy.lastsignin','idUser',String = 'Users')