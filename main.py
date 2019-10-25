#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''
    Suraj Singh
    surajsinghbisht054@gmail.com
'''


print(__author__)
try:
	import tkinter
except:
	import tkinter as Tkinter
import dob

# Format
printdate = """    
Date  	: \t{0:%d}
Month 	: \t{0:%B}
Year  	: \t{0:%Y} 
Day   	: \t{0:%A} 
Hour  	: \t{0:%I}
Minute	: \t{0:%M}
Second	: \t{0:%S}
Period	: \t{0:%p}

Standard Date  	
		 {0:%d}/{0:%B}/{0:%Y} {0:%A} {0:%I}:{0:%M}:{0:%S} {0:%p}
"""
printage="""Age
		In Days : {} Days
		In Year : {} Years {} days
"""


def main():
	root=tkinter.Tk(className=" Age Calculator")
	storeobj=MFrame(root, text="Input Fields")
	storeobj.pack(padx=20,pady=20,ipadx=20,ipady=20,expand="yes",fill='both')

	storeobj1=NFrame(root, text="Output Fields")
	storeobj1.pack(padx=20,pady=20,ipadx=20,ipady=20,expand="yes",fill='both')
	main_variable = tkinter.StringVar()
	main_variable.set(printdate)
	storeobj.main_variable = main_variable 
	storeobj1.main_variable = main_variable
	storeobj1.create_label()
	root.mainloop()
	return

class MFrame(tkinter.LabelFrame):
	def __init__(self, *args, **kwargs):
		tkinter.LabelFrame.__init__(self,*args, **kwargs)
		self.main_variable=None
		self.all_function_trigger()

	def all_function_trigger(self):
		self.create_variables()
		self.create_labels_()
		self.create_date_spin_box()
		self.create_time_spin_box()
		self.create_excecute_button()
		return

	def run_command(self):
		lt=[]
		for i in self.variables:
			lt.append(i.get())
		data= [i.get().rjust(2,"0") for i in self.variables]
		age,born,today = dob.age(data)
		self.main_variable.set(printdate.format(born)+printage.format(age,str(divmod(int(age),365)[0]),str(divmod(int(age),365)[1])))
		print(self.main_variable.get())
		return

	def create_excecute_button(self):
		tkinter.Button(self,text="Calculate",width=15, command=self.run_command, relief="raised").grid(row=10, column=0, columnspan=6)
		return

	def create_variables(self):
		self.variables=[]
		for i in [1,1,1970,1,59,59]:
			storeobj=tkinter.StringVar()
			storeobj.set(i)
			self.variables.append(storeobj)
		return

	def create_date_spin_box(self):
		tkinter.Label(self, text="dd/mm/yyyy").grid(row=1,column=0)
		tkinter.Spinbox(self, from_=1,to_=31, width=3, textvariable=self.variables[0]).grid(row=1, column=1)
		tkinter.Label(self, text="/").grid(row=1, column=2)
		tkinter.Spinbox(self, from_=1,to_=12, width=3, textvariable=self.variables[1]).grid(row=1, column=3)
		tkinter.Label(self, text="/").grid(row=1, column=4)
		tkinter.Entry(self, width=6, textvariable=self.variables[2]).grid(row=1, column=5)
		return

	def create_time_spin_box(self):
		tkinter.Label(self, text="hh:mm:ss").grid(row=5,column=0)
		tkinter.Spinbox(self, from_=1,to_=24, width=3, textvariable=self.variables[3]).grid(row=5, column=1)
		tkinter.Label(self, text=":").grid(row=5, column=2)
		tkinter.Spinbox(self, from_=1,to_=60, width=3, textvariable=self.variables[4]).grid(row=5, column=3)
		tkinter.Label(self, text=":").grid(row=5, column=4)
		tkinter.Spinbox(self, from_=1,to_=60, width=3, textvariable=self.variables[5]).grid(row=5, column=5)
		return

	def create_labels_(self):
		tkinter.Label(self, text="Date").grid(row=0, column=0, columnspan=4)
		tkinter.Label(self, text="Time").grid(row=3, column=0, columnspan=4)
		return

class NFrame(tkinter.LabelFrame):
	def __init__(self, *args, **kwargs):
		tkinter.LabelFrame.__init__(self, *args, **kwargs)
		self.main_variable=None
		

	def create_label(self):
		tkinter.Label(self, textvariable=self.main_variable, justify="left").pack()
		return




if __name__ == '__main__':
	main()
