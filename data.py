from quiniela import db
from quiniela.models import Equipos, Division, Torneo


def new_team(name, sede, id_division):
    """
    new_team crea un nuevo equipo dando nombre, sede y id_division
    """
    equipos = Equipos()
    equipos.name = name
    equipos.sede = sede
    equipos.id_division = id_division
    return equipos


def new_division(name):
    """
    new_division crea una nueva division solo dando el nombre
    """
    division = Division()
    division.name = name
    return division

def new_torneo(name):
    """
    new_torneo crea un nuevo torneo solo dando el nombre
    """
    torneos = Torneo()
    torneos.name = name
    return torneos



def main():
    # list of category names
    division = ['Primera division',
                'Liga de Ascenso',
                'Segunda division',
                'Tercera division']
    for d in division :
        db.session.add(new_division(d))

    equipos = [
        {'America', 'Ciudad de Mexico', 1 }, {'Chivas', 'Guadalajara, ', 1}, {'Atlas', 'Guadalajara', 1},
        {'Toluca', 'Toluca', 1}, {'Necaxa', 'Aguascalientes', 1}, {'Monterrey', 'Monterrey', 1},
        {'Pumas', 'Ciudad de Mexico', 1}, {'Puebla', 'Puebla', 1}, {'Cruz Azul', 'Ciudad de Mexico', 1},
        {'Leon', 'Guanajuato', 1}, {'Monarcas', 'Morelia', 1}, {'Tigres', 'Nuevo Leon', 1},
        {'Tiburones', 'Veracruz', 1}, {'Santos', 'Torreon', 1}, {'Pachuca', 'Pachuca', 1},
        {'Queretaro', 'Queretaro', 1}, {'Tijuana', 'Tijuana', 1}, {'Lobos BUAP', 'Puebla', 1}]
    for c in equipos:
        db.session.add(new_team(c))
    # save all categories to db
    db.session.commit()

    torneo = ['Liga MX']
    for t in torneo:
        db.session.add(new_torneo(t))

if __name__ == '__main__':
    main()