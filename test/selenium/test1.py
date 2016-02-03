#!/usr/bin/python

import unittest
import time
from selenium import webdriver


class TestLocalhost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.Firefox()
        self.driver.set_window_size(1120, 550)

    def test1_url(self):
        """ Test 1
        """
        self.driver.get("http://localhost")
        self.assertIn('Hello world!', self.driver.title)
    
    def test2_url(self):
        """ Test 2
        """
        self.driver.get("http://localhost")
        self.assertEqual(
           self.driver.find_element_by_id("button1").get_attribute("innerHTML"), "Click me!"
        )

    def test3_url(self):
        """ Test 3
        """
        self.driver.get("http://localhost")
        self.driver.find_element_by_id("button1").click()
        self.assertNotEqual(
           self.driver.find_element_by_id("button1").get_attribute("innerHTML"), "Click me!"
        )

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
