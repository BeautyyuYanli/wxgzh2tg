import forward
import requests, urllib, json, time
from config import subscribe_list

if __name__ == "__main__":
    # database
    with open('database.pwp', 'r') as f:
        donelist = f.read().split('$^$')
        f.close()

    # get updates
    update_pool = requests.get("http://127.0.0.1:11459?query=" + "$".join(subscribe_list)).text
    try:
        update_pool = urllib.parse.unquote(update_pool)
        update_pool = json.loads(update_pool)
    except:
        print(update_pool)
        forward.forward({'title': update_pool, 'link': 'none', 'author': 'system'}, [])
    else:
        new_update_pool = []
        for i, j in update_pool.items():
            for k in j:
                if k['title'] not in donelist:
                    new_update_pool.append(k)
        # forward to telegram
        for i in new_update_pool:
            forward.forward(i, donelist)
            with open('database.pwp', 'w') as f:
                f.write('$^$'.join(donelist))
                f.close()