# -*- coding：utf-8 -*-
# @Time ：2022/4/6 22:02
# @Authon :hhj
# @Annotation:
# @File : base_driver.py
from appium import webdriver
import time
import yaml
import os

from Common.my_log import MyLog
from Common.project_path import *
from Common.system_properties import SystemProperties
from tomorrow import threads

my_log = MyLog()


def baseDriver(server_port=4723, automationName=None, noReset=None, **kwargs):
    '''
    :param server_port: appium启动端口号
    :param automationName: 使用哪个自动化引擎，Appium(缺省)，或UiAutomator2, Espresso，或UiAutomator1
    :param noReset: 重置应用程序状态 true, false
    :param kwargs: 其他Desired capabilities参数
    :return: 返回一个启动对象 -driver
    '''
    # my_log.info('_______________' + yaml_path + '_________________')
    fs = open(yaml_path)
    caps = yaml.load(fs, Loader=yaml.FullLoader)
    # 在5.1版本之后就修改了，使用 yaml.load() 方法需要指定Loader，
    # 通过默认加载器（FullLoader）禁止执行任意函数，
    # 这样 load() 函数也变得更加安全。
    # my_log.info(caps.values)
    Device_ID = SystemProperties().group_call()
    caps['deviceName'] = SystemProperties().get_android_system_properties(Device_ID[0], 'ro.product.model')
    caps['platformVersion'] = SystemProperties().get_android_system_properties(Device_ID[0], 'ro.build.version.release')
    if automationName is not None:
        caps['automationName'] = automationName
    if noReset == False:
        caps['noReset'] = False
    for k, v in kwargs.items():
        caps[k] = v
    # print(caps)
    my_log.info(caps.values)
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), caps)
    return driver





