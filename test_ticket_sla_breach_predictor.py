import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from datetime import datetime
from main import band

NOW = datetime(2026, 10, 29, 12, 0, 0)


class TestBreachPredictor(unittest.TestCase):
    def test_breached(self):
        self.assertEqual(band("2026-10-29T08:00:00", 2, NOW), "BREACHED")

    def test_at_risk(self):
        self.assertEqual(band("2026-10-29T08:00:00", 4.5, NOW), "AT RISK")

    def test_ok(self):
        self.assertEqual(band("2026-10-29T11:00:00", 4, NOW), "OK")
