from datetime import datetime
from typing import List, Dict

from shuttlis.serialization import serialize
from shuttlis.utils import uuid4_str
from sqlalchemy import func

from advertisement_analysis.domain.models.campaign import Campaign
from advertisement_analysis.store import db as _db
from advertisement_analysis.store.models.campaign import CampaignModel

sum_fields = ["impressions", "clicks", "installs", "spend", "revenue"]


class CampaignRepo:
    def __init__(self):
        self.db = _db

    def upsert_multi(self, campaigns: List[Campaign]):
        campaign_models = [self._to_domain_model(campaign) for campaign in campaigns]
        ids = [campaign.id for campaign in campaign_models]
        for campaign_model in campaign_models:
            self.db.session.merge(campaign_model)
        self.db.session.commit()
        return self.get_by_ids(ids=ids)

    def get_by_ids(self, ids) -> List[Campaign]:
        campaign_models = (
            self.db.session.query(CampaignModel).filter(CampaignModel.id.in_(ids)).all()
        )

        return [
            self._from_domain_model(campaign_model=campaign_model)
            for campaign_model in campaign_models
        ]

    def get_all(
        self,
        channels: [str] = None,
        countries: [str] = None,
        operating_systems: [str] = None,
        from_time: datetime = None,
        to_time: datetime = None,
        group_by_fields: List[str] = None,
    ) -> List[Dict]:
        if group_by_fields:
            group_by_fields = tuple(group_by_fields)
            query = self.db.session.query(
                *group_by_fields,
                func.sum(CampaignModel.impressions),
                func.sum(CampaignModel.clicks),
                func.sum(CampaignModel.installs),
                func.sum(CampaignModel.spend),
                func.sum(CampaignModel.revenue),
            )
        else:
            query = self.db.session.query(CampaignModel)

        if channels:
            query = query.filter(CampaignModel.channel.in_(channels))

        if countries:
            query = query.filter(CampaignModel.country.in_(countries))

        if operating_systems:
            query = query.filter(CampaignModel.os.in_(operating_systems))

        if from_time:
            query = query.filter(CampaignModel.campaign_date >= from_time)

        if to_time:
            query = query.filter(CampaignModel.campaign_date <= to_time)

        if group_by_fields:
            query = query.group_by(*group_by_fields)
            models = query.all()
            return [
                dict(zip(list(group_by_fields) + sum_fields, model)) for model in models
            ]

        models = query.all()

        return [serialize(self._from_domain_model(model)) for model in models]

    def _to_domain_model(self, campaign: Campaign) -> CampaignModel:
        return CampaignModel(
            id=campaign.id or uuid4_str(),
            channel=campaign.channel,
            country=campaign.country,
            os=campaign.os,
            impressions=campaign.impressions,
            clicks=campaign.clicks,
            installs=campaign.installs,
            spend=campaign.spend,
            revenue=campaign.revenue,
            campaign_date=campaign.campaign_date,
        )

    def _from_domain_model(self, campaign_model: CampaignModel) -> Campaign:
        return Campaign(
            id=campaign_model.id,
            channel=campaign_model.channel,
            country=campaign_model.country,
            os=campaign_model.os,
            impressions=campaign_model.impressions,
            clicks=campaign_model.clicks,
            installs=campaign_model.installs,
            spend=campaign_model.spend,
            revenue=campaign_model.revenue,
            campaign_date=campaign_model.campaign_date,
        )


def get_campaign_repo():
    return CampaignRepo()
