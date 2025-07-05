from odoo import models, fields, api
class CreateTrackWizard(models.TransientModel):
    _name = 'create.track.wizard'

    track_name = fields.Char()
    track_type = fields.Selection([('backend', 'Backend'), ('frontend', 'Frontend'), ('fullstack', 'Fullstack')])

    # def _prepare_track_values(self):
    #     vals = {
    #         'name': self.track_name,
    #         'type': self.track_type,
    #     }
    #     return vals

    # orm reference
    # https: // www.cybrosys.com / blog / what - are - orm - methods - in -odoo - 18
    def create_track(self):
        # vals = self._prepare_track_values()
        print('--------> vals',self.env.context)
        # student_obj = self.env['div.students'].search([]).filtered(lambda s: s.id == self.env.context['active_id'])
        student_obj = self.env['div.students'].search_count([('name', 'ilike', 'test')])
        # student_obj = self.env['div.students'].browse(self.env.context['active_ids'])
        # student_obj = self.env['div.students'].search([]).mapped('name')
        print('--------> student_obj',student_obj)

        # used to unlink just for test
        # student_obj = self.env['div.students'].browse(27)
        # print('--------> student_obj',student_obj)
        # print('--------> student_obj',student_obj.read())
        # student_obj.unlink()
        # student_obj.write({'name': student_obj.name + ' ' + self.track_name})
        # vals = {
        #     'name': self.track_name,
        #     'type': self.track_type,
        # }
        # created_track = self.env['div.track'].create(vals)
        # student_obj.write({'track_id': created_track.id})
        return True
