from odoo import fields, models


class HrHospitalPatientVisit(models.Model):
    _name = "hr.hospital.patient.visit"
    _description = "Patient Visit"

    name = fields.Char(required=True)
    patient_id = fields.Many2one(
        comodel_name="hr.hospital.patient",
        string="Patient",
    )
    doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Doctor",
    )
    visit_datetime = fields.Datetime(string="Visit Date and Time")