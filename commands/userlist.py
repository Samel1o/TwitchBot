from setup import *

def userlist_command(data,channel):
    if "PRIVMSG" in data:
        print(">userlist got called")
        user_index_start = data.find(":") + 1
        user_index_end = data.find("!")
        username = data[user_index_start:user_index_end]
        userlist = username.strip()
        time.sleep(0.5)
        irc.send(f"PRIVMSG {channel} :Die aktuellen Benutzer im Chat sind: {userlist}\r\n".encode("utf-8"))
        