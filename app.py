from flask import Flask, render_template, redirect, url_for, session, request, flash

from data.products import products

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<slug>')
def product_detail(slug):
    product = next((p for p in products if p['slug'] == slug), None)
    if not product:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)

@app.route('/add-to-cart/<slug>', methods=['POST'])
def add_to_cart(slug):
    product = next((p for p in products if p['slug'] == slug), None)
    if product:
        cart = session.get('cart', {})
        cart[slug] = cart.get(slug, 0) + 1
        session['cart'] = cart
        flash(f"✅ {product['name']} added to cart!")
        return redirect('/')
    return "Product not found", 404


@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    items = []
    for slug, quantity in cart.items():
        product = next((p for p in products if p['slug'] == slug), None)
        if product:
            item = product.copy()
            item['quantity'] = quantity
            items.append(item)
    return render_template('cart.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)





