# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class user(models.Model):
    _inherit = 'res.users'
    _name = 'appsy.users'
    user_status = fields.Selection([
        ('0', 'ACTIVE'),
        ('1', 'INACTIVE'),
        ])
    privilege = fields.Selection([
            ('0', 'ADMIN'),
            ('1', 'CLIENT'),
            ('2', 'PSYCHOLOGIST'),
        ])
    
    
