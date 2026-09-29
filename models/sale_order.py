from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    alternative_phone = fields.Char(string="Alternative Phone")
    
    customer_mobile = fields.Char(
        string="Customer Mobile", 
        compute="_compute_customer_mobile", 
        store=True
    )

    customer_importance = fields.Selection(
        selection=[
            ('high', 'High Priority'),
            ('medium', 'Medium Priority'),
            ('low', 'Low Priority'),
        ],
        string="Customer Importance",
        compute="_compute_customer_importance",
        store=True
    )

    @api.depends('partner_id', 'partner_id.mobile')
    def _compute_customer_mobile(self):
        for record in self:
            if record.partner_id and record.partner_id.mobile:
                record.customer_mobile = record.partner_id.mobile
            else:
                record.customer_mobile = False

    @api.depends('partner_id', 'partner_id.phone', 'partner_id.mobile')
    def _compute_customer_importance(self):
        for record in self:
            partner = record.partner_id
            if partner:
                if partner.mobile and partner.phone:
                    record.customer_importance = 'high'
                elif partner.mobile or partner.phone:
                    record.customer_importance = 'medium'
                else:
                    record.customer_importance = 'low'
            else:
                record.customer_importance = 'low'