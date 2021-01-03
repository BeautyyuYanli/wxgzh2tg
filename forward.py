import requests
import urllib
import feedparser
from config import proxies

def forward(post, tg, donelist):
    message = post[2] + ': ' + post[0] + ' Link: ' + post[1]
    message = urllib.parse.quote(message)
    send_text = 'https://api.telegram.org/bot' + tg[0] + '/sendMessage?chat_id=' + tg[1] + '&parse_mode=HTML&text=' + message
    try:
        code = requests.get(send_text, proxies=proxies, timeout=10).status_code
        if (code == 200):
            donelist.append(post[0])
        else:
            raise ValueError(code)
    except:
        print('error when forwarding: ' + post[0])
    else:
        print('forwarded: ' + post[0])
    return 0
