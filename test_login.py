# * coding:utf-8 *
# Author:sisul
#创建时间：2020/4/5 14:24

from pages.login_page import LoginPage
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from ddt import ddt, data
from data.login_data import user_info_error, user_info_invalidate



@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        self.login_page.user_elem.clear()
        self.login_page.pwd_elem.clear()

    # @data(*user_info_error)
    # def test_login_1_error(self, my_data):
    #     self.login_page.login(my_data[0], my_data[1])
    #     error_msg_element = self.login_page.get_actual_result()
    #     self.assertEqual(error_msg_element.text, my_data[2])


    @data(*user_info_invalidate)
    def test_login_2_invalidate(self, user_info):
        '''没有授权的异常用例'''
        self.login_page.login(user_info[0], user_info[1])
        invalid_msg_element = self.login_page.get_invalidate_result()
        self.assertEqual(invalid_msg_element.text, user_info[2])


    # def test_login_2_success(self):
    #     self.login_page.login('18252063029', 'lizhipeng123')
    #     user_element = HomePage(self.driver).user_element
    #     self.assertEqual(user_element.text, '我的帐户[小蜜蜂138526793]')




if __name__ == '__main__':
    unittest.main()