from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restplus import Api, Namespace, Resource

from api import restplus
from api.endpoints import supporting_shellfish_routes

import settings
import logging


app = Flask(__name__)
CORS(app)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    restplus.api.init_app(blueprint)
    global_namespace_user = Namespace('supporting_shellfish', path='/supporting_shellfish')
    restplus.api.add_namespace(global_namespace_user)
    restplus.api.add_namespace(supporting_shellfish_routes.ns)
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug= settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
