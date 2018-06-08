from __future__ import division, print_function

import requests

from werkzeug.exceptions import HTTPException


class CoupChallenge(object):
    def __init__(self, base_url=None):
        base_url = base_url or 'http://127.0.0.1:8080'
        self.url = base_url.rstrip('/') + '/v0'

    def num_of_fe(self, scooters, c, p):
        """
        Find number of Fleet Engineers

        Args:
            scooters (list): scooters from districts in Berlin that Coup operates
            c (int): Number of scooters a single FM may supervise
            p (int): Number of scooters a single FE may supervise

        Returns:
            int
        Raises:
            HTTPException
        """
        payload = dict(
            scooters=scooters,
            C=c,
            P=p
        )

        response = requests.post(
            self.url + '/fleet-management',
            json=payload
        )

        if not response.ok:
            raise HTTPException(str(response.json()), response.status_code)

        return response.json()['fleet_engineers']
