from setup import *

def send_command(data):
    start_index = data.find(">sendto") + len(">sendto") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")
    
    send_to_channel = argList[0]
    
    sendMSG(f"#{send_to_channel}", str(' '.join(argList[1:])))