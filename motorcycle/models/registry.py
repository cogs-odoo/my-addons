from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle registry"
    _rec_name = "registry_number"

    active = fields.Boolean(default=True)

    registry_number = fields.Char(string="Registry number", default="MRN0000", 
                                  copy=False, required=True, readonly=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image()
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate Number")
    certificate_title = fields.Binary(string="Certificate Title")
    register_date = fields.Date(string="Registration Date")

    _sql_constraints = [('unique_vin', 'UNIQUE (vin)', 'This VIN already exists!')]

    owner_id = fields.Many2one(comodel_name="res.partner", string='Owner')
    email = fields.Char(related="owner_id.email")
    phone = fields.Char(related="owner_id.phone")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:  
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
            return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin_pattern(self):
        for registry in self:
            regex = r'^[A-Z]{4}[0-9]{2}[A-Z0-9]{2}[0-9]{6}$'
            if (re.match(regex, registry.vin) == None):
                raise ValidationError('The VIN must match the pattern')

    @api.constrains('license_plate')
    def _check_license_plate_pattern(self):
        for registry in self:
            regex = r'^([A-Z]{1,4})([0-9]{1,3})([A-Z]{2})?$'
            if (re.match(regex, registry.license_plate) == None):
                raise ValidationError('The License Plate must match the pattern')