import mysql.connector
from mysql.connector import errorcode

name ="gffghf"
email_address = "gdfgdfgdfgfgd"

try:

        cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='testingdatabase')

        query = "INSERT INTO users(name,email_address) " \
                "VALUES(%s,%s)"
        #
        
        if cnx.is_connected():
            print('Connected to MySQL database')
        args = (name, email_address)
        cur = cnx.cursor()
        cur.execute(query,args)

        if cur.lastrowid:
            print('insert id' , cur.lastrowid)
        else:
            print('last insert id not found')

        cnx.commit()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cur.close()
  cnx.close()