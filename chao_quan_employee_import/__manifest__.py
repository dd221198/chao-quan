{
    'name': 'Chao Quan Employee Import',
    'version': '16.0.1.0.0',
    'summary': 'Import employees from CSV for Chao Quan restaurant',
    'author': 'Chao Quan',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_import_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
}
