def do_flat(l):
    l_temp=[]
    for i in range(len(l)):
        if type(l[i]) == list:
            l_temp.extend(do_flat(l[i]))
        else:
            l_temp.append(l[i])
    return l_temp

def convert(l):
    l_temp=[]
    for i in range(len(l)):
        k=(len(l)-1)-i
        if type(l[k]) == list:
            l_temp.append(convert(l[k]))
        else:
            l_temp.append(l[k])
    return l_temp

l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

liste=[[1, 2], [3, 4], [5, 6, 7]]

flattened = do_flat(l)

converted = convert(liste)

print(l)
print("flattened list")
print("---------------------------")
print(flattened)

print("***************************")

print(liste)
print("converted list")
print("---------------------------")
print(converted)



