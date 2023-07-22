import uiautomator2 as u2
import time

d = u2.connect()

d(text='QQ').click()

# d(resourceId="com.tencent.mobileqq:id/btn_login").click()
time.sleep(2)

d(resourceId="com.tencent.mobileqq:id/em2").click()

d.clear_text()
d.send_keys("1954368045")

time.sleep(2)

d(resourceId="com.tencent.mobileqq:id/password").click()
d.clear_text()
d.send_keys('***')
time.sleep(2)

d(resourceId="com.tencent.mobileqq:id/login").click()

