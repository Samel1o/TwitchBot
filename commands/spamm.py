from setup import *

def spamm_command(data):
    start_index = data.find(">spamm") + len(">spamm") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")
    
    for x in range(int(argList[0])):
        sendMSG(channel, f"{x+1} {str(' '.join(argList[2:]))}")
        time.sleep(int(argList[1]))
