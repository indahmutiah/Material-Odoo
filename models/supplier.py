from odoo import models, fields

class Supplier(models.Model):
    _name= 'materials.supplier'
    _description= 'Suppliers Data'
    _rec_name = 'name' 

    name =  fields.Char (string= "Name")

