from setup import *

def echo_command(data, username):
    start_index = data.find(">echo") + len(">echo") + 1
    end_index = data.find("\r\n")
    message_to_echo = data[start_index:end_index]
    time.sleep(waitTime)
    sendMSG(channel, f"{username} send the message: {message_to_echo}")
