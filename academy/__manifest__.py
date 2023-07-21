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
    'depends': ['sale'],
    'data': ['security/academy_groups.xml', 
             'security/ir.model.access.csv', 
             'security/academy_security.xml',
             'data/session_data.xml',
             'views/academy_menuitems.xml',
             'views/course_views.xml',
             'views/session_views.xml',
             'views/sale_view_inherit.xml'],
    'demo': ['demo/course_demo.xml'],
    'application': True,
}