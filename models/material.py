from odoo import models, fields,api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name= 'materials.material'
    _description= 'Material Registration'
    _rec_name = 'material_name'

    material_code = fields.Char (string= "Material Code")
    material_name = fields.Char (string= "Material Name")
    material_type = fields.Selection ([
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton'),
    ])
    material_buy_price = fields.Integer(string="Material Buy Price", required=True)
    supplier = fields.Many2one(string="Supplier", comodel_name="materials.supplier")

    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError('Buy price cannot be less than 100!! Check  Material Buy Price')
