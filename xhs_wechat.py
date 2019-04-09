
from appium import webdriver

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep
from processor import Processor
from config import *


class XHS():

    index=1
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': WECHAT_PACKAGE,
            'appActivity': WECHAT_ACTIVITY,
            'noReset': True,
            "automationName": "Uiautomator2"
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[WECHAT_XHS_MONGO_DB]
        self.collection = self.db[WECHAT_XHS_MONGO_COLLECTION]
        # 处理器
        self.processor = Processor()
    
    def login(self):
        """
        登录微信
        :return:
        """
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/cjk')))
        login.click()
        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/h2')))
        phone.set_text(USERNAME)
        # 下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/adj')))
        next.click()
        # 密码
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/h2"][1]')))
        password.set_text(PASSWORD)
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/adj')))
        submit.click()

    
    def enter(self, index=1):
        """
        进入小红书
        :return:
        """
        # 选项卡
        tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]')))
        tab.click()
        # 小程序
        app = self.wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[9]")))
        app.click()

        xhs = self.wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.FrameLayout[@content-desc=\"当前所在页面,小程序\"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]")))
        xhs.click()

        search = self.wait.until(EC.presence_of_element_located((By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View")))
        search.click()

        # 爬取内容or爬取note_id

        # 这句注释掉就是爬取note_id
        self.card_selete()



    def card_selete(self):
        card = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View/android.view.View[" + str(self.index) + "]/android.view.View[1]/android.widget.Button/android.view.View[1]/android.view.View/android.widget.Image")))

        card.click()

        self.index = self.index + 1
        sleep(SCROLL_SLEEP_TIME)

    def back_button(self):
        back = self.wait.until(EC.presence_of_element_located((By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.widget.Image")))
        back.click()
        sleep(SCROLL_SLEEP_TIME)

    def crawl(self):
        """
        爬取
        :return:
        """
        while True:

            # 上滑
            try:
                self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            except WebDriverException:
                self.back_button()
                self.card_selete()

            sleep(SCROLL_SLEEP_TIME)

    
    def main(self):
        """
        入口
        :return:
        """
        # 登录
        # self.login()
        # 进入小红书
        self.enter()
        # 爬取
        self.crawl()


if __name__ == '__main__':
    xhs = XHS()
    xhs.main()
