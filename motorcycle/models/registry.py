from odoo import fields, models

class Registry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle registry"
    _rec_name = "registry_number"

    registry_number = fields.Char(string="Registry number", required=True)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()