"""Test the JSON server."""

import pytest

from server import HEARTBEAT, create_app


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_can_get_heartbeat(client):
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json == HEARTBEAT
