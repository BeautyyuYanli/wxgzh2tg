import requests
import urllib
from config import proxies
from config import bot_token, bot_chatID, subscribe_list, qqAuthKey, qqID, qqGroup
def toTg(post, tg):
    message = '#' + post['author'] + ' 发表了文章: <a href="' + post['link'] + '">' + post['title'] + '</a>'
    message = urllib.parse.quote(message)
    send_text = 'https://api.telegram.org/bot' + tg[0] + '/sendMessage?chat_id=' + tg[1] + '&parse_mode=HTML&text=' + message
    code = requests.get(send_text, proxies=proxies, timeout=10).status_code
    if (code == 200):
        return 1
    else:
        return 0
def toQQ(post, authKey):
    # get cover
    preview = requests.get(post['link']).text
    try:
        img = preview.split('"og:image" content="')[1].split('" />')[0]
    except:
        img = 'https://bkimg.cdn.bcebos.com/pic/6c224f4a20a44623850e32b09522720e0df3d718?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg'
    # get short url
#    preview = requests.post('https://www.shorturl.at/shortener.php', {'u': post['link']})
#    shorturl = preview.text.split('id="shortenurl"')[1].split('value="')[1].split('"')[0]
    # push message
    res = requests.post('http://127.0.0.1:8080/auth', json={'authKey': authKey}).json()
    sessionKey = res['session']
    res = requests.post('http://127.0.0.1:8080/verify', json={'qq': qqID, 'sessionKey': sessionKey}).json()
    message = '#' + post['author'] + '\n' + post['title'] + '\n' + post['link'] + '\n'
    res = requests.post('http://127.0.0.1:8080/sendGroupMessage', json={'sessionKey': sessionKey, 'target': qqGroup, 'messageChain': [{ "type": "Plain", "text": message }, {"type": "Image", "url": img}]})
    if (res.status_code == 200):
        return 1
    else:
        return 0
def forward(post):
    try:
        if (toTg(post, (bot_token, bot_chatID))):
#        if (toTg(post, (bot_token, bot_chatID)) and toQQ(post, qqAuthKey)):
            pass
            # donelist.append(post['title'])
        else:
            raise 'forwarding error'
    except:
        print('error when forwarding: ' + post['title'])
        return -1
    else:
        print('forwarded: ' + post['title'])
        return 0
if __name__ == '__main__':
    toQQ({'link': 'http://baidu.com', 'author': 'test', 'title': 'none'}, qqAuthKey)
