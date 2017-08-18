import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class A_AndroidTests(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        path = Config().get('path')
        url = Config().get('url')
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(path)
        desired_caps['noReset'] = True
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        cls.driver = webdriver.Remote(url, desired_caps)

    def test_a_login(self):
        a_login(self)
        #验证登录成功
        sleep(1)
        result = verify_login(self)
        self.assertTrue(result)

    def test_b_sendmsg(self):
        a_sendmsg(self)
        # 验证发送成功
        sleep(1)
        result = verify_send_success(self)
        self.assertTrue(result)

    def test_c_addfriends1(self):
        a_addfriends1(self)

    def test_d_rename1(self):
        a_rename1(self)

    def test_e_addfriends2(self):
        a_addfriends2(self)

    def test_f_rename2(self):
        a_rename2(self)

    def test_g_deletefriends(self):
        a_deletefriends(self)

    def test_h_quitgroup(self):
        a_quit(self)

    def test_i_press_delete(self):
        a_press_delete(self)

    def test_j_press_stick(self):
        a_press_stick(self)

    def test_k_press_unstick(self):
        a_press_unstick(self)

    def test_l_logoff_cancel(self):
        a_logoff_cancel(self)

    def test_m_logoff_confirm(self):
        a_logoff_confirm(self)
        #验证退出成功
        sleep(1)
        result = verify_logoff(self)
        self.assertTrue(result)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # pipe = 1
    # suite = unittest.TestLoader().loadTestsFromTestCase(A_AndroidTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    report = "D:\study\Test_Framework\\report" + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='Xconnect Test Report', description='修改html报告')
        suite = unittest.TestLoader().loadTestsFromTestCase(A_AndroidTests)
        # unittest.TextTestRunner(verbosity=2).run(suite)
        # runner.run(TestBaiDu('test_search'))
        runner.run(suite)