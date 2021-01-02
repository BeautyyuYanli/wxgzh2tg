import getpost
import forward
import botcreds
# database
with open('database.pwp', 'r') as f:
    donelist = f.read().split('$^$')
    f.close()
# subscribe list
subscribe_list = [
    'dut_su',
    'iduter',
    'ituaner',
    'dutcxy',
    'dutjiaowu',
]
for i in subscribe_list:
    update = getpost.getupdate(i, donelist)
    if update != 0:
        forward.forward(update, (botcreds.bot_token, botcreds.bot_chatID), donelist)
    with open('database.pwp', 'w') as f:
        f.write('$^$'.join(donelist))
        f.close()