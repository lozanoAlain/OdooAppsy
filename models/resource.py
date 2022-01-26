# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class resource(models.Model):
    _name = 'appsy.resource'
    
    dateAdded = fields.Date()
    link = fields.Char()
    tittle = fields.Char()
    psychologist_id = fields.Many2one('appsy.psychologist', string="Psychologist")
    clientResourceIds = fields.One2many('appsy.clientresource', 'resource_id', string="Resources")
    
    @api.constrains('tittle')
    def _check_tittleNotNull(self):
        for record in self:
            if (not (record.tittle and record.tittle.strip())):
                raise ValidationError("The tittle cant be null")
    @api.constrains('link')
    def _check_linkNotNull(self):
        for record in self:
            if (not (record.link and record.link.strip())):
                raise ValidationError("The link cant be null")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
