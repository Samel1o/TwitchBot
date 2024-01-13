from setup import *

def help_command(channel):
    print(">help got called")
    time.sleep(waitTime)
    irc.send(
        f"PRIVMSG {channel} :>exit exits, >echo [args] echos, >help prints this, >op [user] op's the user, >op view views the op'ed, >calc [args] calculates\r\n".encode(
            "utf-8"))
    