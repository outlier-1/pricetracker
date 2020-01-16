import os
import unittest
import csv
from tracker_hb import HBTracker


class MyTestCase(unittest.TestCase):

    def test_query_constructing(self):
        """ Tests for constructing proper search query
            Test queries contains alphanumeric characters, space and special characters.
            Test samples are read from query_constructing_samples.csv file
        """
        with open('hepsiburada/query_constructing_samples.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for case in reader:
                self.assertEqual(HBTracker.construct_search_query(case[0]),
                                 case[1], "Links don't match.")

    def test_price_extracting(self):
        """ Tests for function get_price_from_link(link)
            Test queries contains product links with different discount options.
            Test samples are read from price_extracting_samples.csv file
        """
        with open('hepsiburada/price_extracting_samples.csv') as file:
            reader = csv.reader(file, delimiter='&')
            for case in reader:
                self.assertEqual(HBTracker.get_price_from_link(case[0]),
                                 case[1], "Price couldn't extracted right")


if __name__ == '__main__':
    unittest.main()
