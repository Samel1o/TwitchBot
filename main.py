import time
from setup import *

from commands.test import testcommand
from commands.calc import calc_command
from commands.echo import echo_command
from commands.exit import exit_command
from commands.reload import reload_command
from commands.op import *
from commands.help import help_command
from commands.troll import troll_command
from commands.sendto import send_command
from commands.todo import todo_command

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

                if data.startswith("PING"): irc.send("PONG\r\n".encode("utf-8"))


                if username in operators:
                    if ">echo" in data:
                        echo_command(data, username)
                    elif ">exit" in data:
                        exit_command()
                    elif ">calc" in data:
                        calc_command(data, username)
                    elif ">reload" in data:
                        reload_command()
                    elif ">op" in data:
                        op_command(data, operators, username)
                    elif ">troll" in data:
                        troll_command(data, username)
                    elif ">help" in data:
                        help_command(username)
                    elif ">sendto" in data:
                        send_command(data)
                    elif ">todo" in data:
                        todo_command(data)

        except ConnectionAbortedError:
            print("Connection to Server lost. Try reconnecting.")
            reconnect()

except KeyboardInterrupt:
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()