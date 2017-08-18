from appium.webdriver.common.touch_action import TouchAction

from utils.config import Config
from utils.util import *
import os
from time import sleep
from appium import webdriver
from actions import *
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *

def a_login(test_evm):
    textfields1 = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/et_user_name")
    textfields2 = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/et_user_password")
    phone_num_a = Config().get('phone_num_a')
    password_a = Config().get('password_a')
    textfields1.send_keys(phone_num_a)
    textfields2.send_keys(password_a)
    click_button(test_evm, 'ctrip.android.xconnect:id/btn_login')

def a_logoff_cancel(test_evm):

    click_wait_button(test_evm, 'ctrip.android.xconnect:id/me')
    click_wait_button(test_evm, 'ctrip.android.xconnect:id/tv_exit')
    click_wait_button(test_evm, 'ctrip.android.xconnect:id/lef_btn')

def a_logoff_confirm(test_evm):

    click_wait_button(test_evm, 'ctrip.android.xconnect:id/me')
    click_wait_button(test_evm, 'ctrip.android.xconnect:id/tv_exit')
    click_wait_button(test_evm, 'ctrip.android.xconnect:id/right_btn')

def a_sendmsg(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/rl_item_view")
    input = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
    # el.click()
    msg_1 = Config().get('msg_1')
    input.send_keys(msg_1)
    # self.driver.pressKeyCode(23)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/btn_send_message")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()

def a_sendpic(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/chat_btn_more")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/button_img")
    for i in range(9):
        test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/v_selected")[2*i+1].click()
    click_wait_button(test_evm, "ctrip.android.xconnect:id/done")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()


def a_addfriends1(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_plus")
    friends_name_2 = Config().get('friends_name_2')
    click_wait_button_byname(test_evm, friends_name_2)
    test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/container")[1].click()
    #click_wait_button_byname(test_evm, "测试组")
    group_name_2_1 = Config().get('group_name_2_1')
    click_wait_button_byname(test_evm, group_name_2_1)
    friends_name_3 = Config().get('friends_name_3')
    click_wait_button_byname(test_evm, friends_name_3)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/tv_start_chat")
    input = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
    msg_2 = Config().get('msg_2')
    input.send_keys(msg_2)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/btn_send_message")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()
    # back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    # back.click()

def a_addfriends2(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    friends_name_2 = Config().get('friends_name_2')
    click_wait_button_byname(test_evm, friends_name_2)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_settings")

    cc = test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/riv_avatar")
    cc[1].click()
    # click_wait_button(self, "ctrip.android.xconnect:id/riv_avatar")
    test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/container")[1].click()
    #click_wait_button_byname(test_evm, "测试组")
    group_name_2_1 = Config().get('group_name_2_1')
    click_wait_button_byname(test_evm, group_name_2_1)
    friends_name_4 = Config().get('friends_name_4')
    click_wait_button_byname(test_evm, friends_name_4)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/tv_start_chat")
    input = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
    msg_3 = Config().get('msg_3')
    input.send_keys(msg_3)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/btn_send_message")
    for i in range(3):
        back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
        back.click()

def a_deletefriends(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    new_group_1 = Config().get('new_group_1')
    click_wait_button_byname(test_evm, new_group_1)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_settings")
    cc = test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/riv_avatar")
    cc[4].click()
    friends_name_2 = Config().get('friends_name_2')
    click_wait_button_byname(test_evm, friends_name_2)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/tv_start_chat")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()

def a_quit(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    new_group_2 = Config().get('new_group_2')
    click_wait_button_byname(test_evm, new_group_2)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_settings")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/quit_discussion")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/lef_btn")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/quit_discussion")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/right_btn")

def a_rename1(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    # friends_name_1 = Config().get('friends_name_1')
    # friends_name_2 = Config().get('friends_name_2')
    # friends_name_3 = Config().get('friends_name_3')
    click_wait_button_byname(test_evm,"xuelei3161、xuelei3162、xuelei3163")#’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_settings")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/tv_discussion_name")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/iv_clean_text")
    input = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/et_name")
    new_group_1 = Config().get('new_group_1')
    input.send_keys(new_group_1)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/save")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()

def a_rename2(test_evm):
    click_wait_button(test_evm, "ctrip.android.xconnect:id/conversation")
    click_wait_button_byname(test_evm,"xuelei3161、xuelei3162、xuelei3164")#’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘
    click_wait_button(test_evm, "ctrip.android.xconnect:id/action_settings")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/tv_discussion_name")
    click_wait_button(test_evm, "ctrip.android.xconnect:id/iv_clean_text")
    input = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/et_name")
    new_group_2 = Config().get('new_group_2')
    input.send_keys(new_group_2)
    click_wait_button(test_evm, "ctrip.android.xconnect:id/save")
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()
    back = test_evm.driver.find_element_by_class_name("android.widget.ImageButton")
    back.click()

#长按删除第二个会话
def a_press_delete(test_evm):
    #action1 = TouchAction(test_evm.driver)
    Conversion = test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[1]
    TouchAction(test_evm.driver).press(Conversion).wait(1000).perform()  # 按住应用图标不放
    button_name_1 = Config().get('button_name_1')
    click_wait_button_byname(test_evm,button_name_1)
#长按置顶第三个会话
def a_press_stick(test_evm):
    Conversion = test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[2]
    TouchAction(test_evm.driver).press(Conversion).wait(1000).perform()  # 按住应用图标不放
    button_name_2 = Config().get('button_name_2')
    click_wait_button_byname(test_evm, button_name_2)

#长按取消置顶
def a_press_unstick(test_evm):
    Conversion = test_evm.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[0]
    TouchAction(test_evm.driver).press(Conversion).wait(1000).perform()  # 按住应用图标不放
    button_name_3 = Config().get('button_name_3')
    click_wait_button_byname(test_evm, button_name_3)
