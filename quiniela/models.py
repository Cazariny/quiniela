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

class Jornada(db.model):
    """
    Esta tabla guardara las jornadas a disputar
    """
    __tablename__  = 'jornada'

    id = db.Column(db.Integer, primary_key=True)
    torneo = db.Column(db.Integer, db.ForeignKey('torneo.id', ondelete='CASCADE'))
    fecha_init = db.Column(db.Date)
    fecha_end = db.Column(db.Date)
    actual = db.Column(db.Integer)

class HQuiniela (db.model):
    """
    Esta tabla guarda el encabezado de cada quiniela
    """
    __tablename__ = 'hquiniela'

    id = db.Column(db.Integer ,primary_key=True)
    id_jornada = db.Column(db.Integer, db.ForeignKey('jornada.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))

class Quiniela_Det(db.model):
    """
    Esta tabla va a contener el numero de jornada en la cual se esta prediciendo
    """
    __tablename__ = 'quiniela_det'

    id_detalle = db.Column(db.Integer, primary_key=True)
    id_quiniela = db.Column(db.Integer, db.ForeignKey('quiniela.id', ondelete='CASCADE'))
    id_partido = db.Column(db.Integer, db.ForeignKey('partidos.id'))
    reslocal = db.Column(db.Integer)
    resvisit = db.Column(db.Integer)

class Partidos(db.model):
    """"
    En esta tabla se guardaran los datos de los partidos de cada jornada
    """

    __tablename__ = 'partidos'
    id = db.Column(db.Integer, primary_key=True)
    jornada = db.Column(db.Integer, db.ForeignKey('quiniela.jornada', ondelete='CASCADE'))
    idEquipoLocal = db.Column(db.Integer, db.ForeignKey('equipos.id'))
    idEquipoVisit = db.Column(db.Integer, db.ForeignKey('equipos.id'))

