from __future__ import division, print_function

import logging
import json

from flask import Flask, make_response
from werkzeug.exceptions import HTTPException, BadRequest

logger = logging.getLogger(__name__)


def general_exception_handler(error):
    """
    Default error handler for the App
    """
    logger.exception("Request Exception")

    status_code = 500
    reply = dict(
        success=False,
        message="Internal server error"
    )
    if isinstance(error, HTTPException):
        status_code = error.code
        reply['message'] = error.description
        if isinstance(error, BadRequest):
            try:
                err_msg = error.data.get('message')
            except AttributeError:
                err_msg = None
            if err_msg:
                reply['message'] = err_msg
                status_code = error.status_code
    else:
        reply['message'] = str(error)

    response = make_response(
        json.dumps(reply),
        status_code,
        {'content-type': 'application/json'}
    )

    return response


def create_flask(import_name):
    """
    Creates and performs standard initialization of Flask object.

    Args:
        import_name (str):
            Package name to pass to the Flask object

    Returns:
        Flask
    """
    from flask import Flask
    flask = Flask(import_name)
    flask.register_error_handler(Exception, general_exception_handler)

    return flask
