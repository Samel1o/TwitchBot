from setup import *

def troll_command(data, username): #TODO diesen Command sollen nur Moderatoren des jeweiligen Channels ausführen können, bzw. wir beide halt.
    start_index = data.find(">troll") + len(">troll") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    arg_list = arg.split(" ")

    target_user = arg_list[0]
    num_messages = int(arg_list[1])
    
    if num_messages < 25:
        for i in range(num_messages):
            sendMSG(channel, f"@{target_user} troll :tf:")
            
    else:
        for i in range(5):
            sendMSG(channel, f"@{username} troll :tf:")
        