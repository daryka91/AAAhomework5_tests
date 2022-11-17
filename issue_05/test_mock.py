import unittest
import io
from unittest.mock import Mock, patch
from what_is_year_now import what_is_year_now


class TestCurrentYear(unittest.TestCase):

    def test_1(self):
        with patch('urllib.request.urlopen', return_value=io.StringIO(
                '{"currentDateTime": "2022-01-01"}')):
            year = what_is_year_now()
            self.assertEqual(year, 2022)

    def test_2(self):
        with patch('urllib.request.urlopen', return_value=io.StringIO(
                '{"currentDateTime": "01.01.2022"}')):
            year = what_is_year_now()
            self.assertEqual(year, 2022)

    def test_3(self):
        with patch('urllib.request.urlopen', return_value=io.StringIO(
                '{"currentDateTime": "01/01/2020"}')) as date:
            self.assertRaises(ValueError, what_is_year_now)

