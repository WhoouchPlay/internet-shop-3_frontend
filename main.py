from flask import Flask, request, url_for, redirect, render_template, session, flash
import os
import binascii
from src.data import data_actitons

from src.data.forms import SignUp, LoginForm

app = Flask(__name__, template_folder="src/templates")
app.secret_key = binascii.hexlify(os.urandom(24))

@app.get("/")
def index():
    products = data_actitons.get_products()
    return render_template("index.html", products=products)

@app.get("/product/<product_id>")
def get_product(product_id):
    product = data_actitons.get_product(product_id)
    return render_template("product.html", product=product)



@app.get("/buy_product/<product_id>")
def buy_product(product_id):
    product = data_actitons.get_product(product_id)
    return f"уес! ви придбали товарес {product['name']}"

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        data_actitons.signup(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            password = form.password.data
        )
        return redirect(url_for('cabinet'))
    return render_template("signup.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg= data_actitons.login(
            email=form.email.data,
            password=form.password.data
        )
        if msg:
            flash(msg)
            return redirect(url_for('cabinet'))
        else:
            flash("Пароль не вірний")
            return redirect(url_for("login"), form=form)



@app.get("/cabinet/")
def cabinet():
    user = data_actitons.get_user()
    if user:
        return render_template("cabinet.html", user=user)
    else:
        return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)