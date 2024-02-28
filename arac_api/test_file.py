import unittest

import requests
import json


class GetDriversTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8001/arac_api/driver_list/"
        self.headers = {
            'Content-Type': 'application/json'
        }

    def test_all_filter(self):
        payload = json.dumps({
            "endDate": "2024-01-26",
            "startDate": "2016-01-26",
            "minScore": 1.123123,
            "maxScore": 4.124123123,
            "offset": 100,
            "limit": 100
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)

        assert response.status_code == 200

    ## OFFSET
    def test_normal_offset(self):
        payload = json.dumps({
            "offset": 100,

        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)

        assert response.status_code == 200

    def test_over_offset(self):
        payload = json.dumps({
            "endDate": "2024-01-26",
            "startDate": "2016-01-26",
            "minScore": 1.123123,
            "maxScore": 1.124123123,
            "offset": 100,
            "limit": 100
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)

        assert response.status_code == 500

    def correct_offset_but_over_limit(self):
        payload = json.dumps({
            "endDate": "2024-01-26",
            "startDate": "2016-01-26",
            "minScore": 1.123123,
            "maxScore": 1.124123123,
            "offset": 5,
            "limit": 100
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)

        assert response.status_code == 500

    def test_date_range(self):
        payload = json.dumps({
            "endDate": "2024-01-26",
            "startDate": "2016-01-26"
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)
        assert response.status_code == 200

    def test_score_range(self):
        payload = json.dumps({
            "endDate": "2024-01-26",
            "startDate": "2016-01-26"
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)
        assert response.status_code == 200

    def test_over_limit(self):
        payload = json.dumps({
            "limit": 500
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)
        assert response.status_code == 422

    def test_empty_driver_list(self):
        payload = json.dumps({

            "maxScore": 0.123123,
        })

        response = requests.request("GET", self.url, headers=self.headers, data=payload)

        assert response.status_code == 200

