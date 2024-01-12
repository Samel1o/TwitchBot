from setup import *

while True:
    data = irc.recv(4096).decode("utf-8")
    print(data)

    user_index_start = data.find(":") + 1
    user_index_end = data.find("!")
    username = data[user_index_start:user_index_end]
    
    if data.startswith("PING"):
        irc.send("PONG\r\n".encode("utf-8"))
        print("PING / PONG")


    if username == "same1lo":
        if ">exit" in data:
            irc.send("QUIT\r\n".encode("utf-8"))
            irc.close()
            exit()

    # Check if the message contains ">echo" and extract the message
    if username in ["#####", "#####", "#####", "#####", ]:
        if ">echo" in data:
            start_index = data.find(">echo") + len(">echo") + 1
            end_index = data.find("\r\n")
            message_to_echo = data[start_index:end_index]

            time.sleep(1)
            
            irc.send(f"PRIVMSG {channel} :{username} send the message: {message_to_echo}\r\n".encode("utf-8"))