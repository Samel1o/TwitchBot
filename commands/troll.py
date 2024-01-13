from setup import *

def troll_command(data, channel, username): #TODO diesen Command sollen nur Moderatoren des jeweiligen Channels ausführen können, bzw. wir beide halt.
    start_index = data.find(">troll") + len(">troll") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    arg_list = arg.split(" ")

    if len(arg_list) == 2:
        target_user = arg_list[0]
        try:
            num_messages = int(arg_list[1])
        except:
            num_messages = 2

        if num_messages <= 25:
            try:
                for a in range(num_messages):
                    irc.send(f"PRIVMSG {channel} :{target_user} :tf: 🔔\r\n".encode("utf-8"))

                    if a % 20 == 0:
                        time.sleep(2)
                    else:
                        time.sleep(0.02)

            except ValueError:
                irc.send(f"PRIVMSG {channel} :Invalid number of messages.\r\n".encode("utf-8"))
        else:
            irc.send(f"PRIVMSG {channel} :{username} for now the Bot is only abled to troll for a maximum amount of 25.\r\n".encode("utf-8"))

    else:
        irc.send(f"PRIVMSG {channel} :Invalid troll command format. Usage: >troll [target_user] [num_messages]\r\n".encode("utf-8"))