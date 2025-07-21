from odoo import models, fields, api
import base64
import csv
from io import StringIO


class EmployeeImportWizard(models.TransientModel):
    _name = 'chao_quan.employee.import.wizard'
    _description = 'Employee Import Wizard'

    data_file = fields.Binary(string='CSV File', required=True)
    filename = fields.Char(string='Filename')

    def action_import(self):
        self.ensure_one()
        if not self.data_file:
            return
        file_content = base64.b64decode(self.data_file)
        csv_data = file_content.decode('utf-8')
        reader = csv.DictReader(StringIO(csv_data))
        employees = []
        for row in reader:
            vals = {
                'name': row.get('name'),
                'work_phone': row.get('work_phone'),
                'work_email': row.get('work_email'),
                'job_title': row.get('job_title'),
            }
            employees.append(vals)
        for vals in employees:
            self.env['hr.employee'].create(vals)
