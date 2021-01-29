# wxgzh2tg - 将微信公众号的推送转发至telegram channel

本项目基于姊妹项目[wxgzh-api](https://github.com/BeautyYuYanli/wxgzh-api)将微信公众号推送转发至tg channel

## 开始使用

### 安装依赖

1. 在本地部署运行[wxgzh-api](https://github.com/BeautyYuYanli/wxgzh-api)

2. 将[wxgzh-api](https://github.com/BeautyYuYanli/wxgzh-api)本项目克隆至本地, 使用pip安装`requirement.txt`中的所有依赖
```
git clone https://github.com/BeautyYuYanli/wxgzh2tg.git
cd wxgzh2tg
pip3 install -r requirement.txt
```

### 配置

1. 在目录下创建文件`config.py`, 并仿照`config.py.temp`在该文件中写入配置信息, 包括: tg bot 信息`bot token`, `bot chatID`, 订阅公众号列表`subscribe_list`, 用于连接tg的代理服务器`proxies`

2. 在目录下创建文件`database.pwp`, 不写入任何内容

### 使用
运行`python3 main.py`以转发订阅公众号的最新文章. 你可以为此创建一个定时任务

请谨慎地配置定时任务, 以免触发微信后台的风控. 以下是一个**仅供参考**的定时任务配置
```
$ crontab -l

0 7-23/2 * * * sh /home/xxxx/script/wxgzh2tg.sh

$ cat wxgzh2tg.sh 

cd /home/beautyyu/Development/wxgzh2tg/
timeout 10m python3 main.py -k
```

### Demo

- Telegram Channel: [DUT_News](https://t.me/s/DUT_News)

- 与[RSSHub](https://github.com/DIYgod/RSSHub)协作, 将文章进一步转为[rss订阅链接](https://rsshub.app/telegram/channel/DUT_News)

## Todo
- [ ] 将`database.pwp`替换为数据库
- [ ] 使用合适的方法替换标题作为文章的唯一标识