from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

from webapp.db import db
from flask_login import current_user, login_user, logout_user
from flask import Blueprint, render_template, flash, redirect, url_for

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    page_title = 'Authorization'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=page_title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You successfully logged in')
            return redirect(url_for('news.index'))

    flash('Wrong credentials')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You successfully logged out')
    return redirect(url_for('news.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    page_title = 'Registration'
    registration_form = RegistrationForm()
    return render_template('user/registration.html', page_title=page_title, form=registration_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        new_user = User(username=registration_form.username.data,
                        email=registration_form.email.data,
                        role='user')
        new_user.set_password(registration_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You successfully registered')
        return redirect(url_for('user.login'))
    flash('Please, edit your form')
    return redirect(url_for('user.register'))
