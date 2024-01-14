from setup import *

def todo_command(data):
    start_index = data.find(">todo") + len(">todo") + 1
    end_index = data.find("\r\n")
    arg = data[start_index:end_index]
    argList = arg.split(" ")

    if argList[0] == "add":
        time.sleep(waitTime)
        message = ' '.join(argList[1:])
        
    
        with open(r"todo.md", "a+") as f:
            
            global count
            
            count = str(f).count("-")
            
            f.write(f"- [ ] {count}. {message}\n")

    sendMSG(channel, f"{count}. {message}")
        
    if argList[0] == "list":
        time.sleep(waitTime)
        sendMSG(channel, "Test 123")
    
    if argList[0] == "toggle":
        time.sleep(waitTime)
        sendMSG(channel, "Test check")
        
    