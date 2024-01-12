import socket
import time
import os

server = "irc.chat.twitch.tv"
port = 6667
channel = "#castcrafter"
bot_username = "samelloBot"

oauth_token = "oauth:0"

irc = socket.socket()
irc.connect((server, port))

irc.send(f"PASS {oauth_token}\r\n".encode("utf-8"))
irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
irc.send(f"JOIN {channel}\r\n".encode("utf-8"))

