# _*_ encoding: utf-8 _*_

from odoo import http

class Motorcycle(http.Controller):
    @http.route('/compare/', auth='public', website=True)

    def registry(self, **kw):
        registry = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle.registry_website', {
            'registries': registry,
        })