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
    __tablename__  = 'quiniela'

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
    resloc1 = db.Column(db.Integer)
    resvisit1 = db.Column(db.Integer)
    resloc2 = db.Column(db.Integer)
    resvisit2 = db.Column(db.Integer)
    resloc3 = db.Column(db.Integer)
    resvisit3 = db.Column(db.Integer)
    resloc4 = db.Column(db.Integer)
    resvisit4 = db.Column(db.Integer)
    resloc5 = db.Column(db.Integer)
    resvisit5 = db.Column(db.Integer)
    resloc6 = db.Column(db.Integer)
    resvisit6 = db.Column(db.Integer)
    resloc7 = db.Column(db.Integer)
    resvisit7 = db.Column(db.Integer)
    resloc8 = db.Column(db.Integer)
    resvisit8 = db.Column(db.Integer)
    resloc9 = db.Column(db.Integer)
    resvisit9 = db.Column(db.Integer)

class Partidos (db.model):
    """"
    En esta tabla se guardaran los datos de los partidos de cada jornada
    """

    __tablename__ = 'partidos'
    jornada = db.Column(db.Integer, db.ForeignKey('quiniela.jornada', ondelete='CASCADE'))
    local1 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit1 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local2 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit2 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local3 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit3 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local4 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit4 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local5 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit5 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local6 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit6 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local7 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit7 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local8 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit8 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    local9 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
    visit9 = db.Column(db.String(50), db.ForeignKey('equipos.nombre'))
