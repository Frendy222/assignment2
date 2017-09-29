print('Input in a, b, or c ')
data_input = input('Input :')
data = data_input.lower()
list_data = list(data)
out = [1,0,0]
i=0

def typeA():
    x=out[0]
    y=out[1]
    z=out[2]
    out.remove(x)
    out.remove(y)
    out.insert(0,y)
    out.insert(1,x)
def typeB():
    x=out[0]
    y=out[1]
    z=out[2]
    out.remove(y)
    out.remove(z)
    out.insert(1,z)
    out.insert(2,y)
def typec():
    x=out[0]
    y=out[1]
    z=out[2]
    out.remove(x)
    out.remove(z)
    out.insert(0,z)
    out.insert(2,x)

for letter in list_data:
    if letter == 'a':
        typeA()
    elif letter == 'b':
        typeB()
    elif letter == 'c':
        typec()
    else :
        end = 'Error!!'
x=out[0]
y=out[1]
z=out[2]

if x == 1:
    end=1
elif y == 1:
    end=2
elif z==1:
    end=3
print(end)
