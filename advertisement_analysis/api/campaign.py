from datetime import datetime
from typing import List

from flask import Blueprint
from shuttlis.serialization import serialize

from advertisement_analysis import Config
from advertisement_analysis.api import validators
from advertisement_analysis.api.resource.campaign_resource import campaign_data_resource
from advertisement_analysis.domain.services.campaign_service import get_campaign_service
from advertisement_analysis.utils.flask import APIResponse, APIError
from advertisement_analysis.utils.schema import queryschema, dataschema

blueprint = Blueprint("campaign", __name__, url_prefix="/api/v1")


@blueprint.route("/search", methods=["GET"])
@queryschema(validators.search_schema)
def get_campaign_data(
    channels: List[str] = None,
    countries: List[str] = None,
    group_by: List[str] = None,
    sum_of: List[str] = None,
    order_by: str = None,
    order: str = None,
    os: List[str] = None,
    from_time: datetime = None,
    to_time: datetime = None,
    cpi: str = None,
):
    try:
        campaign_data = get_campaign_service().get_all(
            channels=channels,
            countries=countries,
            os=os,
            from_time=from_time,
            to_time=to_time,
            group_by=group_by,
        )
        campaign_data = campaign_data_resource(
            campaign_data,
            group_by=group_by,
            sum_of=sum_of or [],
            order_by=order_by,
            order=order,
            cpi=cpi,
        )
        return APIResponse(campaign_data)
    except Exception as e:
        return APIError(
            error_message="Error: %s occurred, Please try after some time" % e,
            error_type="Server Error",
        )


@blueprint.route("/bulk_upload", methods=["POST"])
@dataschema(validators.bulk_create_schema)
def bulk_upload(url: str = None):
    print("I am coming inside")

    try:
        campaign_stats = get_campaign_service().bulk_upload(url=url)
        if not campaign_stats:
            raise f"Campaign Creation Error"

        return APIResponse(
            {
                "data_source": url or Config.ADJUST_DATA_URL,
                "records": [
                    serialize(campaign_stat) for campaign_stat in campaign_stats
                ],
            }
        )
    except Exception as e:
        return APIError(
            error_message="Please check the URL, URL given by is : %s" % url,
            error_type="VALIDATION_EXCEPTION",
        )
