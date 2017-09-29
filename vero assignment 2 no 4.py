print('Input in a, b, or c ')
data_input = input('Input :')
data = data_input.lower()
list_data = list(data)
out = 1

for letter in list_data:
    if letter == "a" :
       if out == 1 :
           out += 1
       elif out == 2:
           out -= 1
       else :
           out = 'error a'

    elif letter == 'b' :
        if out == 2 :
           out += 1
        elif out == 3 :
            out -= 1
        else :
            out = "error b"
    elif letter == 'c' :
        if out == 1 :
           out += 2
        elif out == 3 :
            out -= 2
        else:
            out = "error c"
    else :
        out = 'error input'

print(out)
