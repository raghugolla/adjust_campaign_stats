from advertisement_analysis.exapi.adjust.service import (
    get_adjust_data_service,
    AdjustDataService,
)
from advertisement_analysis.store.repo.campaign import get_campaign_repo, CampaignRepo


class CampaignService:
    def __init__(
        self, campaign_repo: CampaignRepo, adjust_data_service: AdjustDataService
    ):
        self._campaign_repo = campaign_repo
        self._adjust_data_service = adjust_data_service

    def bulk_upload(self, url: str):
        campaign_stats = self._adjust_data_service.get_campaign_stats(url=url)
        return self._campaign_repo.upsert_multi(campaigns=campaign_stats)

    def get_all(self, channels, countries, os, from_time, to_time, group_by):
        return self._campaign_repo.get_all(
            channels=channels,
            countries=countries,
            operating_systems=os,
            from_time=from_time,
            to_time=to_time,
            group_by_fields=group_by,
        )


def get_campaign_service() -> CampaignService:
    return CampaignService(
        campaign_repo=get_campaign_repo(), adjust_data_service=get_adjust_data_service()
    )
