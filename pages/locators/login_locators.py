# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/6 10:04
from selenium.webdriver.common.by import By


class LoginLocator:
    error_msg_locator = 'div.form-error-info'
    confirm_login_locator = (By.CSS_SELECTOR, 'button.btn-special')
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    invalidate_msg_locator = (By.CSS_SELECTOR, '.layui-layer-content')
