import socket
import time
from dotenv import load_dotenv
from os import getenv, execv
import sys
import json


load_dotenv()

def restart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    import os
    execv(sys.executable, ['python'] + sys.argv)

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


json_oauth_token = json.loads(getenv("oauth_token"))

def switchOAUTH(user):
    global irc
    global botuser
    
    irc = socket.socket()
    irc.connect((server, port))
    
    if user == "test":
        oauth_token = json_oauth_token["treeed"][0]
        botuser = json_oauth_token["treeed"][1]
    else:
        oauth_token = json_oauth_token["samello"][0]
        botuser = json_oauth_token["samello"][1]
    
    irc.send(f"PASS {oauth_token}\r\n".encode("utf-8"))
    irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
    irc.send(f"JOIN {channel}\r\n".encode("utf-8"))

switchOAUTH("")

