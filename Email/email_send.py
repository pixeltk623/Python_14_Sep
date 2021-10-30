# # import smtplib, ssl

# # smtp_server = "smtp.gmail.com"
# # port = 587  # For starttls
# # sender_email = "dream.sharvan@gmail.com"
# # password = input("Type your password and press enter: ")

# # # Create a secure SSL context
# # context = ssl.create_default_context()

# # # Try to log in to server and send email
# # try:
# #     server = smtplib.SMTP(smtp_server,port)
# #     server.ehlo() # Can be omitted
# #     server.starttls(context=context) # Secure the connection
# #     server.ehlo() # Can be omitted
# #     server.login(sender_email, password)

# #     server.sendmail(sender_email, "sharvan.kumar@tops-int.com", "Hello")

# #     # TODO: Send email here
# # except Exception as e:
# #     # Print any error messages to stdout
# #     print(e)
# # finally:
# #     server.quit()


# import os
# import sendgrid
# from sendgrid.helpers.mail import Content, Email, Mail

# sg = sendgrid.SendGridAPIClient(
#     apikey=os.environ.get("SENDGRID_API_KEY")
# )
# from_email = Email("my@gmail.com")
# to_email = Email("your@gmail.com")
# subject = "A test email from Sendgrid"
# content = Content(
#     "text/plain", "Here's a test email sent through Python"
# )
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())

# # The statements below can be included for debugging purposes
# print(response.status_code)
# print(response.body)
# print(response.headers)

# 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

# Banner

# Post


# Offers 
	


# Free 

# 1 st day 

# Google my business

# Facebook 

# Instagram 

# Payment

# 1 week 


# 400

# 2 Post => 300

# 15K

# 50k

# indian grocery




listOfEmail = ["sharvank1515@gmail.com","sharvank1515@gmail.com","sharvank1515@gmail.com","sharvank1515@gmail.com"];

import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key="")

for x in range(1,2):
	

	from_email = Email("info@pixeltk.com")
	to_email = To("shashwatgupta591@gmail.com")
	cc_email = Email("sharvank1515@gmail.com")
	p = Personalization()
	p.add_to(to_email)
	p.add_cc(cc_email)
	subject = "Sending with SendGrid is Fun"
	content = Content("text/html", '''<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<style type="text/css">
			button {
				background-color: red;
				color: white;
				border: none;
				padding: 10px 20px;
			}
		</style>
	</head>
	<body>
		<p>Hey {name},</p>

		<p>As you are thinking too much about your own career. Let me just make it super easier for you.</p>

		<p style="background-color: rgb(255,242,204);">Let's do it for <b>?450</b> for you to learn <b>India's most Trending Digital Marketing Course</b> and start it seriously from today.</p>

		<p>It is just a 2 minutes opening. And will never come back in this entire life.</p>

		<center><button>Your 2 Minutes Start Here</button></center>
	</body>
	</html>''')
	mail = Mail(from_email, to_email, subject, content)
	mail.add_personalization(p)
	response = sg.client.mail.send.post(request_body=mail.get())
#print(mail)


print(response.status_code)
print(response.body)
print(response.headers)