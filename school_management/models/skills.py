from odoo import models, fields, api

class DivSkills(models.Model):
    _name = 'div.skills'

    name = fields.Char()
    description = fields.Text()

