from tkinter import *
from tkinter import ttk
import webbrowser



class calculator:

	def __init__(self,cost,coupon,amount,tax,multicoupon,addOn):
		self.__itemPrice = cost
		self.__couponPrice = coupon
		self.__multipleItems = amount
		self.__doesItHaveTax = tax
		self.__singleCoupon = multicoupon
		self.__additionalDiscount = addOn
		
		numOfItems = 0
		
		print (self.__singleCoupon)
	

	def itemCalculator(self, cost, coupon, amount, tax, multicoupon, addOn):
		self.__itemPrice = cost
		self.__couponPrice = coupon
		self.__multipleItems = amount
		self.__doesItHaveTax = tax
		self.__singleCoupon = multicoupon
		self.__additionalDiscount = addOn
		taxHolder = self.__couponPrice
		
		self.__yes = { "Yes" : True, "y" : True, "Y" : True, "yes" : True, "YES" : True, "True": True}   # used to determine yes or no
		self.__no = {"No" : False, "n" : False, "N" : False, "no" :False, "NO" : False, "False": False}
		
		if self.__singleCoupon > 0: # If one coupon
			self.__couponPrice = self.__singleCoupon	
		if self.__singleCoupon == 0:  # If multiple coupons
			x = self.__couponPrice
			if x < 1:   # Automatically doubles coupons under .99
				placeholder = self.__couponPrice
				if self.__couponPrice> 1:
					self.__couponPrice = self.__couponPrice * self.__multipleItems
				if self.__multipleItems <= 4:
					self.__couponPrice = self.__couponPrice * 2
					self.__couponPrice = self.__couponPrice* self.__multipleItems
					print ("Your coupon value is less than $1.00. Your coupon was automatically doubled.")
					print ("Your coupon value is:", self.__couponPrice)
					print("-------------------------------------------------")
			
				if self.__multipleItems > 4:
					print (" You have more than 4 coupons, only 4 will double.")
					howManyLeft = self.__multipleItems - 4
					self.__couponPrice = self.__couponPrice * 2
					self.__couponPrice = self.__couponPrice * 4
					totalLeft = howManyLeft * placeholder
					self.__couponPrice = self.__couponPrice + totalLeft
					print (" The value of your coupons combined is:", self.__couponPrice)
			if x >= 1: # If one coupon
				self.__couponPrice = self.__couponPrice * self.__multipleItems
				print("The value of your coupons is:", self.__couponPrice)
				
			
		if self.__multipleItems > 1 :
			numOfItems= self.__multipleItems
			self.__itemPrice = numOfItems * self.__itemPrice
			
			discountPrice = self.__itemPrice - self.__couponPrice
			outputPrice = round(discountPrice, 2)
	
			print("Calculating....")
			print("The discount price of your item is:",outputPrice)
	
		if self.__multipleItems  == 1:	  
			discountPrice = self.__itemPrice - self.__couponPrice
			outputPrice = round(discountPrice, 2)
	
			print("Calculating....")
			print("The discount price of your item is:",outputPrice)

		

	
		if taxHolder < 1:      # TaxHolder is a stand in for COUPON PRICE to calculate proper tax on doubles.
			if self.__multipleItems > 4:
				taxHolder = taxHolder * 4
				print ("taxHolder is", taxHolder, "and there were only 4 to account for")
			if self.__multipleItems <= 4:
				taxHolder = self.__multipleItems * taxHolder
				print ("taxHolder is", taxHolder, "and", self.__multipleItems, "was multiplied by", taxHolder)
		if taxHolder >= 1:
			taxHolder = 0

		if self.__doesItHaveTax == 1 :
			salesTax = self.__itemPrice - taxHolder 
			salesTax1 = salesTax * .08
			outputPrice = outputPrice + salesTax1
			outputPrice = round(outputPrice, 2)
			print ("The price after tax is:",outputPrice)
		if self.__doesItHaveTax == 0:
			print ("Not calculating tax")
		if self.__doesItHaveTax < 1:
			salesTax = self.__itemPrice  - taxHolder 
			salesTax1 = salesTax * self.__doesItHaveTax
			outputPrice = outputPrice + salesTax1
			outputPrice = round(outputPrice, 2)
			print ("The price after tax is:", outputPrice)
		if self.__doesItHaveTax > 1:
			self.__doesItHaveTax = self.__doesItHaveTax / 100
			salesTax = self.__itemPrice  - taxHolder 
			salesTax1 = salesTax * doesItHaveTax
			outputPrice = outputPrice + salesTax1
			outputPrice = round(outputPrice, 2)
			print("Tax has been converted to decimal. Price after tax is:", outputPrice)

	

		if self.__additionalDiscount > 0:
		
			outputPrice = outputPrice - self.__additionalDiscount
			outputPrice = round(outputPrice, 2)
			print ("The final discounted price is:",outputPrice)

		return outputPrice
	

	
	
	


#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#TKINTER Requirements

#discount Item price popup
def popupmsg(msg):
	popup = Tk()
	popup.title("Discount Item Price")

	label2= ttk.Label(popup, text="Discounted Item Price")
	label = ttk.Label(popup, text=msg)
	label2.pack(side="top", fill = "x", pady=10)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popup, text="Okay, Thanks!", command = popup.destroy)
	B1.pack()
	popup.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#   2 variable popup message	
def helpfulMSG(message, amount):
	popup = Tk()
	popup.title("Important Message")
	
	label = ttk.Label(popup, text = message)
	label2 = ttk.Label(popup, text = amount)
	label.pack(side = "top", fill = "x", pady = 10)
	label2.pack(side = "top", fill = "x", pady = 10)
	B1 = ttk.Button(popup, text ="Close Message", command = popup.destroy)
	B1.pack()
	popup.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

