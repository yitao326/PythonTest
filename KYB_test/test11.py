# condig:utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion'] = '5.1.1'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'

desired_caps['app'] = r'C:\Users\Administrator\Desktop\kaoyan3.1.0.apk'
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

def check_cancelBtn():
    print("check_cancelBtn")

    try:
        cencelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no CancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print("check_skipBtn")

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no SkipBtn')
    else:
        skipBtn.click()

check_updateBtn()
check_skipBtn()
