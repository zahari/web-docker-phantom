#!/usr/bin/python

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from testingbotclient import TestingBotClient

class TestLocalhost(unittest.TestCase):

    def setUp(self):
        driver_local = webdriver.PhantomJS()
        #driver_local = webdriver.Firefox()
        desired_cap = {'os': 'Windows', 'os_version': '7', 'browser': 'IE', 'browser_version': '8.0' }
        # Testingbot
        #driver_testingbot = webdriver.Remote(
	#	    command_executor='http://c3a6a535570605cdab649b40111c83d5:7231f285dc925e9842b8a70e67882ea6@hub.testingbot.com/wd/hub',
	#	    desired_capabilities=desired_cap)
        # Browserstack
        driver_browserstack = webdriver.Remote(
            command_executor='http://werwrwr1:nEqWnTfc8Z2Z2wM8kW2p@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)
        self.driver = driver_local
        self.port = 8080
        self.driver.set_window_size(1120, 550)

    def test1_url(self):
        """ Test 1
        """
        self.driver.get("http://localhost:%s" % self.port)
        self.assertIn('Hello world!', self.driver.title)
    
    def test2_url(self):
        """ Test 2
        """
        self.driver.get("http://localhost:%s" % self.port)
        self.assertEqual(
           self.driver.find_element_by_id("button1").get_attribute("innerHTML"), "Click me!"
        )

    def test3_url(self):
        """ Test 3
        """
        self.driver.get("http://localhost:%s" % self.port)
        self.driver.find_element_by_id("button1").click()
        self.assertNotEqual(
           self.driver.find_element_by_id("button1").get_attribute("innerHTML"), "Click me!"
        )

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()
        # Testingbot saves test status
        #status = sys.exc_info() == (None, None, None)
	#tb_client = TestingBotClient('c3a6a535570605cdab649b40111c83d5', '7231f285dc925e9842b8a70e67882ea6')
	#tb_client.tests.update_test(self.driver.session_id, self._testMethodName, status)

if __name__ == '__main__':
    unittest.main()
