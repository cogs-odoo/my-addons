{
    'name': 'Odoo Academy',
    'summary': """Module to handle Course and Sessions""",
    'description': """Module to handle:
        - Courses
        - Sessions
        - Attendees
    """,
    'license': 'OPL-1',
    'author': 'cogs',
    'website': 'www.odoo.com',
    'category': 'Custom Modules/Technical Training',
    'depends': ['base'],
    'data': ['security/academy_groups.xml', 
             'security/ir.model.access.csv', 
             'security/academy_security.xml',
             'views/academy_menuitems.xml',
             'views/course_views.xml'],
    'demo': ['demo/course_demo.xml'],
    'application': True,
}