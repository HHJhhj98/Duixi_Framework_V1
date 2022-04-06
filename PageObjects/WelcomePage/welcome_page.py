# -*- coding：utf-8 -*-
# @Time ：2022/4/5 12:57
# @Authon :hhj
# @Annotation:
# @File : welcome_page.py
import allure

from Common.base_page import BasePage
from PageLocators.WelcomePageLocators.welcomepage_locators import WelcomePageLocator as loc
from PageObjects.IndexPage.index_page import IndexPage


class WelcomePage(BasePage):

    # 判断隐保护政策是否存在
    def is_privacy_protection_exsist(self):
        doc = '引导页_判断隐保护政策是否存在'
        return self.is_element_exsist(locator=loc.privacy_text, doc=doc)

    # 点击同意按钮
    def click_privacy_agree_btn(self):
        doc = '引导页_点击同意按钮'
        self.wait_ele_Visible(locator=loc.privacy_agree_btn, doc=doc)
        self.click_element(locator=loc.privacy_agree_btn, doc=doc)

    # 点击不同意按钮
    def click_privacy_disagree_btn(self):
        doc = '引导页_点击不同意按钮'
        self.wait_ele_Visible(locator=loc.privacy_disagree_btn, doc=doc)
        self.click_element(locator=loc.privacy_disagree_btn, doc=doc)

    # 查看用户协议/隐私政策
    def show_privacy_user_agreement_or_policy(self, attr=''):
        '''
        :param attr: 用户协议or隐私政策
        :return: content_des文本
        '''
        if attr == '用户协议':
            doc = '引导页_查看用户协议'
            with allure.step("step1：等待《用户协议》按钮可见"):
                self.wait_ele_Visible(locator=loc.privacy_user_agreement_btn, doc=doc)
            with allure.step("step2：点击《用户协议》按钮"):
                self.click_element(locator=loc.privacy_user_agreement_btn, doc=doc)
            ele_loc = loc.terms_of_service_text
        elif attr == '隐私政策':
            doc = '引导页_查看隐私政策'
            with allure.step("step1：等待《隐私政策》按钮可见"):
                self.wait_ele_Visible(locator=loc.privacy_policy_btn, doc=doc)
            with allure.step("step2：点击《隐私政策》按钮"):
                self.click_element(locator=loc.privacy_policy_btn, doc=doc)
            ele_loc = loc.privacy_policy_text
        with allure.step("step3：等待《用户协议》元素可见"):
            self.wait_ele_Visible(locator=loc.terms_of_service_text, doc=doc)
        with allure.step("step4：获取《用户协议》content-desc文本"):
            content_desc = self.get_ele_attribute(locator=ele_loc, attr='content-desc', doc=doc)
            # self.click_element(locator=loc.terms_of_service_text, doc=doc)
        with allure.step("step5：点击返回按钮"):
            self.click_element(locator=loc.terms_of_service_btn, doc=doc)
        return content_desc

    # # 查看隐私政策
    # def show_privacy_policy(self):
    #     doc = '引导页_查看隐私政策'
    #     with allure.step("step1：等待《隐私政策》按钮可见"):
    #         self.wait_ele_Visible(locator=loc.privacy_policy_btn, doc=doc)
    #     with allure.step("step2：点击《隐私政策》按钮"):
    #         self.click_element(locator=loc.privacy_policy_btn, doc=doc)
    #     with allure.step("step3：等待《隐私政策》元素可见"):
    #         self.wait_ele_Visible(locator=loc.terms_of_service_text, doc=doc)
    #     with allure.step("step4：获取《隐私政策》content-desc文本"):
    #         content_desc = self.get_ele_attribute(locator=loc.terms_of_service_text, attr='content-desc', doc=doc)
    #         # self.click_element(locator=loc.terms_of_service_text, doc=doc)
    #     with allure.step("step5：点击返回按钮"):
    #         self.click_element(locator=loc.terms_of_service_btn, doc=doc)
    #     return content_desc

    # 隐私政策内容上滑
    def slide_up_text(self):
        doc = '引导页_隐私政策内容上滑'
        pass

    # 隐私政策内容上滑
    def slide_down_text(self):
        doc = '引导页_隐私政策内容下滑'
        pass

    def do_welcome(self):
        # 处理欢迎页面
        # 如果没有找到首页的元素/不包含MainActivity，那么就在欢迎界面
        doc = '欢迎页面_引导页'
        flag = IndexPage(self.driver).is_index_page_exsist()
        if flag == False:
            # 滑动欢迎页面至首页
            if self.is_element_exsist(locator=loc.privacy_text, doc=doc) == True:
                self.wait_ele_Presence(locator=loc.privacy_agree_btn, doc=doc)
                self.click_element(locator=loc.privacy_agree_btn, doc=doc)
            self.wait_ele_Visible(locator=loc.began_btn, doc=doc)
