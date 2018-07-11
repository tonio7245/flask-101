from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 3) # 3 is not a mistake here.


    def test_get_404_when_product_not_exist(self):
        response = self.client.get("/api/v1/products/456")
        self.assertEquals(response.status_code,404)


    def test_get_200_when_product_exists(self):
        response = self.client.get("/api/v1/products/1")
        self.assertEquals(response.status_code,200)

    def test_get_204_when_delete_product(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEquals(response.status_code,204)
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertEquals(len(products), 4)

