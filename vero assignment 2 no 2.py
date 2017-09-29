list_data = []
i = 1
out = []
yeah = 0
while i<11:
    data = int(input('Input :'))
    list_data.append(data)
    i += 1
for nom in list_data:
    ak = nom%42
    out.append(ak)
end = set(out)
for k in end:
    yeah += 1
print(yeah)
