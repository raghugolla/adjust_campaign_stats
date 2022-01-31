from http import HTTPStatus

import pytest

from sample.utils.flask import APIFlask


@pytest.mark.integration
def test_hello_world_is_returned(app: APIFlask):
    with app.test_client() as client:
        response = client.get("/health")
        data = response.get_json()["data"]
        assert HTTPStatus.OK == response.status_code
