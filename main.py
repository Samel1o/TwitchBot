import time

from setup import *

allowed_operators = ["treeed", "same1lo"]

def username_in_list(allowed_operators, username):
    return username in allowed_operators

def echo_command(data, username):
    print(">echo got called")
    start_index = data.find(">echo") + len(">echo") + 1
    end_index = data.find("\r\n")
    message_to_echo = data[start_index:end_index]
    time.sleep(1)
    irc.send(
        f"PRIVMSG {channel} :{username} send the message: {message_to_echo}\r\n".encode("utf-8"))

def exit_command():
    print(">exit got called")
    irc.send(
        f"PRIVMSG {channel} :The bot is quitting....\r\n".encode("utf-8"))
    time.sleep(5)
    irc.close()
    exit()
    
def calc_command(data,channel):
    print(">calculate got called")
    start_index = data.find(">calc") + len(">calc") + 1
    end_index = data.find("\r\n")
    calculation = data[start_index:end_index]
    try:
        answer = eval(calculation)
    except:
        answer = "ERROR"
    time.sleep(1)
    irc.send(
        f"PRIVMSG {channel} :Calc got called with calculation: {calculation} and the answer is {answer}\r\n".encode("utf-8"))
    
def reload_command(channel):
    print(">reload got called")
    irc.send(
        f"PRIVMSG {channel} :reloading...\r\n".encode("utf-8"))
    time.sleep(1)
    restart()

def op_command(data,operators,channel, allowed_operators):
    print(">op got called")
    start_index = data.find(">op") + len(">op") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")
   
    if argList[0] == "list":
        time.sleep(0.2)
        irc.send(f"PRIVMSG {channel} :Op'ed users are {operators}\r\n".encode("utf-8"))

    elif argList[0] == "add":
        if len(argList) == 2 and username_in_list(allowed_operators, argList[1]):
            operators.append(argList[1])
            time.sleep(0.2)
            irc.send(f"PRIVMSG {channel} :Opperating user: {argList[1]} added successfully.\r\n".encode("utf-8"))
        else:
            irc.send(f"PRIVMSG {channel} :Invalid op command format. Usage: >op add [user]\r\n".encode("utf-8"))
    elif argList[0] == "remove":
        if len(argList) == 2 and username_in_list(allowed_operators, argList[1]):
            if argList[1] in operators:
                print(f"Operator {argList[1]} found in the list.")
                if argList[1] not in ["treeed", "same1lo"]:
                    operators.remove(argList[1])
                    time.sleep(0.2)
                    irc.send(f"PRIVMSG {channel} :Opperating user: {argList[1]} removed successfully.\r\n".encode("utf-8"))
                else:
                    print(f"Operator {argList[1]} cannot be removed as an operator.")
                    irc.send(
                        f"PRIVMSG {channel} :{username} you cannot remove this user as an operator.\r\n".encode("utf-8"))  
            else:
                print(f"Operator {argList[1]} not found in the list.")
                time.sleep(0.2)               #TODO Schauen, warum diese Anweisung nicht ausgeführt wird, obwohl der Nutzer nicht in der Liste operator ist.
                irc.send(f"PRIVMSG {channel} :Opperating user: {argList[1]} not found in the list.\r\n".encode("utf-8"))
        else:
            irc.send(f"PRIVMSG {channel} :Invalid op command format. Usage: >op remove [user]\r\n".encode("utf-8"))  
    elif argList[0] == "":
        time.sleep(0.2)
        irc.send(
            f"PRIVMSG {channel} :Invalid op command format. Usage: >op [add/list/remove] [user]\r\n".encode("utf-8"))

    else:
         print(f"Unknown error occurred for operator {argList[1]}.")
         irc.send(
             f"PRIVMSG {channel} :{username} an unknown error occurred, please contact the support!\r\n".encode("utf-8"))

def help_command(channel):
    print(">help got called")
    time.sleep(1)
    irc.send(
        f"PRIVMSG {channel} :>exit exits, >echo [args] echos, >help prints this, >op [user] op's the user, >op view views the op'ed, >calc [args] calculates\r\n".encode(
            "utf-8"))

def userlist_command(data,channel):
    if "PRIVMSG" in data:
        print(">userlist got called")
        user_index_start = data.find(":") + 1
        user_index_end = data.find("!")
        username = data[user_index_start:user_index_end]
        userlist = username.strip()
        time.sleep(0.5)
        irc.send(f"PRIVMSG {channel} :Die aktuellen Benutzer im Chat sind: {userlist}\r\n".encode("utf-8"))

def troll_command(data, channel): #TODO diesen Command sollen nur Moderatoren des jeweiligen Channels ausführen können, bzw. wir beide halt.
    start_index = data.find(">troll") + len(">troll") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    arg_list = arg.split(" ")
    
    if len(arg_list) == 2:
        target_user = arg_list[0]
        num_messages = int(arg_list[1])
        if num_messages <= 25:
            try:
                for a in range(num_messages):
                    irc.send(f"PRIVMSG {channel} :{target_user} :tf: 🔔\r\n".encode("utf-8"))

                    if a % 20 == 0:
                        time.sleep(2)
                    else:
                        time.sleep(0.02)

            except ValueError:
                irc.send(f"PRIVMSG {channel} :Invalid number of messages.\r\n".encode("utf-8"))
        else:
            irc.send(f"PRIVMSG {channel} :{username} for now the Bot is only abled to troll for a maximum amount of 25.\r\n".encode("utf-8"))
            
    else:
        irc.send(f"PRIVMSG {channel} :Invalid troll command format. Usage: >troll [target_user] [num_messages]\r\n".encode("utf-8"))

def reconnect():
    irc.close()
    time.sleep(5)
    irc.connect((server,port))

    irc.send(f"PASS {os.getenv("oauth_token")}\r\n".encode("utf-8"))
    irc.send(f"NICK {bot_username}\r\n".encode("utf-8"))
    irc.send(f"JOIN {channel}\r\n".encode("utf-8"))     





irc.send(f"PRIVMSG {channel} :JannikSamsonBot started\r\n".encode("utf-8"))

    
try:
    while True:
        try:
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
                            echo_command(data, username)
                        elif ">userlist" in data:    
                            userlist_command(data,channel)  
                        elif ">exit" in data:
                            exit_command()
                        elif ">calc" in data:
                            calc_command(data, channel)
                        elif ">reload" in data:
                            reload_command(channel)
                        elif ">op" in data:
                            op_command(data, operators, channel, allowed_operators)
                        elif ">troll" in data:
                            troll_command(data,channel)
                        elif ">help" in data:
                            help_command(channel)

        except ConnectionAbortedError:
            print("Connection to Server lost. Try reconnecting.")
            reconnect()
                

except KeyboardInterrupt:
    irc.send("QUIT\r\n".encode("utf-8"))
    irc.close()
    exit()