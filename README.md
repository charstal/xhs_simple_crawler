# 小红书简单爬虫说明

小红书的反爬机制，真的做的挺好的，我爬得十分痛苦。
经过几次博弈，我总结了几条方法，供大家参考。

>小红书APP: v.5.45.0.6ba2027  
微信APP: version 7.0.3  
手机型号: MI_8  
手机系统: MIUI10.2 稳定版


- Appium
    - 简介: 一个自动化的测试化工具。
    - 平台: 小红书APP。
    - 优点: 这个方法基本上使用所有APP的爬取，稳定性较高。
    - 缺点: 速度慢，有些东西无法爬取, 例:小红书的图片(可能我不会爬)
    - 项目文件：xhs_app.py, 具体配置可以自己找。
- Appium + mitmdump
    - 简介: 因为小红书APP似乎会检测到什么东西, 如果采用mitmdump, 服
    务器方面不会返回response。然后通过Appium 控制微信打开小红书, 
    搜索,点击卡片,进入到详细页。按道理,在这个无限瀑布流里应该都是
    关于这个搜索结果的。但是使用mitmdump之后只有第一项是相关的, 后面
    全部都打乱了, 不知道别人的是怎么样的, 然后通过分析包结构使用
    `mitmdump -s script.py`读取请求,存入mongodb。
    - 平台: 微信里的小红书
    - 优点: 数据更全
    - 缺点: 速度依旧较慢, 一次最多200个
    - 项目文件: xhs_wechat.py/xhs_wechat_item_script.py
    
- Appium + mitmdump + [idate](https://www.idataapi.cn/product/detail/1113?cur_id=1310&init_id=0)
    - 简介: 少量数据推荐。这里是爬取搜索界面每一条笔记的`note_id`, 因为小红书在
    搜索界面下的卡片都是紧跟搜索主体内容的，所以可以保障搜索到的笔记都是相关的
    然后通过`idate`爬`小红书笔记详情 `应该是0.15/100条, 速度：没充值20条/1分钟, 
    充值10元 1条/秒。
    - 优点: 速度更快
    - 缺点: 稍微花点钱, 评论较少, `note_id` 一次最多700条
    - 项目文件: whs_wechat_noteid_script.py/xhs_wechat_py/idata.xhs.py
    
- Appium + mitmdump + 代理池 + chromeDriver
    - 简介: 大量数据推荐, 小红书的网页虽然没有搜索框, 但是可以通过`note_d`获得笔记内容,
    例如`https://www.xiaohongshu.com/discovery/item/5b9518f1672e14389d381496`,后面
    一串就是`note_id`,接下来就到了网页抓取, 方便了许多，不过小心，小红书在web上非常谨慎
    小心。
    - 优点: 速度快,质量高
    - 缺点: 评论只有2条可用, 前期准备`note_id`比较花时间。
    
- 破解header
    - 简介: header有三个关键词`auth`, `auth_sign`, `session_id`, 这三个是破解头关键, 看到
    有些大佬的博客说这东西有时间有效性。但是我爬的时候一直在变。所以求大佬支招。