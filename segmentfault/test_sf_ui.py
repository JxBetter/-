import config
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestSfUi(unittest.TestCase):
    def setUp(self):
        # self.driver = WebDriver(command_executor=config.remote_driver_url,
        #                         desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(config.sf_index_url)

    def tearDown(self):
        self.driver.quit()

    def test_sf_ui_001(self):
        "顶部导航栏首页跳转"
        index_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_index_symbol)
        index_symbol_ele.click()
        self.assertEqual(self.driver.current_url, config.sf_index_url)
        self.assertEqual(self.driver.title, 'SegmentFault 思否')

    def test_sf_ui_002(self):
        "顶部导航栏问答跳转"
        qa_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_qa_symbol)
        qa_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/questions')

    def test_sf_ui_003(self):
        "顶部导航栏专栏跳转"
        special_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_special_symbol)
        special_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/blogs')

    def test_sf_ui_004(self):
        "顶部导航栏讲堂跳转"
        lives_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_lives_symbol)
        lives_symbol_ele.click()
        self.assertTrue('讲堂' in self.driver.title)

    def test_sf_ui_005(self):
        "顶部导航栏圈子跳转"
        groups_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_groups_symbol)
        groups_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/groups')

    def test_sf_ui_006(self):
        "顶部导航栏悬停发现按钮"
        find_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_find_symbol)
        ac = ActionChains(self.driver)
        ac.move_to_element(find_symbol_ele).perform()
        self.driver.save_screenshot('./hover_img.png')

    def test_sf_ui_007(self):
        "左边技术频道前端跳转"
        fontend_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_left_fontend_symbol)
        fontend_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/frontend')

    def test_sf_ui_008(self):
        "左边技术频道后端跳转"
        backend_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_left_backend_symbol)
        backend_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/backend')

    def test_sf_ui_009(self):
        "左边技术频道小程序跳转"
        miniprg_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_miniprogram_symbol)
        miniprg_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/miniprogram')

    def test_sf_ui_010(self):
        "左边技术频道人工智能跳转"
        ai_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_ai_symbol)
        ai_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/ai')

    def test_sf_ui_011(self):
        "左边技术频道区块链跳转"
        bitcoin_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_bitcoin_symbol)
        bitcoin_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/bc')

    def test_sf_ui_012(self):
        "左边技术频道安全跳转"
        safe_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_safe_symbol)
        safe_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/netsec')

    def test_sf_ui_013(self):
        "左边技术频道Android跳转"
        android_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_android_symbol)
        android_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/android')

    def test_sf_ui_014(self):
        "左边技术频道IOS跳转"
        ios_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_ios_symbool)
        ios_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/ios')

    def test_sf_ui_015(self):
        "左边技术频道工具跳转"
        tools_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_tools_symbol)
        tools_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/toolkit')

    def test_sf_ui_016(self):
        "左边技术频道程序员跳转"
        programmer_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_prger_symbol)
        programmer_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/channel/programmer')

    def test_sf_ui_017(self):
        "左边技术频道更多标签跳转"
        tags_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_tags_symbol)
        tags_symbol_ele.click()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/tags')

    def test_sf_ui_018(self):
        "页面多次跳转后返回"
        qa_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_qa_symbol)
        qa_symbol_ele.click()
        special_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_special_symbol)
        special_symbol_ele.click()
        lives_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_lives_symbol)
        lives_symbol_ele.click()
        groups_symbol_ele = self.driver.find_element_by_css_selector(config.css_of_groups_symbol)
        groups_symbol_ele.click()

        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/lives')
        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/blogs')
        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/questions')
        self.driver.back()
        self.assertEqual(self.driver.current_url, config.sf_index_url)

    def test_sf_ui_019(self):
        "页面返回后再向前跳转"
        self.test_sf_ui_018()
        self.driver.forward()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/questions')
        self.driver.forward()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/blogs')
        self.driver.forward()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/lives')
        self.driver.forward()
        self.assertEqual(self.driver.current_url, 'https://segmentfault.com/groups')
