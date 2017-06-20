#!/usr/bin/python
# -*- coding: utf-8 -*-
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.in
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
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__

# Import Module
import re
import datetime

# pattern For Checking Valid Time Format
pattern = "(\d{1,2})/(\d{1,2})/(\d\d\d\d).(\d{1,2}):(\d{1,2}):(\d{1,2})" 

#  ++++ Checking Mechanism ++++++++++
# Hour
def check_h(h):
	if h==24:
		h=0
	else:
		pass
	return h # hour

# Minutes
def check_m(m):
	if m==60:
		m=0
	else:
		pass
	return m  # Minute

# Seconds
def check_s(s):
	if s==60:
		s=0
	else:
		pass
	return s 

# Main Function
def main(data):
	# Matching Pattern
	if re.match(pattern, data):
		data=[i.rjust(2, '0') for i in re.match(pattern, data).groups()]
	else:
		data=None
	return data

def age(data):
	input_time=data
	try:
		d = datetime.date(int(input_time[2]),
			int(input_time[1]), 
			int(input_time[0]))
			# Time
		t = datetime.time(check_h(int(input_time[3])),
			check_m(int(input_time[4])),
			check_s(int(input_time[5])))
		# Combine Date And Time
		b_dt = datetime.datetime.combine(d,t) 
		# Today Time
		t_dt = datetime.datetime.today()
		return [abs(t_dt-b_dt).days,b_dt,t_dt]

	except EOFError as e:
		print "[*] Something Wrong.."
		print "[*] Friend... ", e
		return 
		

if __name__ == '__main__':
	formated_time = main(raw_input("[+] Enter Date In dd/mm/year hh:mm:ss "))		# Formated Date
	print datetime.timedelta(days=age(formated_time)[0]).__str__()
