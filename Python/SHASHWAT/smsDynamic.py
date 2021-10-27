personList  = ["+919925226212","919925226212","9925226212","99252 26212"]
newList = []
for x in personList:
    # print(x)
    
    if len(x)== 10:
        newList.append("+91"+x)
    elif x[0:2] == "91":
        num  = x.replace("91","+91")
        newList.append(x)
    elif len(x) == 13 and x[0:3] =="+91":
        newList.append(x)

print(newList)

