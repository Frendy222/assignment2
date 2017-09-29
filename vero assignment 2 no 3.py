print('Please input in integer!!')
data = int(input('Input :'))
check = data%2
out = 0

if check == 1:
    out = 'Alice'
elif check == 0:
    out = 'Bob'
else :
    out = 'Error !!'
print(out)
