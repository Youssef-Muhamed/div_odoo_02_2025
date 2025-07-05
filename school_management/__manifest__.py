{
    'name': 'School Management',
    'description': """
    this module is for school management and handle student and teacher
    """,
    'depends': ['base','mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_action_data.xml',
        'wizard/create_track_wizard_view.xml',

        'views/div_student_view.xml',
        'views/div_track_view.xml',
        'views/div_skills_view.xml',
        'views/sale_order_view.xml',
        'views/menus.xml',

    ],
    'license': 'OEEL-1',
    'application': True,
    'installable': True,
    'sequence': 1
}
