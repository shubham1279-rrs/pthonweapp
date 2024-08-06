from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for products
products = [
    {'id': 1, 'name': 'T-Shirt', 'price': 19.99, 'description': 'A comfortable cotton t-shirt and can be wore in any season.'},
    {'id': 2, 'name': 'Jeans', 'price': 49.99, 'description': 'Stylish blue jeans and can be wore in any season.'},
    {'id': 3, 'name': 'Jacket', 'price': 89.99, 'description': 'Warm and cozy jacket and can be wore in any season.'}
]

# In-memory cart
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

if __name__ == '__main__':
    app.run(debug=True)
