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


server = "irc.chat.twitch.tv"
port = 6667
channel = "#treeedbot"
bot_username = "samelloBot"
operators = ["treeed", "same1lo"]

irc = socket.socket()
irc.connect((server, port))

irc.send(f"PASS {os.getenv("oauth_token")}\r\n".encode("utf-8"))
irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
irc.send(f"JOIN {channel}\r\n".encode("utf-8"))
