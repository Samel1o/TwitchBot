from setup import *
import math

def calc_command(data, username):
    start_index = data.find(">calc") + len(">calc") + 1
    end_index = data.find("\r\n")
    calculation = data[start_index:end_index]

    try:
        allowed_functions = ['']

        if calculation in allowed_functions:
            calculation = calculation.replace(f'{func}(', f'math.{func})')

        answer = eval(calculation)
    except Exception as e:
        answer = f"ERROR: {str(e)}"

    time.sleep(waitTime)
    
    sendMSG(channel, f"@{username} > {calculation} = {answer}")