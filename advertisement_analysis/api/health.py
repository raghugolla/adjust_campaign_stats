from flask import Blueprint

from advertisement_analysis.utils.flask import APIResponse

blueprint = Blueprint("advertisement_analysis", __name__)


@blueprint.route("/health")
def health() -> APIResponse:
    return APIResponse({"data": "healthy"})
