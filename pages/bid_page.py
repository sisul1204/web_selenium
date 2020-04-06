# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/6 11:26

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BidPage(BasePage):
    bid_input_locator = (By.CSS_SELECTOR, '.form-control')
    bid_confirm_locator = (By.CSS_SELECTOR, '.btn-special')


    @property
    def bid_input(self):
        return self.wait_visible_element(self.bid_input_locator)

    @property
    def bid_confirm_button(self):
        return self.wait_visible_element(self.bid_confirm_button)

