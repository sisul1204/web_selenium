# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/6 10:56

import unittest
from ddt import ddt,data
from selenium import webdriver

from pages.bid_page import BidPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.login_data import user_info_success
from ddt import ddt, data
from data.bid_data import bid_error_data

@ddt
class TestBid(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success[0], user_info_success[1])

    def tearDown(self) -> None:
        self.driver.close()

    @data(*bid_error_data)
    def test_bid_error(self, error_data):
        HomePage(self.driver).click_bid_button()
        bid_page = BidPage(self.driver)
        bid_page.bid_input.send_keys(error_data[0])
        self.assertEqual(bid_page.bid_confirm_button.text, error_data[1])


if __name__ =='__main__':
    unittest.main()
