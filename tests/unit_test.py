from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super().setUp()

        # Membuat data supplier untuk diuji
        self.supplier = self.env['supplier'].create({
            'name': 'PT Surya Cahaya Abadi',
        })

        # Membuat data material untuk diuji
        self.material = self.env['materials.material'].create({
            'material_code': 'MOX002951',
            'material_name': 'Vest Dylan',
            'material_type': 'Jeans',
            'material_buy_price': 100000,
            'supplier': self.supplier.id
        })

    def test_create_material(self):
        # Membuat data material baru
        new_material = self.env['materials.material'].create({
            'material_code': 'MOX002952',
            'material_name': 'Vest',
            'material_type': 'Jeans',
            'material_buy_price': 50000,
            'supplier': self.supplier.id
        })

        # Memastikan data material berhasil dibuat
        self.assertTrue(new_material)

    def test_read_material(self):
        # Membaca data material yang telah dibuat
        read_material = self.material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'supplier'])

        # Memastikan data material yang dibaca sesuai
        self.assertEqual(read_material[0]['material_code'], 'MOX002951')
        self.assertEqual(read_material[0]['material_name'], 'Vest Dylan')
        self.assertEqual(read_material[0]['material_type'], 'Jeans')
        self.assertEqual(read_material[0]['material_buy_price'], 100000)
        self.assertEqual(read_material[0]['supplier'][0], self.supplier.id)

    def test_update_material(self):
        # Memperbarui data material yang telah dibuat
        self.material.write({
            'material_code': 'MOX002951S',
            'material_name': 'Vest Dylan Limited Edition'
        })

        # Membaca data material yang telah diperbarui
        updated_material = self.material.read(['material_code', 'material_name'])

        # Memastikan data material yang diperbarui sesuai
        self.assertEqual(updated_material[0]['material_code'], 'MOX002951S')
        self.assertEqual(updated_material[0]['material_name'], 'Vest Dylan Limited Edition')

    def test_delete_material(self):
        # Menghapus data material yang telah dibuat
        self.material.unlink()

        # Mencoba membaca data material yang telah dihapus
        with self.assertRaises(Exception):
            self.material.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'supplier'])
