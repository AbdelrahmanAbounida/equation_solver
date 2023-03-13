from crypt import methods
from flask import request,redirect,render_template,flash,url_for
from .forms import LoginForm, RegisterForm
from app import app
from .models import User
from .extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,current_user, login_required, logout_user


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/linear',methods=['GET'])
@login_required
def linear():
    return render_template('linear.html')

@app.route('/nonlinear',methods=['GET'])
@login_required
def nonlinear():
    return render_template('nonlinear.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        password = generate_password_hash(form.password.data)

        usr = User(email=email,password=password)
        db.session.add(usr)
        db.session.commit()
        flash('You are now registered and can login','success')
        return redirect(url_for('login'))

    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,login_form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("The password is in correct","danger")
                return redirect(url_for('login'))
        else:
            flash("There is no user with this email","danger")
            return redirect(url_for('login'))
    else:
        return render_template('login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))