

from odoo import models, fields, api
from odoo.exceptions import UserError

class FreelanceProject(models.Model):
    _name = 'freelance.project'
    _description = 'Freelance Marketplace Model'

    name = fields.Char(string="Project Title", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price")
    
    state = fields.Selection([
        ('open', 'Open'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='open', string="Status")

    
    client_id = fields.Many2one("res.partner", string="Client")
    freelancer_id = fields.Many2one("res.users", string="Freelancer")
    category_id = fields.Many2one("project.category", string="Category")
    alternative_phone = fields.Char(string="Alternative Phone")
    
    def claim_project(self):
        self.ensure_one()
        for record in self:
            if record.state == "completed":
                raise UserError("This project is already complete")
            else:
                record.state = "progress"

    def complete_project(self):
        self.ensure_one()
        for record in self:
            if record.state == "completed":
                raise UserError("This project is already completed")
            record.state = "completed"