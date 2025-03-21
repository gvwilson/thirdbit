"""Test the server and model layer together."""

from unittest.mock import patch

from test_fixtures import client
from test_db import STAFF, make_db


def test_can_get_one_row(client):
    with patch("models.connect", make_db):
        response = client.get("/row/4")
        assert response.status_code == 200
        assert response.json == {"staff_id": 4, "personal": "Paula", "family": "Martinez"}
