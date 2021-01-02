# wechat2tg - 将微信公众号的推送转发至telegram channel
本项目提供一种方法基于搜狗搜索将微信公众号的推送转发至tg channel

曾经EFB是一种完美解决方案, 但随着微信关闭了web api, 该方案现已不可用

## 开始使用
### 前置
你应当了解如何创建`tg bot`, 并获取`bot token`以及`bot chatID`

### 安装依赖
使用pip安装`main.py`, `forward.py`, `getpost.py`中引用的所有包

其中的`selenium`是一个自动控制的web引擎, 如果你使用`Linux/Windows`机器 在本机上安装`Chrome/Chromium`浏览器即可; 如果你使用其它系统的机器, 请到`selenium`的官方网站上查询如何在python中使用该引擎

`selenium`还要求使用图形界面, 请确保你的机器安装了图形界面或可以连接到其它`X server`

使用`selenium`是为了更高程度地模拟人类行为, 以规避不必要的反爬虫审查

### 配置
在目录下创建文件`botcreds.py`, 并仿照`botcreds.py.temp`在该文件中写入`bot token`以及`bot chatID`

在目录下创建文件`database.pwp`, 不写入任何内容

在`main.py`的`subscribe_list`中修改你所订阅的微信公众号

在`forward.py`的`proxies`中修改你用于连接tg的代理服务器

### 部署
运行`python main.py`以获取订阅公众号的最新文章. 你可以为此创建一个定时任务

## 缺陷
该项目尚且存在若干缺陷

1. 若订阅公众号一次性推送多篇文章, 只能收到最新的一篇推送
2. 项目未使用数据库, 长期使用可能导致`database.pwp`文件过大. 清空文件即可(可能导致最近的几篇文章重复推送).