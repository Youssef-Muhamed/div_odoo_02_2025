from odoo import models, fields, api

class DivTrack(models.Model):
    _name = 'div.track'
    _description = 'Track'

    name = fields.Char(string="Track Name")
    type = fields.Selection(
        selection=[('backend', 'Backend'), ('frontend', 'Frontend'), ('fullstack', 'Fullstack')],
    )

    student_ids = fields.One2many('div.students','track_id', string="Students")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name must be unique'),
        # ('type_unique', 'check(salary > 0)', 'Type must be unique'),
    ]