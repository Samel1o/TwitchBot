from setup import *

def echo_command(data, username):
    print(">echo got called")
    start_index = data.find(">echo") + len(">echo") + 1
    end_index = data.find("\r\n")
    message_to_echo = data[start_index:end_index]
    time.sleep(waitTime)
    irc.send(
        f"PRIVMSG {channel} :{username} send the message: {message_to_echo}\r\n".encode("utf-8"))
    