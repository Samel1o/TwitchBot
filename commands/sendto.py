import setup

def send_command(data):
<<<<<<< HEAD
    setup.sendMSG(setup.channel, f"{data}")
=======
    setup.sendMSG(setup.channel, f"{data}")

    start_index = data.find(">sendto") + len(">sendto") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")


    setup.sendMSG(setup.channel, f"{argList}")

    setup.sendMSG(f"#{argList[0]}", argList[1])
>>>>>>> 331cde5ee36898cea8288aa9c22d8ee2d11b392f
