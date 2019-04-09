import os

# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'MI_8'

# APP包名
XHS_PACKAGE = 'com.xingin.xhs'
WECHAT_PACKAGE = 'com.tencent.mm'
APP_PACKAGE = 'com.xingin.xhs'
# 'com.xingin.xhs'  小红书
# 'com.jingdong.app.mall' jd
# 'com.tencent.mm' wechat

# 入口类名
XHS_ACTIVITY = '.activity.SplashActivity'
WECHAT_ACTIVITY = '.ui.LauncherUI'

APP_ACTIVITY = '.activity.SplashActivity'
# '.activity.SplashActivity' 小红书
# '.MainFrameActivity' jd
# '.ui.LauncherUI' wechat

# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 300

# 微信手机号密码
USERNAME = ''
PASSWORD = ''

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

# MongoDB配置
MONGO_URL = 'localhost'

WECHAT_XHS_MONGO_DB = 'wechat'
WECHAT_XHS_MONGO_COLLECTION = 'xhs'
WECHAT_XHS_NOTE_MONGO_COLLECTION = 'noteID'

XHS_MONGO_DB = 'xhs'
XHS_MONGO_COLLECTION = 'testContent'
XHS_MONGO_ITEM_COLLECTION = 'noteItem'

# 滑动间隔
SCROLL_SLEEP_TIME = 3

KEYWORD = '杭州'


# webspider

MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
TAOBAO_KEYWORD = 'ipad'
MAX_PAGE = 100
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
