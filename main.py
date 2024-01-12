import time

from setup import *

irc.send(f"PRIVMSG {channel} :JannikSamsonBot started\r\n".encode("utf-8"))

try:
    while True:
        data = irc.recv(4096).decode("utf-8")

        user_index_start = data.find(":") + 1
        user_index_end = data.find("!")
        username = data[user_index_start:user_index_end]
        if username != "":
            if data:
                print(data, end="")

                if data.startswith("PING"):
                    irc.send("PONG\r\n".encode("utf-8"))
                    print("PING / PONG")

                if username in operators:
                    if ">echo" in data:
                        start_index = data.find(">echo") + len(">echo") + 1
                        end_index = data.find("\r\n")
                        message_to_echo = data[start_index:end_index]

                        time.sleep(1)

                        irc.send(
                            f"PRIVMSG {channel} :{username} send the message: {message_to_echo}\r\n".encode("utf-8"))

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
                        irc.send(
                            f"PRIVMSG {channel} :Calc got called with the calculation: {calculation} and the answer is {answer}\r\n".encode(
                                "utf-8"))

                    if ">reload" in data:
                        irc.send(
                            f"PRIVMSG {channel} :reloading...\r\n".encode(
                                "utf-8"))
                        time.sleep(1)
                        restart()

                    if ">op" in data:
                        start_index = data.find(">op") + len(">op") + 1
                        end_index = data.find("\r\n")
                        arg = data[start_index:end_index]

                        print(">op got called")

                        argList = arg.split(" ")
                        irc.send(f"PRIVMSG {channel} :Op call with args {argList}\r\n".encode("utf-8"))


                        if argList[0] == "list":
                            time.sleep(1)
                            irc.send(f"PRIVMSG {channel} :Op'ed users are {operators}\r\n".encode("utf-8"))

                        if argList[0] == "add":
                            operators += argList[1]
                            time.sleep(1)
                            irc.send(f"PRIVMSG {channel} :Opperating user: {argList[1]}, did not succsede why i dont now\r\n".encode("utf-8"))

                    if ">help" in data:
                        print("Help comand got called")
                        time.sleep(1)
                        irc.send(
                            f"PRIVMSG {channel} :>exit exits, >echo [args] echos, >help prints this, >op [user] op's the user, >op view views the op'ed, >calc [args] calculates\r\n".encode(
                                "utf-8"))

        else:
            pass
except KeyboardInterrupt:
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()
