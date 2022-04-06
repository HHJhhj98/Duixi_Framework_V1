# -*- coding：utf-8 -*-
# @Time ：2022/4/5 17:10
# @Authon :hhj
# @Annotation:
# @File : test_welcome.py
import pytest

from Common.my_log import MyLog
from PageObjects.WelcomePage.welcome_page import WelcomePage
from TestDatas import welcome_datas as WD

my_log = MyLog()


@pytest.mark.usefixtures("startApp")  # 在运行的时候，会去运行access_web函数
class Test0Welcome:

    # 有隐私保护政策，点击用户协议or隐私政策
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.demo3
    def test_welcome_0_user_policy(self, startApp, user_or_policy_data):
        my_log.info("****正常用例——{}****".format(user_or_policy_data['title']))
        driver = startApp[0]
        wel = WelcomePage(driver)
        res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        assert res == user_or_policy_data['check']

    # 有隐私保护政策，点击用户协议or隐私政策后返回
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.demo3
    def test_welcome_1_user_policy(self, startApp, user_or_policy_data):
        my_log.info("****正常用例——{}****".format(user_or_policy_data['title']))
        driver = startApp[0]
        wel = WelcomePage(driver)
        res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        assert wel.is_privacy_protection_exsist()
