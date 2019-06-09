import logging

import flask
from flask_restplus import Api
import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Supporting Shellfish API',
          description='Supporting Shellfish generating tips for a better life, based on emotions!')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500