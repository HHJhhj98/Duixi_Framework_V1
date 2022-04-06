# -*- coding：utf-8 -*-
# @Time ：2022/4/3 21:50
# @Authon :hhj
# @Annotation:
# @File : conftest.py
import pytest
import yaml

from Common.base_page import BasePage
from PageLocators.WelcomePageLocators.welcomepage_locators import WelcomePageLocator as loc
from Common.project_path import *
from appium import webdriver


# @pytest.fixture
# def startApp():
#     # 准备服务器参数，与appium server进行连接
#     # 1、要不要判断欢迎界面是否存在?
#     # 2、要不要判断当前用户是否已登录？
#     pass


# def baseDriver(automationName=None, noReset=None):
#     '''
#     :param automationName:
#     :param noReset:
#     :return:
#     '''
#     fs = open(yaml_path)
#     caps = yaml.load(fs)
#     if automationName is not None:
#         caps['automationName'] = automationName
#     if noReset == False:
#         caps['noReset'] = False
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
#     return driver

# def do_welcome(driver):
#     # 处理欢迎页面
#     # 如果没有找到首页的元素/不包含MainActivity，那么就在欢迎界面
#     doc = '欢迎页面_引导页'
#     curAct = driver.current_activity
#     if curAct.find("Mainactivity")==-1:
#         # 滑动欢迎页面至首页
#         if BasePage(driver).is_element_exsist(locator=loc.privacy_text,doc=doc)==True:
#             BasePage(driver).wait_ele_Presence(locator=loc.privacy_agree_btn,doc=doc)
#
#         else:
