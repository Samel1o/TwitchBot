import time
from setup import *

from commands.test import testcommand
from commands.calc import calc_command
from commands.echo import echo_command
from commands.exit import exit_command
from commands.reload import reload_command
from commands.op import *
from commands.help import help_command
from commands.userlist import userlist_command
from commands.troll import troll_command

allowed_operators = ["treeed", "same1lo"]

def reconnect():
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    time.sleep(5)
    irc.connect((server,port))

    irc.send(f"PASS {os.getenv("oauth_token")}\r\n".encode("utf-8"))
    irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
    irc.send(f"JOIN {channel}\r\n".encode("utf-8"))     

sendMSG(channel, 'JannikSamsonBot started')
try:
    while True:
        try:
            data = irc.recv(4096).decode("utf-8")

            user_index_start = data.find(":") + 1
            user_index_end = data.find("!")
            username = data[user_index_start:user_index_end]

            if data:
                print(data, end="")

                if data.startswith("PING"):
                    irc.send("PONG\r\n".encode("utf-8"))
                    print("PING / PONG")

                if username in operators:
                    if ">echo" in data:
                        echo_command(data, username)
                    elif ">userlist" in data:
                        userlist_command(data,channel)
                    elif ">exit" in data:
                        exit_command()
                    elif ">calc" in data:
                        calc_command(data, channel)
                    elif ">reload" in data:
                        reload_command(channel)
                    elif ">op" in data:
                        op_command(data, operators, channel, allowed_operators, username)
                    elif ">troll" in data:
                        troll_command(data, channel)
                    elif ">help" in data:
                        help_command(channel)
                    elif ">t" in data:
                        print("send msg")
                        sendMSG(channel, 'Text command')
                        testcommand()

        except ConnectionAbortedError:
            print("Connection to Server lost. Try reconnecting.")
            reconnect()

except KeyboardInterrupt:
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()