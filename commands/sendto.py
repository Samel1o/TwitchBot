import setup

def send_command(data):
    setup.sendMSG(setup.channel, f"{data}")

    start_index = data.find(">sendto") + len(">sendto") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")
    
    setup.sendMSG(f"#{argList[0]}", " ".join(argList[1:]))