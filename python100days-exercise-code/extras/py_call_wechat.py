import itchat

itchat.auto_login()
friend_list = itchat.get_friends(update=True)
print(len(friend_list))

kenny = friend_list[0]
props = ['NickName', 'Signature', 'Sex']
for prop in props:
    print(kenny[prop])