import mysql.connector


def login(username, password):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM user where username='" + username + "' and password ='" + password + "'")

  myresult = mycursor.fetchall()

  print(len(myresult))

  if(len(myresult)>0):
    return "Success"
  else:
    return "Failure"


def addUser(name,phone,email,username,password):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO user (userid, name, phone,email,username,password) VALUES (%s, %s,%s, %s,%s, %s)"
  val = ("1111", "Highway 21","John", "Highway 21","John", "Highway 21")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  if((mycursor.rowcount)>0):
    return "Success"
  else:
    return "Failure"


def ingest_nmap(reportid):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO nmap (reportid, status) VALUES (%s, %s)"
  val = (reportid, "Completed")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted into nmap.")


def ingest_owasp_zap(reportid):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO owasp_zap (reportid, status) VALUES (%s, %s)"
  val = (reportid, "Completed")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted into owasp_zap.")

def ingest_nikto(reportid):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO nikto (reportid, status) VALUES (%s, %s)"
  val = (reportid, "Completed")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted into nikto.")


def ingest_wapiti(reportid):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO wapiti (reportid, status) VALUES (%s, %s)"
  val = (reportid, "Completed")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted into wapiti.")



def createReport(userid):
  mydb = mysql.connector.connect(
    host="sql4.freemysqlhosting.net",
    user="sql4406256",
    password="Lxilmq4gJG",
    database="sql4406256"
  )

  print(mydb)
  mycursor = mydb.cursor()

  sql = "INSERT INTO reportm (userid, status) VALUES (%s, %s)"
  val = (userid, "In Progress")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  if ((mycursor.rowcount) > 0):
     print("Success")
  else:
    print("Failure")

  mycursor.execute("SELECT max(reportid) from reportm")

  myresult = mycursor.fetchall()

  print(myresult[0])

  strout = str(myresult[0])

  strout = strout[1::]

  strout = strout[:-1:]
  strout = strout[:-1:]

  return strout





print(createReport('12345'))

#print(login('John','Highway21'))
#print(addUser('Suman','11111111','aa@gmail.com','usr123','123abc'))

