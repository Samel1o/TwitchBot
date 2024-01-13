import socket
import time
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def restart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    import os
    os.execv(sys.executable, ['python'] + sys.argv)

def sendMSG(channel, message):
    irc.send(f"PRIVMSG {channel} :{message}\r\n".encode("utf-8"))

def username_in_list(allowed_operators, username):
    return username in allowed_operators


server = "irc.chat.twitch.tv"
port = 6667
channel = "#treeedbot"
bot_username = "JannikSamsonBot"
operators = ["treeed", "same1lo"]

waitTime = 0.1


irc = socket.socket()
irc.connect((server, port))

irc.send(f"PASS {os.getenv("oauth_token")}\r\n".encode("utf-8"))
irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
irc.send(f"JOIN {channel}\r\n".encode("utf-8"))
