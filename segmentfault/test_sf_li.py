import config
import unittest
from selenium import webdriver


class TestSfLi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(config.sf_index_url)
        self.driver.find_element_by_css_selector(config.css_of_index_login_symbol).click()

    def tearDown(self):
        self.driver.quit()

    def test_sf_li_001(self):
        "输入已注册正确的11位手机号，正确的密码登录"
        login_phone_email = self.driver.find_element_by_css_selector(config.css_of_login_phone_email_field)
        login_pwd = self.driver.find_element_by_css_selector(config.css_of_login_pwd_field)
        login = self.driver.find_element_by_css_selector(config.css_of_login_symbol)

        login_phone_email.send_keys('18042463051')
        login_pwd.send_keys('test1234')
        login.click()

        user = self.driver.find_elements_by_css_selector(
            'body > div.global-nav.sf-header.sf-header--index > nav > div.row.hidden-xs.hidden-sm > div.col-sm-4.col-md-3.col-lg-3.text-right > ul > li.opts__item.user.dropdown.hoverDropdown.ml0')
        self.assertEqual(len(user), 1)

    def test_sf_li_002(self):
        "输入已注册正确的邮箱，正确的密码登录"
        pass

    def test_sf_li_003(self):
        "输入已注册正确的11位手机号，错误的密码登录"
        login_phone_email = self.driver.find_element_by_css_selector(config.css_of_login_phone_email_field)
        login_pwd = self.driver.find_element_by_css_selector(config.css_of_login_pwd_field)
        login = self.driver.find_element_by_css_selector(config.css_of_login_symbol)

        login_phone_email.send_keys('18042463051')
        login_pwd.send_keys('test123')
        login.click()
        err = self.driver.find_element_by_css_selector(config.css_of_login_error)
        self.assertTrue('密码错误' in err.text)

    def test_sf_li_007(self):
        "输入错误的10位手机号登录"
        login_phone_email = self.driver.find_element_by_css_selector(config.css_of_login_phone_email_field)
        login_pwd = self.driver.find_element_by_css_selector(config.css_of_login_pwd_field)
        login = self.driver.find_element_by_css_selector(config.css_of_login_symbol)

        login_phone_email.send_keys('1804246305')
        login_pwd.send_keys('test1234')
        login.click()
        err = self.driver.find_element_by_css_selector(config.css_of_login_error)
        self.assertTrue('格式错误' in err.text)

    def test_sf_li_008(self):
        "输入错误的邮箱登录"
        login_phone_email = self.driver.find_element_by_css_selector(config.css_of_login_phone_email_field)
        login_pwd = self.driver.find_element_by_css_selector(config.css_of_login_pwd_field)
        login = self.driver.find_element_by_css_selector(config.css_of_login_symbol)

        login_phone_email.send_keys('123@error')
        login_pwd.send_keys('test1234')
        login.click()
        err = self.driver.find_element_by_css_selector(config.css_of_login_error)
        self.assertTrue('格式错误' in err.text)
