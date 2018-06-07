from __future__ import division, print_function

import mockito
import unittest

import coup_challenge_app.logic.fleet_calculator as mod


class TestFleetCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        mockito.verifyStubbedInvocationsAreUsed()
        mockito.verifyNoMoreInteractions()
        mockito.unstub()

    def test_calculation(self):
        fc = mod.FleetCalculator([15, 10], 12, 5)
        self.assertEqual(fc.calculate(), 3)

        fc = mod.FleetCalculator([11, 15, 13], 9, 5)
        self.assertEqual(fc.calculate(), 7)

    def test_calculation_fe_gt_fm(self):
        fc = mod.FleetCalculator([15, 10], 5, 12)
        self.assertEqual(fc.calculate(), 2)

        fc = mod.FleetCalculator([11, 15, 13], 5, 9)
        self.assertEqual(fc.calculate(), 5)
