import update
import forward
from config import bot_token, bot_chatID


if __name__ == "__main__":
    # database
    with open('database.pwp', 'r') as f:
        donelist = f.read().split('$^$')
        f.close()

    # get updates
    update_pool = update.update()
    new_update_pool = []
    for i in update_pool:
        if i[0] not in donelist:
            new_update_pool.append(i)

    # forward to telegram
    for i in new_update_pool:
        forward.forward(i, (bot_token, bot_chatID), donelist)
        with open('database.pwp', 'w') as f:
            f.write('$^$'.join(donelist))
            f.close()