from advertisement_analysis.store import configure_db_with_app
from advertisement_analysis.utils.config import Config

# local imports
from advertisement_analysis.utils.flask import APIFlask
from advertisement_analysis.utils.log import LOG


def create_app() -> APIFlask:
    LOG.debug("advertisement_analysis.initialisation.start")
    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # NOTE: Order matters here
    configure_db_with_app(app)
    _register_all_blueprints(app)
    LOG.debug("advertisement_analysis.initialisation.end")
    return app


def _register_all_blueprints(app: APIFlask):
    from advertisement_analysis.api import health, campaign

    app.register_blueprint(health.blueprint)
    app.register_blueprint(campaign.blueprint)
