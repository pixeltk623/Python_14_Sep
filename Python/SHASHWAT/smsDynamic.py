personList  = ["+919925226212","919925226212","9925226212","99252 26212","09925226212"]
newList = []
for x in personList:
    # print(x)
    
    if len(x)== 10:
        newList.append("+91"+x)
    elif x[:2] == "91" and len(x)==12:
        num  = x.replace("91","+91")
        newList.append(num)
    elif len(x) == 13 and x[0:3] =="+91":
        newList.append(x)
    elif len(x)==11 and x[0]!="0":
        num = x.replace(" ","")
        newList.append("+91"+num)
    elif len(x)==11 and x[0]=="0":
        num = x.replace("0","+91")
        newList.append(num)

for x in newList:
    print(x)

