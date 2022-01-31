from dataclasses import dataclass, field
from datetime import datetime

from shuttlis.utils import uuid4_str


@dataclass
class Campaign:

    campaign_date: datetime
    channel: str
    country: str
    os: str
    impressions: str
    clicks: int
    installs: int
    spend: float
    revenue: float
    id: str = field(default_factory=uuid4_str)

    @classmethod
    def from_dict(cls, campaign_dict) -> "Campaign":
        return Campaign(
            campaign_date=campaign_dict["campaign_date"]
            if campaign_dict.get("campaign_date")
            else campaign_dict["date"],
            channel=campaign_dict["channel"],
            country=campaign_dict["country"],
            os=campaign_dict["os"],
            impressions=campaign_dict["impressions"],
            clicks=campaign_dict["clicks"],
            installs=campaign_dict["installs"],
            spend=campaign_dict["spend"],
            revenue=campaign_dict["revenue"],
        )
