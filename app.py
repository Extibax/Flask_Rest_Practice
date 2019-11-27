from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products, "message": "Products's list"})


@app.route('/products/<string:product_name>', methods=['GET'])
def get_product(product_name):
    product_found = [
        product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "No product found"})


@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})


@app.route("/products/<string:product_name>", methods=["PUT"])
def edit_product(product_name):
    product_found = [
        product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]
        return jsonify({"message": "Product updated successfully", "product": product_found[0]})
    return jsonify({"message": "Product not found"})


@app.route("/products/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    product_found = [
        product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        products.remove(product_found[0])
        return jsonify({"message": "Product deleted successfully", "products": products})
    return jsonify({"message": "Product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
