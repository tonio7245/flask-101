from flask import Flask, jsonify, abort

app = Flask(__name__)

the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' },
    { 'id': 4, 'name': 'machin' }
]

@app.route('/')
def hello():
    return "Hello World !"

@app.route('/api/v1/products')
def get_products():
    return jsonify(the_products)

@app.route('/api/v1/products/<id_product>')
def get_product(id_product):
    for elem in the_products:
        if elem['id'] == int(id_product):
            return jsonify(elem)
    abort(404)



