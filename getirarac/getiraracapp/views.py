import json
import logging

from django.shortcuts import render
from django.views import View
import requests


class GetDriverList(View):
    template_name = 'get_driver.html'
    get_driver_list_url = 'http://127.0.0.1:8001/arac_api/driver_list/'

    def get(self, request, *args, **kwargs):
        try:
            url = self.get_driver_list_url

            data = {
                "startDate": request.GET.get('startDate', ''),
                "endDate": request.GET.get('endDate', ''),
                "minScore": request.GET.get('minScore', ''),
                "maxScore": request.GET.get('maxScore', ''),
                "limit": request.GET.get('limit', ''),
                "offset": request.GET.get('offset', '')
            }

            payload = {key: value for key, value in data.items() if value is not None and value != ""}

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                items = response.json()
                return render(request, self.template_name, {'data': items})
            else:
                logging.error(f"['GetUserList']. Error Code: {response.status_code}")
                return render(request, self.template_name, {'data': response.json()})
        except requests.exceptions.RequestException as e:
            logging.error(f"['GetUserList'] has exception: {e}")
        return render(request, self.template_name, {'items': []})
