from odoo import fields, models


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(required=True)
    supervisor_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Supervising Doctor",
    )