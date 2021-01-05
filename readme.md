# wechat2tg - 将微信公众号的推送转发至telegram channel
本项目提供一种基于微信公众平台的方法将微信公众号的推送转发至tg channel

## 开始使用
### 前置
你应当创建一个`tg bot`, 并获取`bot token`以及`bot chatID`

你应当创建一个`微信公众平台订阅号`

### 安装依赖
将本项目克隆至本地

使用pip安装`requirement.txt`中的所有依赖
```
pip install --user -r requirement.txt
```

其中的`selenium`是一个自动控制的web引擎, 如果你使用`Linux/Windows`机器 在本机上安装`Chrome/Chromium`浏览器即可; 如果你使用其它系统的机器, 请到`selenium`的官方网站上查询如何在python中使用该引擎

`selenium`还要求使用图形界面, 请确保你的机器安装了图形界面或可以连接到其它`X server`

使用`selenium`是为了更高程度地模拟人类行为, 以规避不必要的反爬虫审查

### 配置
1. 在目录下创建文件`config.py`, 并仿照`config.py.temp`在该文件中写入配置信息, 包括`bot token`, `bot chatID`, 订阅公众号列表, 用于连接tg的代理服务器

2. 在目录下创建文件`database.pwp`, 不写入任何内容

3. 登录`微信公众平台`, 将`mp.weixin.qq.com`域名下的cookie以`json`格式保存至`cookies.json`. 你可以使用[这个插件](https://chrome.google.com/webstore/detail/%E3%82%AF%E3%83%83%E3%82%AD%E3%83%BCjson%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%BA%E5%8A%9B-for-puppet/nmckokihipjgplolmcmjakknndddifde)

完成配置后目录应该至少包含:
```
config.py
cookies.json
database.pwp
forward.py
main.py
update.py
chromedriver.exe
```

### 部署
运行`python main.py`以获取订阅公众号的最新文章. 你可以为此创建一个定时任务

请谨慎地配置定时任务, 以免触发微信后台的风控. 以下是一个**仅供参考**的定时任务配置
```
➜ crontab -l
30 6-23/1 * * * sh /home/xxxx/wc2tg.sh

➜ cat wc2tg.sh 
cd /home/xxxx/wechat2tg/
export DISPLAY=:0
timeout 10m python main.py -k
```

### Demo
- Telegram Channel: [DUT_News](https://t.me/DUT_News)

- 与[RSSHub](https://github.com/DIYgod/RSSHub)协作, 将文章进一步转为[rss订阅链接](https://rsshub.app/telegram/channel/DUT_News)

## Todo
- [ ] 项目未使用数据库, 长期使用可能导致`database.pwp`文件过大. 将`database.pwp`替换为数据库
- [ ] 使用`docker`包装`update.py`及其相关内容至`wechat-gzh-api`
- [ ] 使用合适的方法替换标题作为文章的唯一标识
