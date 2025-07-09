from odoo import http
from odoo.http import request,Response
import json
import werkzeug.wrappers

class Student(http.Controller):

    @http.route('/api/students',methods=['GET'], type='json', auth='none', csrf=False)
    def get_students(self, **kwargs):
        students = request.env['div.students'].sudo().search([])
        data = []
        for student in students:
            data.append({
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'gender': student.gender,
                'date_of_birth': student.date_of_birth,
                'track_id': student.track_id.name
            })

        return {'status': 'success','total': len(data),'data': data }

    @http.route('/api/students/<int:student_id>',methods=['GET'], type='json', auth='none', csrf=False)
    def get_student(self, student_id, **kwargs):
        payload = json.loads(request.httprequest.data.decode('utf-8'))
        if payload.get('name',False):
            student = request.env['div.students'].sudo().search([('name', 'ilike', payload.get('name'))])
            print(student)
        student = request.env['div.students'].sudo().search([('id', '=', student_id)])
        if not student:
            return {'status': 'error','message': 'Student not found' }
        data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'gender': student.gender,
            'date_of_birth': student.date_of_birth,
            'track_id': student.track_id.name
        }
        return {'status': 'success','data': data }


    @http.route('/api/students',methods=['POST'], type='json', auth='none', csrf=False)
    def create_student(self, **kwargs):
        payload = json.loads(request.httprequest.data.decode('utf-8'))
        if not payload.get('name',False):
            return {'status': 'error','message': 'Name is required' }
        if not payload.get('email',False):
            return {'status': 'error','message': 'Email is required' }

        student = request.env['div.students'].sudo().create(payload)
        return {'status': 'success','data': {'id': student.id,'name': student.name,'email': student.email,'gender': student.gender,'date_of_birth': student.date_of_birth,'track_id': student.track_id.name} }



    @http.route('/api/students/<int:student_id>',methods=['PUT'], type='json', auth='none', csrf=False)
    def update_student(self, student_id, **kwargs):
        payload = json.loads(request.httprequest.data.decode('utf-8'))
        student = request.env['div.students'].sudo().search([('id', '=', student_id)])
        if not student:
            return {'status': 'error','message': 'Student not found' }
        student.write(payload)
        return {'status': 'success','message':"Student updated successfully" }


    @http.route('/api/students/<int:student_id>',methods=['DELETE'], type='json', auth='none', csrf=False)
    def delete_student(self, student_id, **kwargs):
        student = request.env['div.students'].sudo().search([('id', '=', student_id)])
        if not student:
            return {'status': 'error','message': 'Student not found' }
        student.unlink()
        return {'status': 'success','message':"Student deleted successfully" }