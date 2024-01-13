from setup import *


def exit_command():
    print(">exit got called")
    irc.send(
        f"PRIVMSG {channel} :The bot is quitting....\r\n".encode("utf-8"))
    time.sleep(5)
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()
    