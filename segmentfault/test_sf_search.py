import config
import unittest
from selenium import webdriver


class TestSfSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1200, 4000)
        self.driver.implicitly_wait(30)
        self.driver.get(config.sf_index_url)

    def tearDown(self):
        self.driver.quit()

    def test_sf_search_005(self):
        "缩小窗口下搜索"
        search_field_ele = self.driver.find_element_by_css_selector(config.css_of_search_field)
        search_btn_ele = self.driver.find_element_by_css_selector(config.css_of_search_btn)

        search_field_ele.send_keys('python')
        search_btn_ele.click()
        self.driver.save_screenshot('./mini_window_search.jpg')
        self.assertNotEqual(self.driver.current_url, 'https://segmentfault.com/')


