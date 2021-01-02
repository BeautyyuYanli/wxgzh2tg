import requests
import urllib
import feedparser
proxies = {
 'http': 'http://127.0.0.1:1081',
 'https': 'http://127.0.0.1:1081',
}
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
        with open ('err.log', 'a') as f:
            f.write('ERR: ' + str(post) + '\n')
