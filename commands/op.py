from setup import *

def op_command(data,operators,channel, allowed_operators, username):
    print(">op got called")

    start_index = data.find(">op") + len(">op") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")

    sendMSG(channel, f"{arg}, {argList}, {username}")
    if argList[0] == "list":
        time.sleep(waitTime)
        sendMSG(channel, f"Op'ed users are {operators}")

    if argList[0] == "add":

        sendMSG(channel, f"add called {len(argList)} {username_in_list(allowed_operators, argList[1])}")

        if username_in_list(allowed_operators, username):
            operators += argList[1]
            allowed_operators += argList[1]
            time.sleep(waitTime)
            sendMSG(channel, f"Opperating user: {argList[1]} added successfully.")
        else:
            sendMSG(channel, f"Invalid op command format. Usage: >op add [user]")


'''
try:
    if argList[0] == "add":

        sendMSG(channel, f"add called {len(argList)} {username_in_list(allowed_operators, argList[1])}")
        if len(argList) == 2 and username_in_list(allowed_operators, argList[1]):
            operators += argList[1]
            allowed_operators += argList[1]
            time.sleep(0.2)
            sendMSG(channel, f"Opperating user: {argList[1]} added successfully.")
        else:
            sendMSG(channel, f"Invalid op command format. Usage: >op add [user]")
except:
    sendMSG(channel, f"Pleas provide an argument")

if argList[0] == "remove":
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
        f"PRIVMSG {channel} :Invalid op command format. Usage: >op [add/list/remove] [user]\r\n".encode("utf-8"))'''

'''else:
    try:
        print(f"Unknown error occurred for operator {argList[1]}.")
    except:
        print("No argument was provided")
    irc.send(
        f"PRIVMSG {channel} :{username} an unknown error occurred, please contact the support!\r\n".encode("utf-8"))'''
    