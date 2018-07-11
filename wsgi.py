from flask import Flask, jsonify, abort, request

app = Flask(__name__)

the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' },
    { 'id': 4, 'name': 'machin' },
    { 'id': 5, 'name': 'bidule' }
]

@app.route('/')
def hello():
    return "Hello World !"

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(the_products)

@app.route('/api/v1/products/<id_product>', methods=['GET','DELETE'])
def do(id_product):
    if request.method == 'GET':
        return get_product(id_product)
    else:
        return delete_product(id_product)

def delete_product(id_product):
    for elem in the_products:
        if elem['id'] == int(id_product):
            the_products.remove(elem)
            return ('', 204)
    abort(404)


def get_product(id_product):
    for elem in the_products:
        if elem['id'] == int(id_product):
            return jsonify(elem)
    abort(404)


@app.route('/api/v1/products/', methods=['POST'])
def create_product():
    the_products.append({'id' : int(request.form['id']),'name' : request.form['name']})
    return (get_product(request.form['id']), 201)



