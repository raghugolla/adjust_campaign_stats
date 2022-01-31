from sqlalchemy import func
from sqlalchemy_uuidstr import UUIDType

from advertisement_analysis.store import db
from advertisement_analysis.store.models.base import _EntityBase


class CampaignModel(_EntityBase):
    __tablename__ = "campaign"

    id = db.Column(UUIDType(), primary_key=True)
    channel = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    installs = db.Column(db.Integer, nullable=False)
    spend = db.Column(db.Float, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    campaign_date = db.Column(db.DateTime, nullable=False, default=func.now())
