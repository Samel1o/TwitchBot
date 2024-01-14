from setup import *


def reload_command():
    sendMSG(channel, "reloading...")
    time.sleep(waitTime)
    restart()
    