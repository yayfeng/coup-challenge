from __future__ import division, print_function

import math


class FleetCalculator(object):
    """
    Calculate the total number of FEs according to a given fleet configuration.

    Attributes:
        scooters (list): scooters from districts in Berlin that Coup operates
        c (int): how many scooters a single FM may supervise
        p (int): how many scooters a single FE may supervise
    """

    def __init__(self, scooters, c, p):
        self.scooters = scooters
        self.c = c
        self.p = p

    def _cal_fe_only(self, n_scooters):
        """
        Calculate number of FE needed if we only send FE to the given district.

        Args:
            n_scooters (int): Number of scooters

        Returns:
            int
        """
        return int(math.ceil(n_scooters / float(self.p)))

    def _cal_fe_with_fm(self, n_scooters):
        """
        Calculate number of FE needed if we send both FM and FE to the given district.

        Args:
            n_scooters (int): Number of scooters

        Returns:
            int
        """

        if n_scooters < self.c:
            return 0
        return int(math.ceil((n_scooters - self.c) / float(self.p)))

    def _saved(self, n_scooters):
        """
        Calculate number of FE saved if we send FM to current district

        Args:
            n_scooters (int): Number of scooters

        Returns:
            int
        """
        return self._cal_fe_only(n_scooters) - self._cal_fe_with_fm(n_scooters)

    def calculate(self):
        """
        Calculate number of FEs
        """
        total = 0
        max_saved = 0
        for n_scooters in self.scooters:
            total += self._cal_fe_only(n_scooters)
            max_saved = max(max_saved, self._saved(n_scooters))

        return int(total - max_saved)
