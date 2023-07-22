import uiautomator2 as u2
import time

d = u2.connect()


# 启动 APP
def start_app():
    d.press("home")
    time.sleep(5)
    if d(text=appName).exists():
        d(text=appName).click()
        logon_but = d(resourceId=logon_btn_resource_id)
        if logon_but.exists():
            logon_but.click()
            d(resourceId=acc_num_resource_id).click()
            d.clear_text()
            d.send_keys(acc_num)
            d(resourceId=pass_num_resource_id).click()
            d.clear_text()
            d.send_keys(pass_num)
            d(resourceId=logon_resource_id).click()


# 监听器 未读消息列表
def listen_func():
    start_app()
    while (True):
        time.sleep(listen_frequency)
        listen_list = d.xpath(listen_resource_id).all()
        size = len(listen_list)
        for listen in listen_list:
            if (size > 0):
                listen_offset = listen.offset(listen_offset_transverse, listen_offset_direction)
                d.click(listen_offset[0],
                        listen_offset[1])
                interactive_func()


# 交互器
def interactive_func():
    # 判定是否有回复框
    input = d.xpath(reply_resource_id)
    if input.exists != True:
        d.xpath(exit_btn).click()
        return

    # 打印所有列表内容
    i = 1
    while i < len(d.xpath(info_list_resource_id).all()) + 1:
        info_text = info_list_resource_id + '[%s]' % (i)
        print("text", d.xpath(info_text).child(info_list_sub_resource_id).get_text())
        i += 1

    # 点击回复按钮 回复内容 发送
    input.click()
    d.clear_text()
    d.send_keys(reply_info)
    d.xpath(send_btn_resource_id).click()

    # 退出到列表页
    d.xpath(exit_btn).click()


# *****************登录部分参数*******************************
# APP名称
appName = "QQ"
# 登录按钮标识
logon_btn_resource_id = 'com.tencent.mobileqq:id/btn_login'
# 确定登录标识
logon_resource_id = 'com.tencent.mobileqq:id/login'
# 账号输入框标识
acc_num_resource_id = 'com.tencent.mobileqq:id/em2'
# 账号
acc_num = '1954368045'
# 密码输入框标识
pass_num_resource_id = 'com.tencent.mobileqq:id/password'
# 密码 TODO 输入自己的账号密码
pass_num = '********'

# *****************监听器部分参数*****************************
# 监听唯一标识
listen_resource_id = '//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView'
# 横向 负数为左 正数为右
listen_offset_transverse = -10
# 纵向 负数为下 正数为上
listen_offset_direction = 0
# 监听频率
listen_frequency = 5

# *****************交互器部分参数*****************************
# 回复框标识
reply_resource_id = '//*[@resource-id="com.tencent.mobileqq:id/input"]'
# 退出按钮标识
exit_btn = '//*[@resource-id="com.tencent.mobileqq:id/dz1"]'
# 消息列表标识
info_list_resource_id = '//*[@resource-id="com.tencent.mobileqq:id/listView1"]/android.widget.RelativeLayout'
# 消息列表子级标识
info_list_sub_resource_id = '//*[@resource-id="com.tencent.mobileqq:id/chat_item_content_layout"]'
# 发生消息标识
send_btn_resource_id = '//*[@resource-id="com.tencent.mobileqq:id/fun_btn"]'
# 回复内容
reply_info = '回复！'

if __name__ == '__main__':
    listen_func()
