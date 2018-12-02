#!/usr/bin/env python
# Version 1.0.2

import RPi.GPIO as GPIO
import SimpleMFRC522
import openpyxl
import datetime
import shutil

while True:
	inside = "in"
	outside = "out"
	nameis = ""
	direction = ""
	
	while direction != outside and direction != inside:
	
		direction = input("Going inside or outside?: ")
	
	reader = SimpleMFRC522.SimpleMFRC522()
	id, text = reader.read()
	date = datetime.date.today()
	time = datetime.datetime.now().time()
	wb = openpyxl.load_workbook(text.replace(" ", "") + '.xlsx')
	
	if text.replace(" ", "") in wb.sheetnames:
		nameis = "True"
		sheet = wb[text.replace(" ", "")]
	
	if nameis != "True":
		wb.create_sheet(text.replace(" ", ""))
		sheet = wb [text.replace(" ", "")]

	if direction == inside:
	        a = sheet.max_row
		sheet.cell(row=a+1,column=1).value="Inside"
	        sheet.cell(row=a+1,column=2).value=text
	        sheet.cell(row=a+1,column=3).value=date
	        sheet.cell(row=a+1,column=4).value=time
	
	        wb.save(text.replace(" ","") + '.xlsx')
		shutil.copy2('/home/pi/pilvijarjestelma/' + text.replace(" ", "") + '.xlsx', '/home/pi/NextcloudFold/excel')
		print("Welcome, " + text)
	
		GPIO.cleanup()
	
	elif direction == outside:
		a = sheet.max_row
	        sheet.cell(row=a+1,column=5).value="Outside"
	        sheet.cell(row=a+1,column=6).value=text
	        sheet.cell(row=a+1,column=7).value=date
	        sheet.cell(row=a+1,column=8).value=time

		sheet.cell(row=a+1,column=10).value='=sum()'
	
	        wb.save(text.replace(" ", "") + '.xlsx')
		shutil.copy2('/home/pi/pilvijarjestelma/' + text.replace(" ", "") + '.xlsx', '/home/pi/NextcloudFold/excel')
	        print("Goodbye, " + text)
	
		GPIO.cleanup()
