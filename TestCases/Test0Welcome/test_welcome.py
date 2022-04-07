# -*- coding：utf-8 -*-
# @Time ：2022/4/5 17:10
# @Authon :hhj
# @Annotation:
# @File : test_welcome.py
from time import sleep

import pytest

from Common.my_log import MyLog
from PageObjects.WelcomePage.welcome_page import WelcomePage
from PageObjects.IndexPage.index_page import IndexPage
from TestDatas import welcome_datas as WD
from Common.system_properties import SystemProperties

my_log = MyLog()


class Test0Welcome:

    # 有隐私保护政策，点击用户协议or隐私政策
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    @pytest.mark.demo3
    def test_welcome_0_user_policy(self, start_function_App, user_or_policy_data):
        my_log.info("****{}****".format(user_or_policy_data['title']))
        driver = start_function_App[0]
        wel = WelcomePage(driver)
        sleep(3)
        res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        assert res == user_or_policy_data['check']

    # 有隐私保护政策，点击用户协议or隐私政策后返回
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    @pytest.mark.demo3
    def test_welcome_1_user_policy(self, start_function_App, user_or_policy_data):
        my_log.info("****{}****".format(user_or_policy_data['title']))
        driver = start_function_App[0]
        wel = WelcomePage(driver)
        sleep(3)
        res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        assert wel.is_privacy_protection_exsist()

    @pytest.mark.usefixtures("start_function_App_and_launcher_name")  # 在运行的时候，会去运行start_function_App函数
    @pytest.mark.demo1
    def test_welcome_3_click_warm_tips_quit_btn(self, start_function_App_and_launcher_name):
        my_log.info("****引导页_温馨提示_退出应用_点击****")
        launcher_name = start_function_App_and_launcher_name[1]
        driver = start_function_App_and_launcher_name[0]
        wel = WelcomePage(driver)
        sleep(3)
        wel.click_privacy_disagree_btn()
        res = wel.click_warm_tips_quit_btn()
        my_log.info(res)
        assert res == launcher_name

    @pytest.mark.demo2
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    def test_welcome_4_click_warm_tips_agree_btn(self, start_function_App):
        my_log.info("****引导页_温馨提示_退出应用_点击****")
        driver = start_function_App[0]
        wel = WelcomePage(driver)
        sleep(3)
        wel.click_privacy_disagree_btn()
        res = wel.click_warm_tips_agree_btn()
        # my_log.info(res)
        assert res

    @pytest.mark.demo2
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    def test_welcome_5_click_privacy_agree_btn(self, start_function_App):
        my_log.info("****引导页_同意_点击****")
        driver = start_function_App[0]
        wel = WelcomePage(driver)
        sleep(3)
        wel.click_privacy_agree_btn()
        assert wel.is_began_btn_exsist()

    @pytest.mark.demo2
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    def test_welcome_6_click_began_btn(self, start_function_App):
        my_log.info("****引导页_同意_点击_马上开始_点击****")
        driver = start_function_App[0]
        wel = WelcomePage(driver)
        index = IndexPage(driver)
        sleep(3)
        wel.click_privacy_agree_btn()
        wel.click_began_btn()
        assert index.is_index_page_exsist()
