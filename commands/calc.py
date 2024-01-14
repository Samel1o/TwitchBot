import setup

def calc_command(data, username):
    start_index = data.find(">calc") + len(">calc") + 1
    end_index = data.find("\r\n")
    calculation = data[start_index:end_index]

    setup.time.sleep(setup.waitTime)
    
    try:
        answer = eval(f"1+{calculation}-1")
    except:
        answer = "Error"
    
    setup.sendMSG(setup.channel, f"@{username} > {calculation} = {answer}")
    
    