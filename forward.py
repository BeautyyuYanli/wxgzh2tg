import requests
import urllib
from config import proxies
def forward(post, tg, donelist):
    message = '#' + post['author'] + ' 发表了文章: <a href="' + post['link'] + '">' + post['title'] + '</a>'
    message = urllib.parse.quote(message)
    send_text = 'https://api.telegram.org/bot' + tg[0] + '/sendMessage?chat_id=' + tg[1] + '&parse_mode=HTML&text=' + message
    try:
        code = requests.get(send_text, proxies=proxies, timeout=10).status_code
        if (code == 200):
            donelist.append(post['title'])
        else:
            raise ValueError(code)
    except:
        print('error when forwarding: ' + post['title'])
    else:
        print('forwarded: ' + post['title'])
    return 0
