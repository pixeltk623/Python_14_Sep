personList = [
	('Kumar', '99252 26212'),
	('Sharvan', '+919925226212'),
	('Rahul', '+9925226212'),
	('Ravi', '919925226212'),
	('Test', '09925226212'),
	('Ronak', '9925226212'),
]
# personList  = ["+919925226212","919925226212","9925226212","99252 26212","09925226212"]

newList = []

for x in personList:
    # print(x[1][1])
    
    if len(x[1])== 10:
        newList.append((x[0],"+91"+x[1]))
    elif x[1][:2] == "91" and len(x[1])==12:
        num  = x[1].replace("91","+91")
        newList.append((x[0],num))
    elif len(x[1]) == 13 and x[1][0:3] =="+91":
        newList.append((x[0],x[1]))
    elif len(x[1])==11 and x[1][0]=="+":
        num  = x[1].replace("+","+91")
        newList.append((x[0],num))
    elif len(x[1])==11 and x[1][0]!="0":
        num = x[1].replace(" ","")
        newList.append((x[0],"+91"+num))
    elif len(x[1])==11 and x[1][0]=="0":
        num = x[1].replace("0","+91")
        newList.append((x[0],num))
    


from twilio.rest import Client

from keys import getAllKeys


account_sid = getAllKeys['ACCOUNT_SID']
auth_token = getAllKeys['AUTH_TOKEN']


client = Client(account_sid, auth_token)

for x in newList:
    message = client.messages \
                    .create(
                        body=x[0]+"Hello !!",
                        from_='+17122143232',
                        to=x[1]
                    )
    print(message.sid)
