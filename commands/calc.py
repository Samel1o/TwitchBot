from setup import *

def calc_command(data,channel):
    print(">calculate got called")
    start_index = data.find(">calc") + len(">calc") + 1
    end_index = data.find("\r\n")
    calculation = data[start_index:end_index]
    try:
        answer = eval(calculation)
    except:
        answer = "ERROR"
    time.sleep(waitTime)
    irc.send(
        f"PRIVMSG {channel} :{calculation}={answer}\r\n".encode("utf-8"))
    