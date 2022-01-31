import csv
from http import HTTPStatus
from typing import List, Dict

import requests

from advertisement_analysis import Config, LOG
from advertisement_analysis.domain.models.campaign import Campaign


def log_response_and_raise(log_msg, response):
    LOG.error(
        log_msg, extra={"status": response.status_code, "response_text": response.text}
    )
    raise RuntimeError(
        f"""
        Response code: {response.status_code}
        Response body:

        {response.text}
        """
    )


class AdjustDataService:
    def __init__(self, adjust_data_url):
        self.adjust_data_url = adjust_data_url

    def get_campaign_stats(self, url: str) -> (List[Campaign], Dict):

        print("I am coming********************", url)

        resp = requests.get(
            url
            if url
            else f"{self.adjust_data_url}/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv"
        )

        print("resp.text.splitlines()", resp.text.splitlines())

        print("resp.status_code", resp.status_code)

        if resp.status_code != HTTPStatus.OK:
            log_response_and_raise("fleet.get_paginated_vehicles.error", resp)

        data = [dict(od) for od in csv.DictReader(resp.text.splitlines())]

        return [Campaign.from_dict(campaign_stat) for campaign_stat in data]


def get_adjust_data_service():
    return AdjustDataService(Config.ADJUST_DATA_URL)
