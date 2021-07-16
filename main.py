import requests, json, datetime
import forward
from config import subscribe_list

def getUpdate():
    requestUpdate = requests.get("http://127.0.0.1:11459?query=" + "$".join(subscribe_list))
    if requestUpdate.status_code == 200:
        update_pool = requestUpdate.json()
        updateEntries = []
        for i, j in update_pool.items():
            for k in j:
                updateEntries.append(k)
        return 200, updateEntries
    else:
        return requestUpdate.status_code, requestUpdate.text

def compareEntries(his, upd):
    newEntries = []
    hisTitles = [x['title'] for x in his]
    for i in upd:
        if i['title'] not in hisTitles:
            newEntries.append(i)
    return newEntries

if __name__ == "__main__":
    updateCode, updateContent = getUpdate()
    if updateCode == 200:
        with open('history.list', 'r') as f:
            history = json.loads(f.read())
        newEntries = compareEntries(history, updateContent)
        for i in newEntries:
            if (forward.forward(i) == 0):
                i['pubDate'] = datetime.date.today().strftime('%x')
                history.append(i)
            with open('history.list', 'w') as f:
                f.write(json.dumps(history))
    else:
        forward.forward(
            {'title': updateContent, 'link': 'http://bing.com', 'author': 'system'})
