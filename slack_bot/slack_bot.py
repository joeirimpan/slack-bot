# -*- coding: utf-8 -*-
import requests
import json

class Slack:

    def __init__(self, url):
        self.base_url = url
        self.session = requests.Session()

    def notify(self, **kwargs):
        return self.session.post(
            self.base_url,
            data={
                'payload': json.dumps(kwargs)
            }
        )

