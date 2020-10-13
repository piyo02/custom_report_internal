from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    canvas_price = fields.Float(string="Canvas Price", compute="get_canvas_price")

    @api.one
    def get_canvas_price(self):
        canvas_pricelist = self.env['product.pricelist'].search([('name', '=', 'Harga Kampas')])

        for line in canvas_pricelist.item_ids:
            product = self.env['product.template'].search([('name', '=', line.name)])
            product.update({
                'canvas_price' : line.fixed_price
            })
            