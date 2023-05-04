from odoo import http
from odoo.http import request

class Session(http.Controller):
    @http.route('/web/session/authenticate', type='json',auth='none')
    def authenticate(self, db, login,password, base_location=None):
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()

class MaterialController(http.Controller):
    @http.route('/materials/material', auth='user', methods=['GET'], type='json')
    def get_material(self):
        print("Yes data")
        materials_rec = request.env['materials.material'].search([])
        materials = []
        for rec in materials_rec:
            vals = {
                'id': rec.id,
                'name' : rec.material_name,
                'material_code' : rec.material_code,
                'material_type' : rec.material_type,
                'material_buy_price' : rec.material_buy_price,
                'supplier': rec.supplier
            } 
            materials.append(vals)
            print("material list>>", materials)
            data = {'status' : 200, 'response' : materials, 'message' : 'Success'}
        return data

        
    @http.route('/create_material', auth='user', methods=['POST'], type='json')
    def create_material(self, **rec):
        if request.jsonrequest:
            print("yes",rec)
            if rec['name']:
                vals = {
                    'material_name': rec['name'],
                    'material_code' : rec['material_code'],
                    'material_type' : rec['material_type'],
                    'material_buy_price' : rec['material_buy_price'],
                    'supplier' : rec['supplier']
                }
                new_material = request.env['materials.material'].sudo().create(vals)
                args = {'success': True,'message': 'Success','ID': new_material.id}
        return args

    @http.route('/update_material', auth='user', methods=['POST'], type='json')
    def update_material(self, **rec):
        if request.jsonrequest:
            print("yes",rec)
            if rec['id']:
                materials = request.env['materials.material'].sudo().search([('id','=',rec['id'])])
                if materials:
                    materials.sudo().write(rec)
                args = {'success': True,'message': 'Success'}
        return args
    
    @http.route('/delete_material', auth='user', methods=['POST'], type='json')
    def delete_material(self, **rec):
        if request.jsonrequest:
            print("yes",rec)
            if rec['id']:
                materials = request.env['materials.material'].search([('id','=',rec['id'])])
                if materials:
                    materials.unlink()
                args = {'success': True,'message': 'Success'}
        return args
    