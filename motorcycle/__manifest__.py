{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license': 'OPL-1',
    'author': 'cogs-odoo',
    'website': 'https://github.com/cogs-odoo/technical-training',
    'category': 'Custom Modules/Kawiil',
    'depends': ['base'],
    'data': ['security/motorcycle_groups.xml', 
             'security/ir.model.access.csv', 
             'security/motorcycle_security.xml',
             'views/motorcycle_menuitems.xml'],
    'demo': ['demo/registry_demo.xml'],
    'application': True
}