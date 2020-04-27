from dndsheets import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    sheets = db.relationship('Sheet', backref='author', lazy=True)

class Sheet(db.Model):
    sheet_id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(60), nullable=False)
    race = db.Column(db.String(60), nullable=False)
    char_class = db.Column(db.String(60), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Stats(db.Model):
    stat_id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer, default=1)
    dexterity = db.Column(db.Integer, default=1)
    constitution = db.Column(db.Integer, default=1)
    inteligence = db.Column(db.Integer, default=1)
    wisdom = db.Column(db.Integer, default=1)
    charisma = db.Column(db.Integer, default=1)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.sheet_id'), nullable=False)

class Skills(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True)
    acrobatics = db.Column(db.Integer, default=1)
    animal_handling = db.Column(db.Integer, default=1)
    arcana = db.Column(db.Integer, default=1)
    athletics = db.Column(db.Integer, default=1)
    deception = db.Column(db.Integer, default=1)
    history = db.Column(db.Integer, default=1)
    insight = db.Column(db.Integer, default=1)
    intimidation = db.Column(db.Integer, default=1)
    investigation = db.Column(db.Integer, default=1)
    medicine = db.Column(db.Integer, default=1)
    nature = db.Column(db.Integer, default=1)
    perception = db.Column(db.Integer, default=1)
    performance = db.Column(db.Integer, default=1)
    persuation = db.Column(db.Integer, default=1)
    religion = db.Column(db.Integer, default=1)
    slight_of_hand = db.Column(db.Integer, default=1)
    stealth = db.Column(db.Integer, default=1)
    survival = db.Column(db.Integer, default=1)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.sheet_id'), nullable=False)