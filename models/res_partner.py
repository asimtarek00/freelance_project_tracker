
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    
    is_freelancer = fields.Boolean(string="Is Freelancer", default=False)
    freelance_project_ids = fields.One2many(
        'freelance.project', 
        'client_id', 
        string="Freelance Projects"
    )