from typing import List, Any, Dict

from shuttlis.serialization import serialize

from advertisement_analysis.domain.models.campaign import Campaign

actual_sum_fields = ["impressions", "clicks", "installs", "spend", "revenue"]


def campaign_data_resource(
    campaign_stats: List[Dict],
    group_by: List[str],
    sum_of: List[str],
    order_by: str,
    order: str,
    cpi: str,
) -> List[Any]:

    if cpi and cpi.lower() == "yes":

        for campaign_stat in campaign_stats:
            campaign_stat["cpi"] = campaign_stat["spend"] / campaign_stat["installs"]

    if group_by:
        remove_fields = list(set(actual_sum_fields) - set(sum_of))
        for field in remove_fields:
            campaign_stats = [
                {k: v for k, v in d.items() if k != field} for d in campaign_stats
            ]

    if order_by:
        campaign_stats = sorted(
            campaign_stats,
            key=lambda d: d[order_by],
            reverse=True if order == "DESC" else False,
        )

    return [serialize(campaign_stat) for campaign_stat in campaign_stats]
