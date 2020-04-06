# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/5 13:21

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocator


class LoginPage(BasePage):
    login_url = 'http://120.78.128.25:8765/Index/login.html'

    #页面元素定位
    error_msg_locator = 'div.form-error-info'
    confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')


    def get_actual_result(self):
        return self.driver.find_element_by_css_selector(LoginLocator.error_msg_locator)




    def login(self, username, password):

        self.driver.get(self.login_url)

        user_element = self.user_elem
        password_element = self.pwd_elem

        user_element.send_keys(username)
        password_element.send_keys(password)

        e = self.wait_click_element(LoginLocator.confirm_login_locator)
        e.click()


    def get_invalidate_result(self):
        return self.wait_visible_element(LoginLocator.invalidate_msg_locator)

    @property
    def user_elem(self) -> WebElement:
        return self.wait_presence_element(LoginLocator.mobile_locator)

    @property
    def pwd_elem(self) -> WebElement:
        return self.wait_presence_element(LoginLocator.pwd_locator)