# error message with 1 variable to fix
def errorMSG(msg):
	popup = Tk()
	popup.title("ERROR!!")
	
	label = ttk.Label(popup, text = "Sorry, but whatever you just did broke it!!")
	label2 = ttk.Label(popup, text = msg)
	label.pack(side = "top", fill = "x", pady = 10)
	label2.pack(side = "top", fill = "x", pady = 10)
	B1 = ttk.Button(popup, text ="OK Sorry!", command = popup.destroy)
	B1.pack()
	popup.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
		
def tasker():
	
	cost = float(e1.get())
	coupon = float(e2.get())
	amount = float(e3.get())
	tax = float(e4.get())
	multiple = float(e5.get())
	additional = float(e6.get())
	x= calculator(e1,e2,e3,e4,e5,e6)
	x = x.itemCalculator(cost,coupon,amount,tax,multiple,additional)

	
	


	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)
	e6.delete(0,END)
	popupmsg(x)	

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
# Menu Bar tax calculator. Is standalone
def taxCalc():  
	holder = 0
	
	taxApp = Tk()
	taxApp.title("Tax Calculator")
	
	Label(taxApp, text="Item Cost").grid(row=0)
	global tax1
	global tax2
	tax1 = Entry(taxApp)
	Label(taxApp, text="Tax amount: 1 = Chelsea's tax or enter unique rate").grid(row=1)
	tax2= Entry(taxApp)
	tax1.grid(row = 0, column =1)
	tax2.grid(row = 1, column = 1)
	ttk.Button(taxApp, text='Calculate Tax!', command=taxCalcTask).grid(row=2, column=1, sticky=W, pady=4)
	taxApp.mainloop()

def taxCalcTask():
	
	
	try:
		cost = float(tax1.get())
		tax = float(tax2.get())

	except:
		errorMSG("Please fill in both fields!")

	if tax > 1:
		tax = tax / 100
		holder = cost * tax
		cost = cost + holder
		helpfulMSG("The cost including tax is",cost)
	if tax == 1:
		tax = .08
		holder = cost * tax
		cost = cost + holder
		helpfulMSG("The cost including tax is", cost)
	if tax < 1:
		holder = cost * tax
		cost = cost + holder
		helpfulMSG("The cost inlcuding tax is",cost)

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#Bogo menubar task: Is standalone
def bogo():

	bogoApp = Tk()
	bogoApp.title("Use this to determine BOGO")
	
	Label(bogoApp, text="Amount to purchase").grid(row=0)
	global bogo1
	bogo1 = Entry(bogoApp)
	bogo1.grid(row = 0, column =1)
	ttk.Button(bogoApp, text='Calculate Bogo!', command=bogoCalcTasker).grid(row=2, column=1, sticky=W, pady=4)
	bogoApp.mainloop()


def bogoCalcTasker():
	try:
		amount = float(bogo1.get())
	except:
		errorMSG("Please fill in: Amount to purchase")	
		
	amount = amount / 2
	helpfulMSG("Please enter this amount into main app: How many are you buying?", amount)

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------			


	



master = Tk()
master.title("Chelsea's Coupon App")


Label(master, text="How much does one item cost?").grid(row=0)
e1= Entry(master)  #Item Cost

Label(master, text="How much is one coupon worth? ").grid(row=1)
e2= Entry(master)   #Coupon Value

Label(master, text="How many are you buying? ").grid(row=2)
e3 = Entry(master)  #How many are there

Label(master, text="0 = no tax 1 = Chelsea tax OR enter unique tax rate.").grid(row=3)
e4 = Entry(master)  #Does it have tax

Label(master, text="If deal uses single coupon, enter amount. Enter 0 otherwise.").grid(row=4)
e5 = Entry(master)  #One or multiple coupons

Label(master, text="Enter any additional coupons total amount. Enter 0 otherwise.").grid(row = 5)
e6 = Entry(master) # Additional Coupons





ttk.Button(master, text='Calculate Price!', command=tasker).grid(row=9, column=1, sticky=W, pady=4)




#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
#TOP MENU
def NewFile():
	print ("New File!")
def OpenFile():
    print (name)
def About():
    print ("This is a simple example of a menu")
def helper():
	webbrowser.open("help.txt")



menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_command(label="Help", command = helper)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Other Tools", menu=helpmenu)
helpmenu.add_command(label="Tax Calculator", command=taxCalc)
helpmenu.add_command(label="BOGO Calculator", command = bogo)





e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row =2, column=1)
e4.grid(row = 3,column=1)
e5.grid(row = 4, column=1)
e6.grid(row = 5, column = 1)




mainloop()

		



#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#Usable code


#Checkbox
#----------------------------------------------------------------------------------------------------

#ckVar= IntVar()   Checkbutton for multiple coupons variable (0 or 1)

#def checkbox():       Method that takes checkbox input  
#	state = ckVar.get()
#	if == 1:
#
#	if == 0:

#Label(master, text = "BoGo?").grid(row = 6, column = 0)     Functioning Checkbox code for TKINTER                   
#bogo = Checkbutton(master, variable= ckVar)      

#bogo.grid(row = 6, column = 1)


#-----------------------------------------------------------------------------------------------------

# create a toplevel menu


#menubar = Menu(master)
#mb.tk_menuBar.add_checkbutton (label = "Click", comman = taxCalc) 
#menubar.add_command(label="Tax Calculator", command= taxCalc)
#menubar.add_command(label="BOGO", command=bogo)
#menubar.add_command(label="Exit", command = master.quit)

# display the menu
#master.config(menu=menubar)

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

#Create buttons on bottom of app
#Button(master, text='Exit', command=master.quit).grid(row=9, column=0, sticky=W, pady=4)

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

 