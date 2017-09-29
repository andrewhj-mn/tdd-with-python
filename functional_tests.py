from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        super(NewVisitorTest, self).setUp()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        super(NewVisitorTest, self).tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
