from setup import *


try:
    while True:
        data = irc.recv(4096).decode("utf-8")

        if data:
            print(data, end="")

            user_index_start = data.find(":") + 1
            user_index_end = data.find("!")
            username = data[user_index_start:user_index_end]
    
            if data.startswith("PING"):
                irc.send("PONG\r\n".encode("utf-8"))
                print("PING / PONG")

            if username in ["same1lo", "Treeed"]:
                if ">echo" in data:
                    start_index = data.find(">echo") + len(">echo") + 1
                    end_index = data.find("\r\n")
                    message_to_echo = data[start_index:end_index]

                    time.sleep(1)

                    irc.send(f"PRIVMSG {channel} :{username} send the message: {message_to_echo}\r\n".encode("utf-8"))

                if ">exit" in data:
                    irc.send("QUIT\r\n".encode("utf-8"))
                    irc.close()
                    exit()
                if ">calc" in data:
                    start_index = data.find(">calc") + len(">calc") + 1
                    end_index = data.find("\r\n")
                    calculation = data[start_index:end_index]
                    print(">calculate got called")
                    try:
                        answer = eval(calculation)
                    except:
                        answer = "ERROR"
                    time.sleep(1)
                    irc.send(f"PRIVMSG {channel} :Calc got called with the calculation: {calculation} and the answer is {answer}\r\n".encode("utf-8"))

                    if ">restard" in data:
                        pass
        else:
            pass
except KeyboardInterrupt:
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()
