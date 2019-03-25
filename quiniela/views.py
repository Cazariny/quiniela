import json
from datetime import datetime

from quiniela import app, db
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import desc
from flask import render_template, redirect, url_for, session, request,\
    jsonify
from requests.exceptions import HTTPError

from config import Auth
from quiniela.helpers import get_google_auth
from quiniela.models import User, Equipos, Division, Partidos,Quiniela,\
    Quiniela_Det, Torneo,

@app.route('/login')
def login():
    """
    login handler route
    redirects to Google oauth uri if user is not logged in
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    google = get_google_auth()
    # get google oauth url
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    # set oauth state
    session['oauth_state'] = state
    # redirect to google for auth
    return redirect(auth_url)


@app.route('/gCallback')
def callback():
    """
    google callback route
    """
    # redirect to home page if user is logged in
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('index'))
    # check for errors
    if 'error' in request.args:
        # user denied access to their account
        if request.args.get('error') == 'access_denied':
            return 'Access denied by user'
        # some unknown error occured
        return 'Some error has occured. Please try again'
    # missing state information in the callback
    # something went wrong, login again
    if 'code' not in request.args and 'state' not in request.args:
        return redirect(url_for('login'))
    # successful authentication confirmed at this point
    google = get_google_auth(state=session['oauth_state'])
    try:
        # fetch token from google servers
        token = google.fetch_token(
            Auth.TOKEN_URI,
            client_secret=Auth.CLIENT_SECRET,
            authorization_response=request.url)
    except HTTPError as e:
        return 'HTTPError occurred: ' + str(e)
    # get handler for server token
    google = get_google_auth(token=token)
    # get user info now that we have token for user
    resp = google.get(Auth.USER_INFO)
    if resp.status_code == 200:
        # user data fetched
        user_data = resp.json()
        email = user_data['email']
        user = User.query.filter_by(email=email).first()
        if user is None:
            # create new user if user with the email didn't exist
            user = User()
            user.email = email
        user.name = user_data['name']
        user.token = json.dumps(token)
        # save user to database
        db.session.add(user)
        db.session.commit()
        # login user now using flask_login
        login_user(user)
        return redirect(url_for('index'))
    return 'Error when fetching user information from Google'


@app.route('/logout')
@login_required
def logout():
    """
    log user out of the system
    uses flask_login method
    """
    logout_user()
    return redirect(url_for('index'))


@app.route('/equipos')
@login_required
def equipos():
    """"
    Esta ruta mandara a la pantalla para observar los equipos
    """

    equipos = Equipos.query.order_by(desc(Equipos.id))
    return render_template("equipos.html")

@app.route('/int:jornada/new')
@login_required
def new_quiniela():
    jornada =
    hquiniela =
    partidos =
    if request.method == 'POST':
        newQuiniela = Quiniela_Det(jornada=quiniela.jornada,
                        id_quiniela=quiniela.id,
                        user_id=current_user.id,
                       )
        db.session.add(newQuiniela)
        db.session.commit()
        return redirect(url_for('principal'))
    else:
        return render_template('new_quiniela.html', )

