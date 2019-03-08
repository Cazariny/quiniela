from quiniela import db
import random
import string
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """
    Registered user information is stored in db
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True)
    picture = db.Column(db.String)
    email = db.Column(db.String)
    token = db.column(db.text)

class Equipos(db.model):
    """
    Equipos locales y visitantes
    """
    __tablename__ = 'equipos'

    id = db.Column(db.Integer)
    nombre = db.Column(db.String(50))
    sede = db.Column(db.String(50))
    id_division = db.Column(db.Integer, db.ForeignKey('division.id'))

class Division(db.model):
    """
    En esta tabla se guardará la division en la que juega un equipo
    """
    __tablename__ = 'division'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    equipos = db.relationship('equipos', backref='division', uselist=True)

class Torneo(db.model):
    """"
    En esta tabla se guardaran los torneos en los que se aplicaran las quinielas
    """
    __tablename__ = 'torneo'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), Null=False)
    quiniela = db.relationship('Quiniela', backref='torneo', uselist=True)

class Quiniela(db.model):
    """
    Esta tabla guardara las quinielas de cada jornada y torneo
    """
    __tablename__  = 'partidos'

    id = db.Column(db.Integer, primary_key=True)
    jornada = db.Column(db.Integer)
    torneo = db.Column(db.Integer, db.ForeignKey('torneo.id', ondelete='CASCADE'))
    fecha_init = db.Column(db.Date)
    fecha_end = db.Column(db.Date)


class Quiniela_Det(db.model):
    """
    Esta tabla va a contener el numero de jornada en la cual se esta prediciendo
    """
    __tablename__ = 'quiniela_det'

    id = db.Column(db.Integer, primary_key=True)
    id_quiniela = db.Column(db.Integer, db.ForeignKey('quiniela.id', ondelete='CASCADE'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_partido1 = db.Column (db.integer)