# -*- coding：utf-8 -*-
# @Time ：2022/4/6 22:02
# @Authon :hhj
# @Annotation:
# @File : base_driver.py
import yaml
from appium import webdriver

from Common.my_log import MyLog
from Common.project_path import yaml_path
from Common.system_properties import SystemProperties

my_log = MyLog()

def baseDriver(automationName=None, noReset=None):
    '''
    :param automationName:
    :param noReset:
    :return:
    '''
    my_log.info('_______________' + yaml_path + '_________________')
    fs = open(yaml_path)
    caps = yaml.load(fs, Loader=yaml.FullLoader)
    # caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'Android Emulator',
    #     'platformVersion': '7.1',
    #     # apk包名
    #     'appPackage': 'com.duixivideo.app',
    #     # apk的launcherActivity
    #     'appActivity': 'app.dupa.festival.MainActivity',
    #     # 重置与否
    #     # 'noReset': 'True'
    # }

    my_log.info(caps.values)
    Device_ID = SystemProperties().group_call()
    caps['deviceName'] = SystemProperties().get_android_system_properties(Device_ID[0], 'ro.product.model')
    caps['platformVersion'] = SystemProperties().get_android_system_properties(Device_ID[0], 'ro.build.version.release')
    if automationName is not None:
        caps['automationName'] = automationName
    if noReset == False:
        caps['noReset'] = False
    my_log.info(caps.values)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    return driver
