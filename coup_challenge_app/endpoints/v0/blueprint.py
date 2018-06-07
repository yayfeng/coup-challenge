from __future__ import division, print_function

import flask_restplus

from flask import Blueprint

from coup_challenge_app.endpoints.v0 import fleet_management

blueprint = Blueprint('v0', __name__, url_prefix='/v0')

api = flask_restplus.Api(
    blueprint,
    version='v0',
    title='Coup Challenge App',
    validate=True
)

api.add_namespace(fleet_management.namespace)
