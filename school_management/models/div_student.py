from reportlab.graphics.transform import inverse

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class DivStudent(models.Model):
    _name = 'div.students'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(required=True,tracking=True)
    email = fields.Char(string="Student Email",copy=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male')
    # default = fields.Datetime.now  --> to get current date
    date_of_birth = fields.Datetime()
    age = fields.Integer()
    salary = fields.Float()
    tax = fields.Float()
    net_salary = fields.Float(compute='_compute_net_salary', store=True, )
    # company_id = fields.Many2one('res.company', default=lambda self: self.env.company)

    # new_salary = fields.Float(compute='_compute_new_salary',store=True)
    @api.depends('salary', 'tax')
    def _compute_net_salary(self):
        """ compute net salary """
        # print('-------------->',self)
        # self.net_salary = self.salary * self.tax
        for rec in self:
            rec.net_salary = rec.salary - (rec.salary * rec.tax)

    # @api.depends('net_salary','salary','tax')
    # def _compute_new_salary(self):
    #     for rec in self:
    #         rec.new_salary = rec.net_salary / 2

    graduated = fields.Boolean()
    description = fields.Text()
    content = fields.Html()
    skills_ids = fields.Many2many('div.skills')
    track_id = fields.Many2one('div.track', domain=[('type', '=', 'backend')],tracking=True)

    state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'), ('accepted', 'Accepted'), ('cancelled', 'Cancelled') ],
        default='draft')
    _sql_constraints = [
        ('name_student_unique', 'unique(name)', 'Name must be unique'),
        # ('type_unique', 'check(salary > 0)', 'Type must be unique'),
    ]
    @api.constrains('email')
    def _check_email(self):
        if self.email:
            if '@' not in self.email:
                raise ValidationError(_(f'Email {self.email} should be valid '))
    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        if self.date_of_birth:
            # self.age = (datetime.now().year - self.date_of_birth.year)
            self.age = (fields.Date.today().year - self.date_of_birth.year)

    def action_set_draft(self):
        self.state = 'draft'

    def action_set_in_progress(self):
        self.state = 'in_progress'

    def action_set_accepted(self):
        if self.age < 18:
            raise ValidationError(_('Age should be greater than 18'))
        self.state = 'accepted'

    def action_set_canceled(self):
        self.state = 'cancelled'


    @api.model
    def create(self, vals):
        # print('--------> vals',vals)
        # if 'email' in vals:
        #     print('--------> outside if')
        #     if '@' not in vals['email']:
        #         print('--------> inside if')
        #         vals['email'] = vals['email'] + '@gmail.com'
        res = super(DivStudent, self).create(vals)
        # if res.email:
        #     if '@' not in res.email:
        #         res.email = res.email + '@gmail.com'

        return res

    def write(self, vals):
        print('--------> vals',vals)
        res = super(DivStudent, self).write(vals)
        return res
    def unlink(self):
        print('--------> vals',self)
        res = super(DivStudent, self).unlink()
        return res
    def copy(self, default=None):
        print('--------> vals',self)
        res = super(DivStudent, self).copy(default)
        return res

    def _server_action_set_draft(self):
        for rec in self:
            rec.action_set_draft()


    def _cron_set_tax(self):
        print('--------> _cron_set_tax')
        for rec in self:
            rec.tax = 0.10

    def action_create_track(self):
        # action = self.env.ref('school_management.create_track_wizard_act_window').read()[0]
        # action['context'] = {
        #     'default_track_name': 'New Track',
        #     'default_track_type': 'backend',
        # }
        # print(action)
        #
        # return action

        action = {
            'type': 'ir.actions.act_window',
            'name': 'Create Track',
            'view_mode': 'form',
            'res_model': 'create.track.wizard',
            'target': 'new',
        }
        return action

    # def action_create_skills(self):
    #     action = {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Create Skills',
    #         'view_mode': 'form',
    #         'res_model': 'div.skills',
    #         'target': 'new',
    #     }
    #     return action
# Inheritance
#1 python inheritance
#2 class inheritance
#3 view inheritance

# security levels
# 1. model level
# 2 record level
# 3 field level

# models
# 1. odoo models
# 2. Transient models
# 3. Abstract models