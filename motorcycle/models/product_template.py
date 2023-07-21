# _*_ coding: utf-8 _*_

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], 
                                     ondelete={'motorcycle': 'set product'})

    horse_power = fields.Float(string="Horse Power")
    top_speed = fields.Float(string="Top Speed")
    torque = fields.Float(string="Torque")
    battery_capacity = fields.Char(string="Battery Capacity")
    charge_time = fields.Float(string="Charge Time")
    m_range = fields.Float(string="Range")
    curb_weight = fields.Float(string="Curb Weight")
    make = fields.Char(string="Make")
    model = fields.Char(string="Model")
    year = fields.Integer(string="Year")
    launch_date = fields.Date(string="Launch Date")

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping