# listOfUser = [
# 	('Kumar', '99252 26212'),
# 	('Sharvan', '+919925226212'),
# 	('Rahul', '+9925226212'),
# 	('Ravi', '919925226212'),
# 	('Test', '09925226212'),
# 	('Ronak', '9925226212'),
# ]

# # print(listOfUser)

# for x in listOfUser:
# 	print(x[0])
# 	new = x[1].replace(" ", "")
# 	print(new)

# exit();


# from twilio.rest import Client

# from env import getAllKeys


# account_sid = getAllKeys['ACCOUNT_SID']
# auth_token = getAllKeys['AUTH_TOKEN']


# client = Client(account_sid, auth_token)


# message = client.messages \
#                 .create(
#                      body="Hello Kumar",
#                      from_='+17122143232',
#                      to=x
#                  )
# print(message.sid)
