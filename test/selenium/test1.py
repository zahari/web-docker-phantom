#!/usr/bin/python

import unittest
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLocalhost(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.Firefox()
        desired_cap = {'os': 'Windows', 'os_version': '7', 'browser': 'IE', 'browser_version': '8.0' }
        self.driver = webdriver.Remote(
            command_executor='http://werwrwr1:nEqWnTfc8Z2Z2wM8kW2p@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)
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
