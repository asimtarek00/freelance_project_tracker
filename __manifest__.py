{
    'name': "Freelance Project Tracker",
    'summary': "Manage freelance projects and categories",
    'version': '15.0.1.0.0',
    'category': 'Services',
    'author': 'Asim_Developer',
    
    'depends': ['base', 'sale'],
    
    'application': True,
    'installable': True,
    'auto_install': False,

    'data': [
        'security/ir.model.access.csv',
        'views/freelance_project_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_view.xml'
    ],
}