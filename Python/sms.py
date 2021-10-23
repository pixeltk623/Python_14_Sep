from twilio.rest import Client

from env import getAllKeys


account_sid = getAllKeys['ACCOUNT_SID']
auth_token = getAllKeys['AUTH_TOKEN']


client = Client(account_sid, auth_token)


listOffNumber = ["+918780237219", "+919925226212", "+916352007588", "+917487009183"]

# print(listOffNumber)

# exit()


for x in listOffNumber:
	message = client.messages \
	                .create(
	                     body="Hello Kumar",
	                     from_='+17122143232',
	                     to=x
	                 )
	print(message.sid)
