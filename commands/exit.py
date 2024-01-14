from setup import *


def exit_command():
    sendMSG(channel, "The bot is quitting....")
    
    time.sleep(waitTime)

    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()
    