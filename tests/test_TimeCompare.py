from unittest import TestCase
from TimeCompare import TimeCompare
import datetime


class TestTimeCompare(TestCase):

    def test_is_time_in_range(self):
        time_compare = TimeCompare("5:00:00 PM", "8:00:00 AM")
        upper = time_compare.get_upper_time()
        lower = time_compare.get_lower_time()
        mocked_now = datetime.time(7,00,00)
        self.assertFalse(time_compare.is_time_in_range(lower, upper, mocked_now))
        mocked_now = datetime.time(12,00,00)
        self.assertTrue(time_compare.is_time_in_range(upper, lower, mocked_now))
        mocked_now = datetime.time(18,00,00)
        self.assertFalse(time_compare.is_time_in_range(upper, lower, mocked_now))

    def test_convert_to_24_hours(self):
        time_compare = TimeCompare("10:00:00 PM", "10:00:00 PM")
        self.assertEqual(time_compare.convert_to_24_hours("10:00:00 PM"), datetime.time(22,00,00))
        self.assertEqual(time_compare.convert_to_24_hours("04:00:00 AM"), datetime.time(4,00,00))

    def test_get_upper_time(self):
        time_compare = TimeCompare("10:00:00 PM", "10:00:00 PM")
        time_compare.upperTime = "4:07:59 PM"
        self.assertEqual(time_compare.get_upper_time(), "4:07:59 PM")

    def test_get_lower_time(self):
        time_compare = TimeCompare("10:00:00 PM", "10:00:00 PM")
        time_compare.lowerTime = "4:07:59 PM"
        self.assertEqual(time_compare.get_lower_time(), "4:07:59 PM")
