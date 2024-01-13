from setup import *

def reload_command(channel):
    print(">reload got called")
    irc.send(
        f"PRIVMSG {channel} :reloading...\r\n".encode("utf-8"))
    time.sleep(waitTime)
    restart()
    