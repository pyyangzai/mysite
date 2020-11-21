import time
import unittest
from appium import webdriver


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1',  # 系统版本号
                        'deviceName': '127.0.0.1:21513',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.gotokeep.keep',  # apk的包名
                        'appActivity': 'com.gotokeep.keep.splash.SplashActivity'  # activity 名称
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_keep(self):
        """keep测试"""
        time.sleep(10)
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView[1]')
        # 根据xpath找到指定元素，进行点击操作
        element.click()
        print('同意并继续')
        time.sleep(3)
        self.driver.find_element_by_id('com.gotokeep.keep:id/edit_phone_in_phone_edit').send_keys("18736916003")
        # 根据id找到指定元素，进行点击操作
        # element.click()
        print('手机号登录')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/image_view_select')
        element.click()
        print('阅读用户协议')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_action')
        element.click()
        print('获取验证码')
        time.sleep(3)
        yzm = input('请输入验证码：')
        print(yzm)
        time.sleep(10)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]').send_keys(yzm[0],yzm[1],yzm[2],yzm[3])
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]').send_keys(yzm[1])
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[3]').send_keys(yzm[2])
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[4]').send_keys(yzm[3])
        print('输入验证码')
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_action')
        element.click()
        print('确定')
        element = self.driver.find_element_by_id('android:id/button2')
        element.click()
        print('跳过安装')
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/text_secondary_action')
        element.click()
        print('暂不开启')
        self.driver.swipe(start_x=500,start_y=1000,end_x=500,end_y=400,duration=None)
        self.driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=400, duration=None)
        self.driver.swipe(start_x=500, start_y=400, end_x=500, end_y=1000, duration=None)
        self.driver.swipe(start_x=500, start_y=400, end_x=500, end_y=1000, duration=None)
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.ImageView')
        element.click()
        print('我的')
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/right_third_button')
        element.click()
        print('设置')
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]')
        element.click()
        print('账号与安全')
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_logout')
        element.click()
        print('退出')
        '''
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView')
        element.click()
        print('阅读用户协议')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/txt_login_method_switcher')
        element.click()
        print('密码登录')
        time.sleep(3)
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView')
        element.click()
        print('忘记密码')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_close_in_enter_phone_number')
        element.click()
        print('返回')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_login_main_two')
        element.click()
        print('QQ登录')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_more_login')
        element.click()
        print('其他登录')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/layout_login_email')
        element.click()
        print('邮箱登录')
        time.sleep(3)
        element = self.driver.find_element_by_id('com.gotokeep.keep:id/btn_close')
        element.click()
        print('返回')
        '''

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test1 = MyTests()
    test1.test_keep()
