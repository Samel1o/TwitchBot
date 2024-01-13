import setup

def send_command(data):
    setup.sendMSG(setup.channel, f"{data}")