name = input("Input here :")
formlist = list(name)
i = 0
out = []
out.append(formlist[0])
for x in formlist :
    if x == '-':
        add = i +1
        push = (formlist[add])
        out.append(push)
    i += 1
print(''.join(out).upper())
