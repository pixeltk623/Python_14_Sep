import mysql.connector

# print(mysql.connector)


# localhost
# root
# ""
# python_14_sep

# conn = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = ""
# )

conn = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "api_db"
)

myCursor = conn.cursor()

# query = "SELECT e.e_id AS id, e.name AS name  FROM employees AS e"

# myCursor.execute(query)

# myresult = myCursor.fetchall()


# print(myresult)

# query = "[INSERT INTO `employees`(`name`, `email`, `gender`, `Address`, `dob`) \
#  VALUES ('skumar','asdsa','male','test','2021-10-10')]";

# queryMain = "INSERT INTO employees (name, email, gender, Address, dob) VALUES (%s,%s,%s,%s,%s)"

# values = [
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10'],
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10'],
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10'],
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10'],
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10'],
# 		['Sharvan','Sharvan','Sharvan','Sharvan','2020-10-10']
# 	]



# myCursor.executemany(queryMain, values)
# conn.commit()

# myCursor.execute(query)
# conn.commit()
# print(myCursor.rowcount, "record inserted.")
# print(myCursor.lastrowid)

# myCursor.execute(query)
# conn.commit()


# for x in query:
# 	myCursor.execute(x)
# 	conn.commit()

	#print(x)

# print(conn)

# print(myCursor)


query = "SELECT WORKING_AREA , COUNT(AGENT_CODE) FROM `agents` GROUP BY WORKING_AREA";
myCursor.execute(query)

myresult = myCursor.fetchall()


print(myresult)

Django 
PHP 
LARAVEL 
Express
Node 
Java => spring

CRUD 


