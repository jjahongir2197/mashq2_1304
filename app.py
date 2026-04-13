from flask import Flask, render_template

app = Flask(__name__)

@app.route("/products")
def products():

    products = [

        {"name": "Phone", "price": 800},
        {"name": "Laptop", "price": 1500},
        {"name": "Mouse", "price": 60},
        {"name": "Keyboard", "price": 120},
        {"name": "Monitor", "price": 400}

    ]

    total = 0

    for p in products:
        total += p["price"]

    average = total / len(products)

    expensive = max(products, key=lambda x: x["price"])
    cheap = min(products, key=lambda x: x["price"])

    return render_template(
        "products.html",
        products=products,
        average=average,
        expensive=expensive,
        cheap=cheap
    )


if __name__ == "__main__":
    app.run(debug=True)
