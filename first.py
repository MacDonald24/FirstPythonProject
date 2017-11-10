import mysql.connector
from mysql.connector import errorcode
try:
	import wx
except ImportError:
	raise ImportError + "The wxPython module is required to run this program"

class simpleapp_wx(wx.Frame):
		def __init__(self,parent,id,title):
			wx.Frame.__init__(self,parent,id,title)
			self.parent = parent
			self.initialize()

		def initialize(self):
			#TextBox
			sizer = wx.GridBagSizer()
			self.entry = wx.TextCtrl(self,-1,value=u"Enter name.")
			sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
			self.entry2 = wx.TextCtrl(self,-1,value=u"Enter email address.")
			sizer.Add(self.entry2,(1,0),(2,2),wx.EXPAND)
			self.entry3 = wx.TextCtrl(self,-1,value=u"Enter user id")
			sizer.Add(self.entry3,(1,8),(1,9),wx.EXPAND)

			#Button
			button = wx.Button(self,-1,label="Insert")
			sizer.Add(button, (4,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)


			button2 = wx.Button(self,-1,label="Delete")
			sizer.Add(button2, (5,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClickDelete, button2)

			button3 = wx.Button(self,-1,label="Find")
			sizer.Add(button3, (6,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClickFind, button3)

			button4 = wx.Button(self,-1,label="Update")
			sizer.Add(button4, (7,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClickUpdate, button4)

			self.label = wx.StaticText(self,-1,label=u'Hello !')
			self.label.SetBackgroundColour(wx.BLUE)
			self.label.SetForegroundColour(wx.WHITE)
			sizer.Add( self.label, (9,0),(9,1), wx.EXPAND )
			sizer.AddGrowableCol(0)
			self.SetSizerAndFit(sizer)
			#self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
			self.entry.SetFocus()
			self.entry.SetSelection(-1,-1)
			self.Show(True)


			
		try:

			def OnButtonClick(self,event):
						self.label.SetLabel( "Name : "+ self.entry.GetValue() + "\nEmail Address : "  + self.entry2.GetValue())
						self.entry.SetFocus()
						self.entry.SetSelection(-1,-1)

						cnx = mysql.connector.connect(user = 'root', password = '',host = '127.0.0.1', database = 'testingdatabase')

						query = "INSERT INTO users(name,email_address)" \
						        "VALUES(%s,%s)"

						if cnx.is_connected():
						        	print('Connected to MySQL database')
						        	name = self.entry.GetValue() 
						        	email_address = self.entry2.GetValue() 
						        	args = (name, email_address)
						        	print(args)
						        	cur = cnx.cursor()
						        	cur.execute(query,args)
						        	cnx.commit()
						        	if cur.lastrowid:
						        		print('insert id' , cur.lastrowid)
						        	else:
						        		print('last insert id not found')

						        		

		except mysql.connector.Error as err:
			  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			    print("Something is wrong with your user name or password")
			  elif err.errno == errorcode.ER_BAD_DB_ERROR:
			    print("Database does not exist")
			  else:
			  	print(err)
			  	cur.close()
			  	cnx.close()

		def OnButtonClickDelete(self,event):
			print("Delete")
			user_id = (int(self.entry3.GetValue()))
			print(user_id)
			try:
				query = "DELETE FROM users WHERE id = '%d'" % (user_id)
				cnx = mysql.connector.connect(user = 'root', password = '',host = '127.0.0.1', database = 'testingdatabase')
				cursor = cnx.cursor()
				cursor.execute(query)
				cnx.commit()
			except Error as e:
					print(e)
			finally:
					cursor.close()
					cnx.close()

		def OnButtonClickUpdate(self,event):
			print("Update the User")
		def OnButtonClickFind(self,event):
			print("Find")


			try:
				cnx = mysql.connector.connect(user = 'root', password = '',host = '127.0.0.1', database = 'testingdatabase')
				cursor = cnx.cursor()
				cursor.execute("SELECT * FROM users")

				rows = cursor.fetchall()

				print('Total Row(s):', cursor.rowcount)

				print(rows[3])
				'''for row in rows:
					print(row)'''

			except Error as e:
					print(e)
			finally:
					cursor.close()
					cnx.close()


if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'MyFirstPythonApp')
    app.MainLoop()