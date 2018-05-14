import pytest
from flask import url_for

class TestLunchbot(object):


    def test_who_is_going_to_lunch(self, client):
        res = client.get(url_for('lunch'))
        assert res.status_code == 200
        assert len(res.json) == 8

        res2 = client.get(url_for('lunch'))
        assert res != res2
