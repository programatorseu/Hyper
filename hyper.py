msg_0 = "Enter an equation "
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0
result = 0

def wiadomosc(msg_index):
    if msg_index == 10:
            msg_text = "Are you sure? It is only one digit! (y / n)"
    elif msg_index == 11:
        msg_text = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif msg_index == 12:
        msg_text = "Last chance! Do you really want to embarrass yourself? (y / n)"

    return msg_text


def check_input(input):
    val = ""
    try:
        val = float(input)
    except ValueError:
        val = "Error"     
    finally:
        return val
    
def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def is_one_digit(v):
    if is_integer_num(v) and v > -10 and v < 10:
        return True
    else:
        return False

# message list

def message(msg_index_value):
    if msg_index_value == 0:
        msg_text = "Enter an equation"
    elif msg_index_value == 1:
        msg_text = "Do you even know what numbers are? Stay focused!"
    elif msg_index_value == 2:
        msg_text = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif msg_index_value == 3:
        msg_text = "Yeah... division by zero. Smart move..."
    elif msg_index_value == 4:
        msg_text = "Do you want to store the result? (y / n):"
    elif msg_index_value == 5:
        msg_text = "Do you want to continue calculations? (y / n):"
    elif msg_index_value == 6:
        msg_text = " ... lazy"
    elif msg_index_value == 7:
        msg_text = " ... very lazy"
    elif msg_index_value == 8:
        msg_text = " ... very, very lazy"
    elif msg_index_value == 9:
        msg_text = "You are"
    elif msg_index_value == 10:
        msg_text = "Are you sure? It is only one digit! (y / n)"
    elif msg_index_value == 11:
        msg_text = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif msg_index_value == 12:
        msg_text = "Last chance! Do you really want to embarrass yourself? (y / n)"

    return msg_text


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
            msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg

    return msg




while True:
    while True:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        if x == 'M':
                x = memory
        if y == 'M':
                y = memory
        try:
            x,y = float(x), float(y)
        except:
            print(msg_1)            
        if (oper == "+") or (oper == "-") or (oper == "*") or (oper == "/"):
            print(check(x,y,oper))
            if oper == "+":
                    result = float(x) + float(y)
                    break
            elif oper == "-":
                    result = x - y
                    break
            elif oper == "*":
                    result = x * y
                    break
            else:
                if(oper == "/") and (y == 0):
                    print(msg_3)
                    continue
                else:
                    result = x / y 
                    break
        else:
            print(msg_2)
    print(result)
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(wiadomosc(msg_index))
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue        
            else:
                memory = result 
            break
        elif answer == 'n':
            break    
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            break
        elif answer == 'n':
            exit(0)        
                                   
