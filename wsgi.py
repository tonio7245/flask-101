from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World !"

@app.route('/api/v1/products')
def return_product:
    the_products = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' }
    ]
    return json.dumps(the_products)


