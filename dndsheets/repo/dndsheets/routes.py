from flask import render_template, redirect, url_for
from dndsheets import app, db, bcrypt
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dndsheets.forms import SignupForm, LoginForm, CreateChar
from dndsheets.models import User, Sheet, Stats, Skills

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('my_sheets'))
        else:  
            return '<h1> Invalid username or password </h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data  + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/characters', methods=['GET', 'POST'])
@login_required
def my_sheets():

    createForm = CreateChar()
    sheets = Sheet.query.filter_by(user_id = current_user.id).all()

    if createForm.validate_on_submit():
        sheet = Sheet(char_name=createForm.char_name.data, race=createForm.race.data, char_class=createForm.char_class.data, level=1, user_id=current_user.id)
        db.session.add(sheet)
        db.session.commit()

        stats = Stats(sheet_id = sheet.sheet_id)
        skills = Skills(sheet_id = sheet.sheet_id)

        db.session.add(stats)
        db.session.add(skills)
        db.session.commit()


    return render_template('characters.html', form=createForm, sheets=sheets)

@app.route('/sheets/<s_id>')
@login_required
def sheets(s_id):

    s_id = int(s_id)
    sheet = Sheet.query.filter_by(sheet_id=s_id).first()

    return render_template('sheets.html', sheet=sheet)