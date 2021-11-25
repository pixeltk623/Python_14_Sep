import datetime

# print(datetime)

# print(dir(datetime))


#currentDateAndTime = datetime.datetime.now()

#todayDate = datetime.date.today()

# print(todayDate)

# print(currentDateAndTime)

# a = "5465asdas4"

# print(a.isnumeric())

# aString = "0121"
# print(aString.startswith("1"))

# exit()

# year = input("Enter The Year: ")
# month = input("Month: ")
# day = input("Day: ")

# #userDate = datetime.date(2021,11,11)


# if year.isnumeric() and year!='':
# 	if len(year)==4 and year.startswith("0") != True:
# 		print(year)
# 	else:
# 		print("Length Issue")
# else:
# 	print("Enter Valid Year")


# if month!='':
# 	if month.isnumeric() and (int(month)>0 and int(month)<=12):
# 		print(month)
# 	else:
# 		print("Enter Valid Month")

# else:
# 	print("Month Can Not be blank")

# if day!='':
# 	if day.isnumeric() and (int(day)>0 and int(day)<=31):
# 		print(day)
# 	else:
# 		print("Enter Valid Day")

# else:
# 	print("Day Can Not be blank")


# if (year.isnumeric() and year!='' and len(year)==4 and year.startswith("0") != True) and (month.isnumeric() and (int(month)>0 and int(month)<=12)) and (day.isnumeric() and (int(day)>0 and int(day)<=31)):
# 	userDate = datetime.date(int(year),int(month),int(day))
# 	print(userDate)
# else:
# 	print("Galat Hai")


from datetime import date

# userDate = date(2021,11,11)

# print(userDate)

# print(date.today())

# timestamp = date.fromtimestamp(1637674256)

# print(timestamp)

# today = date.today()

# print(today) # 2021-01-01

# print(today.year)
# print(today.month)
# print(today.day)

from datetime import time

# a = time(19,10,15,454646)

# t = time(hour=19, minute=15,second=56,microsecond=54546)

# print(t)

# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# print(datetime.datetime.now())


from datetime import datetime

# t = datetime(2021,5,10,11,52,52,2365)

# print(t.year)
# print(t.month)
# print(t.day)

# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)
# print(a)


# t1 = datetime(year=2021,month=12,day=31)
# t2 = datetime(year=2022,month=1,day=1)

# t3 = t2-t1

# print(t3)


from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 0, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 1, minutes = 4, seconds = 54)

# t3 = t1 - t2

# print(t3)

# now = datetime.now()

# print(now.strftime("%H:%M:%S"))


# s1 = now.strftime("%Y-%m-%d, %H:%M:%S")

# print(s1)

# date_string = "21 June, 2018"
# print("date_string =", date_string)


# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# import pytz

# print("--Local Time-----")

# print(datetime.now())

# nzTimeZone = pytz.timezone('America/New_York')

# print(datetime.now(nzTimeZone))


# Europe = pytz.timezone('Asia/Karachi')

# print(datetime.now(Europe))