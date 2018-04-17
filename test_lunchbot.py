import pytest
from flask import url_for

class TestLunchbot(object):

    # you don't need to change this test in order to get it to pass
    def test_who_is_going_to_lunch(self, client):
        res = client.get(url_for('lunch'))
        assert res.status_code == 200
        assert res.json == [
            'Alice',
            'Bob',
            'Charlie'
        ]
