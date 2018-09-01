#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://www.bitforestinfo.com
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''
######################################################
                By S.S.B Group                          
######################################################
    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://www.bitforestinfo.com/
    Note: We Feel Proud To Be Indian
######################################################
'''


print __author__

try:
	import Tkinter
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

Standard Date  :	{0:%d}/{0:%B}/{0:%Y} {0:%A} {0:%I}:{0:%M}:{0:%S} {0:%p}
"""
printage="""Age 
         In Days : {} Days
         In Year : {} Years {} days
         In Hours : {} hours
         
"""

def main():
    root=Tkinter.Tk(className=" Age Calculator")
    root.configure(background="orange")
    storeobj=MFrame(root, text="Input Fields",bg="azure",fg="black")
    storeobj.pack(padx=100,pady=20,ipadx=20,ipady=20,expand="yes",fill='both')
    storeobj1=NFrame(root, text="Output Fields",bg="azure",fg="black")
    storeobj1.pack(padx=100,pady=20,ipadx=20,ipady=20,expand="yes",fill='both')
    main_variable = Tkinter.StringVar()
    main_variable.set(printdate)
    storeobj.main_variable = main_variable 
    storeobj1.main_variable = main_variable 
    storeobj1.create_label()
    root.mainloop()
    return

class MFrame(Tkinter.LabelFrame):
	def __init__(self, *args, **kwargs):
		Tkinter.LabelFrame.__init__(self,*args, **kwargs)
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
         self.main_variable.set(printdate.format(born)+printage.format(age,str(divmod(int(age),365)[0]),str(divmod(int(age),365)[1]),age*24))
         print self.main_variable.get()
         return

	def create_excecute_button(self):
         Tkinter.Button(self,text="Calculate",width=15,bg="white", fg="green" ,command=self.run_command, relief="raised").grid(row=10, column=0, columnspan=6)
         return

	def create_variables(self):
		self.variables=[]
		for i in [1,1,1970,1,59,59]:
			storeobj=Tkinter.StringVar()
			storeobj.set(i)
			self.variables.append(storeobj)
		return

	def create_date_spin_box(self):
		Tkinter.Label(self, text="dd/mm/yyyy",bg='snow').grid(row=1,column=0)
		Tkinter.Spinbox(self, from_=1,to_=31, width=3, textvariable=self.variables[0]).grid(row=1, column=1)
		Tkinter.Label(self, text="/").grid(row=1, column=2)
		Tkinter.Spinbox(self, from_=1,to_=12, width=3, textvariable=self.variables[1]).grid(row=1, column=3)
		Tkinter.Label(self, text="/").grid(row=1, column=4)
		Tkinter.Entry(self, width=6, textvariable=self.variables[2]).grid(row=1, column=5)
		return
	def create_time_spin_box(self):
		Tkinter.Label(self, text="hh:mm:ss",bg='snow').grid(row=5,column=0)
		Tkinter.Spinbox(self, from_=1,to_=24, width=3, textvariable=self.variables[3]).grid(row=5, column=1)
		Tkinter.Label(self, text=":").grid(row=5, column=2)
		Tkinter.Spinbox(self, from_=1,to_=60, width=3, textvariable=self.variables[4]).grid(row=5, column=3)
		Tkinter.Label(self, text=":").grid(row=5, column=4)
		Tkinter.Spinbox(self, from_=1,to_=60, width=3, textvariable=self.variables[5]).grid(row=5, column=5)
		return

	def create_labels_(self):
        
         Tkinter.Label(self, text="Date",bg='snow').grid(row=0, column=0, columnspan=4)
         Tkinter.Label(self, text="Time",bg='snow').grid(row=3, column=0, columnspan=4)
         return

class NFrame(Tkinter.LabelFrame):
	def __init__(self, *args, **kwargs):
		Tkinter.LabelFrame.__init__(self, *args, **kwargs)
		self.main_variable=None
		

	def create_label(self):
		Tkinter.Label(self, textvariable=self.main_variable, justify="left",bg='azure').pack()
		return




if __name__ == '__main__':
    main()
