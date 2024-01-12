import socket
import time
from dotenv import load_dotenv
import os
import sys

load_dotenv()

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
