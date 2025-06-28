from odoo import models, fields, api
from  odoo.exceptions import UserError,ValidationError
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    student_id = fields.Many2one('div.students', string='Student')

    def action_confirm(self):
        if not self.student_id:
            raise ValidationError("Please select a student")
        return super(SaleOrder, self).action_confirm()

    def _prepare_confirmation_values(self):
        res = super(SaleOrder, self)._prepare_confirmation_values()
        del res['date_order']
        return res