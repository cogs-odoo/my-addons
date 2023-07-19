from odoo import fields, models

class Registry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle registry"
    _rec_name = "registry_number"

    registry_number = fields.Char(string="Registry number", required=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image()
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate Number")
    certificate_title = fields.Binary(string="Certificate Title")
    register_date = fields.Date(string="Registration Date")