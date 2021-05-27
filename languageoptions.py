from logging import setLogRecordFactory
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select

class LanguageOptionsTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./webdriver/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_select_language(self):
        driver = self.driver
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)
        
        self.assertListEqual(exp_options, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output='test_reports', report_name='languageoptions-report'))