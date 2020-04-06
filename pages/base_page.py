# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/6 19:23
import os
import time
from selenium.webdriver import Chrome, ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import config


class BasePage:
    def __init__(self, driver:Chrome):
        self.driver = driver

    def wait_presence_element(self, loactor):
        '''等待元素出现'''
        try:
            return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(loactor))
        except Exception as e:
            self.save_screenshot()


    def wait_click_element(self, locator):
        '''返回的是一个webelement对象'''
        return WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))

    def wait_visible_element(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def gen_screen_file_name_by_ts(self):
        '''生成文件名'''
        ts = str(int(time.time()))
        return ''.join((ts, '.png'))

    def save_screenshot(self):
        '''自动保存截图'''
        img_path = config.LOG_IMG
        file_name = os.path.join(img_path, self.gen_screen_file_name_by_ts())
        self.driver.save_screenshot(file_name)

    def get_url(self):
        return self.driver.current_url

    def switch_window(self, window_name):
        pass

    def switch_iframe(self, frame_reference):
        pass


    def switch_alter(self):
        pass


    def double_click(self, elem):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(elem).perform()

    def context_click(self, elem):
        action_chains = ActionChains(self.driver)
        return action_chains.context_click(elem).perform()

    def scoll_window(self, width, height):
        return self.driver.execute_script('window.scollTo({},{})'.format(width, height))

    def upload_file(self, elem):
        pass




