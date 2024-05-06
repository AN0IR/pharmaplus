from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# markup = '''<html><body><div id="container">Div Content</div></body></html>'''


# finding the div with the id


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    order_user = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def mainpage():
    try:
        print(f"Current user: {current_user.id}")
        if current_user.name == "admin":
            user_is_admin = True
        return render_template("index.html",
                               logged_in=current_user.is_authenticated,
                               user_is_admin=user_is_admin)
    except:
        return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("Данный адрес почты уже используется. Пожалуйста, используйте его для входа")
            return redirect(url_for('login'))
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("mainpage"))
    # Passing True or False if the user is authenticated.
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('mainpage'))
    # Passing True or False if the user is authenticated.
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/about')
def about():
    try:
        print(f"Current user: {current_user.id}")
        if current_user.name == "admin":
            user_is_admin = True
        return render_template("products.html",
                               logged_in=current_user.is_authenticated,
                               user_is_admin=user_is_admin)
    except:
        return render_template("products.html", logged_in=current_user.is_authenticated)



@app.route('/update_total_price', methods=['POST'])
def update_total_price():
    global total_price
    global cartItems
    data = request.get_json()
    total_price = data.get('totalPrice')
    cartItems = data.get('cartItems')

    print(f"Received total price from client: {total_price}")
    print(f"Received total price from client: {cartItems}")
    # Do something with the total_price variable

    # You can return a response if needed
    return "Total price received successfully", 200


@app.route('/buy')
def buy():
    # ordered_products = []
    # for item in cartItems:
    #     ordered_products.append(item["product"])
    new_order = Orders(
        price=total_price,
        product=cartItems,
        order_user=current_user.id
    )

    print(f"Received total price from client: {total_price}")
    print(f"Received total price from client: {cartItems}")

    db.session.add(new_order)
    db.session.commit()
    return render_template("ordertaken.html", logged_in=current_user.is_authenticated)


@app.route('/cart')
def cart():
    try:
        print(f"Current user: {current_user.id}")
        if current_user.name == "admin":
            user_is_admin = True
        return render_template("cart.html",
                               logged_in=current_user.is_authenticated,
                               user_is_admin=user_is_admin)
    except:
        return render_template("cart.html", logged_in=current_user.is_authenticated)


@app.route('/me')
def me():
    orders = Orders.query.all()
    orders_list = []

    for order in orders:
        product = {
            'id': order.id,
            'product': order.product,
            'price': order.price,
            'order_user': order.order_user
        }

        orders_list.append(product)

    try:
        print(f"Current user: {current_user.id}")
        if current_user.name == "admin":
            user_is_admin = True
        return render_template("account.html",
                               logged_in=current_user.is_authenticated,
                               user_is_admin=user_is_admin,
                               orders_list=orders_list)
    except:
        return render_template("account.html", logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('mainpage'))


if __name__ == "__main__":
    app.run(debug=True)
