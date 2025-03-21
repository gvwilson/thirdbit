"""Test the JSON server."""

from server import HEARTBEAT
from test_fixtures import client

import util


def test_can_get_heartbeat(client):
    response = client.get("/heartbeat")
    assert response.status_code == util.HTTP_200_OK
    assert response.json == HEARTBEAT
