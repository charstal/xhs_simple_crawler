from appium import webdriver
from pymongo import MongoClient
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from processor import Processor
from config import *


class Action():

    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': XHS_PACKAGE,
            'appActivity': XHS_ACTIVITY,
            'noReset': True,
            "automationName": "Uiautomator2"
        }
        global collection
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[XHS_MONGO_DB]
        self.collection = self.db[XHS_MONGO_COLLECTION]
        self.processor = Processor()

    def enterApp(self):
        el1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.xingin.xhs:id/zs')))
        el1.click()
        el2 = self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ak5")))
        el2.click()
        el3 = self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ak4")))
        el3.send_keys(KEYWORD)
        el4 = self.wait.until(EC.presence_of_element_located((By.ID, "com.xingin.xhs:id/ak7")))
        el4.click()
        el5 = self.wait.until(EC.presence_of_element_located((By.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]')))
        el5.click()

    def scroll(self):
        while True:
            # 当前页面显示的所有状态
            items = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.xingin.xhs:id/a1z')))
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.xingin.xhs:id/bhs').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.xingin.xhs:id/anl').get_attribute('text')
                    # 日期
                    date = item.find_element_by_id('com.xingin.xhs:id/ask').get_attribute('text')
                    # 处理日期
                    date = self.processor.date(date)
                    print(nickname, content, date)
                    data = {
                        'nickname': nickname,
                        'content': content,
                        'date': date,
                    }
                    # 插入MongoDB
                    self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)

    def main(self):
        self.enterApp()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()