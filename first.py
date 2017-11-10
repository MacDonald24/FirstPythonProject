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
			sizer = wx.GridBagSizer()
			self.entry = wx.TextCtrl(self,-1,value=u"Enter name.")
			sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
			self.entry2 = wx.TextCtrl(self,-1,value=u"Enter email address.")
			sizer.Add(self.entry2,(1,0),(2,2),wx.EXPAND)
			self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

			#Button
			button = wx.Button(self,-1,label="Insert")
			sizer.Add(button, (4,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)


			button2 = wx.Button(self,-1,label="Delete")
			sizer.Add(button2, (5,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button2)

			button3 = wx.Button(self,-1,label="Find")
			sizer.Add(button3, (6,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button3)

			button4 = wx.Button(self,-1,label="Update")
			sizer.Add(button4, (7,0))
			self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button4)

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


	
		def OnPressEnter(self,event):
			self.label.SetLabel(self.entry.GetValue())
			self.entry.SetFocus()
			self.entry.SetSelection(-1,-1)

			
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

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'MyFirstPythonApp')
    app.MainLoop()