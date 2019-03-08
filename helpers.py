
from requests_oauthlib import OAuth2Session
from config import Auth
from quiniela.models import Categories, Items
from flask_login import current_user

def get_google_auth(state=None, token=None):
    """
    get_google_auth creates an oauth object for google oauth
    Thanks http://bitwiser.in/2015/09/09/add-google-login-in-flask.html
    """
    # if token from server is available, just use it
    # we can now fetch user info from google
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    # if state is set (& token is not), create an OAuth session to fetch token
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI)
    # neither token nor state is set
    # start a new oauth session
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE)
    return oauth

def is_not_authorized(item_id):
    """
    is_not_authorized checks if user is not authorized to access a page
    This means he is not the one who created that item
    """
    item = Items.query.get(int(item_id))
    return item.user.id != current_user.id