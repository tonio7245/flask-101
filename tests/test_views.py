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
        before = len(self.client.get("/api/v1/products").json)
        response = self.client.delete("/api/v1/products/1")
        after = len(self.client.get("/api/v1/products").json)
        self.assertEquals(response.status_code,204)
        self.assertEquals(before,after + 1 )


    def test_get_201_when_creating(self):
        response = self.client.post('/api/v1/products/', data=dict(id=6,name='chose'))
        self.assertEquals(response.status_code,201)
        self.assertEquals(response.json,{ 'id': 6, 'name': 'chose' })

    def test_get_422_if_empty(self):
        response = self.client.patch('/api/v1/products/1', data=dict(name=''))
        self.assertEquals(response.status_code,422)
        response = self.client.patch('/api/v1/products/1')
        self.assertEquals(response.status_code,422)


    def test_get_204_update(self):
        response = self.client.get('/api/v1/products/1')
        self.assertEquals(response.json,{ 'id': 1, 'name': 'Skello' })
        response = self.client.patch('/api/v1/products/1', data=dict(name='Skella'))
        self.assertEquals(response.status_code,204)
        response = self.client.get('/api/v1/products/1')
        self.assertEquals(response.json,{ 'id': 1, 'name': 'Skella' })


