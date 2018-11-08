from KYB.capability import driver
import random
import time
# 选择头像上传
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[1].click()
time.sleep(3)
driver.find_element_by_id('com.tal.kaoyan:id/save').click()
time.sleep(3)

# 输入随机账号密码邮箱
username = '自学'+'0'+str(random.randint(1000, 9000))        # 生成随机账号
print('username: %s' %username)             # 打印出随机账号

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
time.sleep(3)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').click()
password = 'ytZX'+str(random.randint(1000, 9000))
print('password: %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
time.sleep(3)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').click()
email = 'yito'+str(random.randint(1000, 9000))+'@163.com'
print('email: %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
time.sleep(3)       # 等待2秒

# 点击立即注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
time.sleep(3)

# 院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()

# 专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()

# 点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()