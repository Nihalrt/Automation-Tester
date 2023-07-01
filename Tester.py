import unittest
import HtmlTestRunner
from selenium import webdriver

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://www.google.com")
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("Automation")
        search_input.submit()

        # Assertion to check if the search results page contains the query
        self.assertIn("Automation", self.driver.title)

    def test_search_selenium(self):
        self.driver.get("https://www.google.com")
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("Selenium")
        search_input.submit()

        # Assertion to check if the search results page contains the query
        self.assertIn("Selenium", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed successfully.")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='path/to/reports'))
