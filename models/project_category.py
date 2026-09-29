from odoo import models, fields

class ProjectCategory(models.Model):
    _name = 'project.category'
    _description = 'Project Category'

    name = fields.Char(string="Category Name", required=True)