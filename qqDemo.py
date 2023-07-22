import uiautomator2 as u2
import time

d = u2.connect()

# d.app_install("https://downapp.baidu.com/appsearch/AndroidPhone/1.0.82.230/1/1009556z/20230613164404/appsearch_AndroidPhone_1-0-82-230_1009556z.apk?responseContentDisposition=attachment%3Bfilename%3D%22appsearch_AndroidPhone_1009556z.apk%22&responseContentType=application%2Fvnd.android.package-archive&request_id=1690021775_1472592814&type=static")

# 启动 APP
appName = d(text='QQ')
if appName.exists():
    appName.click()
    # 账号按钮
    accNum = d(resourceId="com.tencent.mobileqq:id/btn_login").click()
    if accNum.exists():
        d(resourceId="com.tencent.mobileqq:id/em2").click()
        d.clear_text()
        d.send_keys("1954368045")
        # 密码按钮
        d(resourceId="com.tencent.mobileqq:id/password").click()
        d.clear_text()
        d.send_keys('shuang5210')
        # 登录按钮
        d(resourceId="com.tencent.mobileqq:id/login").click()


# 获取未读消息列表
print("size:", len(d.xpath('//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView').all()))
d.xpath('//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.view.View[2]').click()
# d.xpath(f'//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]').click(offset=(0.5, 0.5))

# 打印所有列表内容
i = 1
while i < len(d.xpath('//*[@resource-id="com.tencent.mobileqq:id/listView1"]/android.widget.RelativeLayout').all()) + 1:
    print("text",d.xpath(f'//*[@resource-id="com.tencent.mobileqq:id/listView1"]/android.widget.RelativeLayout[{i}]').child('//*[@resource-id="com.tencent.mobileqq:id/chat_item_content_layout"]').get_text())
    i += 1

# 点击回复按钮 回复内容 发送
d.xpath('//*[@resource-id="com.tencent.mobileqq:id/input"]').click()
d.clear_text()
d.send_keys("回复！")
d.xpath('//*[@resource-id="com.tencent.mobileqq:id/fun_btn"]').click()

# 退出到列表页
d.xpath('//*[@resource-id="com.tencent.mobileqq:id/dz1"]').click()


