# coding=utf-8
from appium import webdriver

desired_caps = {}
# 逍遥模拟器
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion'] = '5.1.1'

# 真机
# desired_caps['deviceName'] = 'MX4'
# desired_caps['platforVersion'] = '5.1'
# desired_caps['udid'] = '750BBKL22GDN'

desired_caps['app'] = r'C:\Users\Administrator\Desktop\app-dev-release.apk'
desired_caps['appPackage'] = 'com.mixpace.android.mixpace'
desired_caps['appActivity'] = '.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

