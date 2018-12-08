# Pilvijärjestelmä - work time tracking

This program uses a Raspberry Pi 3, an MFRC522 RFID reader and NextCloud to track work time.

## General dependencies:  
Raspberry Pi 3 or similar  
MFRC522 RFID reader, wired onto the GPIO pins of the Pi  
RFID tag(s)  
NextCloud server and client (server can be hosted elsewhere)  


## Python dependencies:  
SimpleMFRC522  
openpyxl  
datetime  
shutil  

## The program code is in the file version102.py

### How it works:

Running the version 102.py opens a program that asks the user whether they're arriving or leaving. This is determined by typing "inside" or "outside" to the terminal window.  

After determining the direction, the user is asked to place their RFID tag on the reader. The reader reads the data (name) written on the tag (text). This data is used in the name of the .xlsx document.  

The program cannot create the .xlsx files by itself, so it is necessary to create a .xlsx workbook with the right filename (for example DonJohnson.xlsx) in the program folder before running.  

The program creates a worksheet with the tag data as its name, and writes the event. If the direction is arrival, the event is written on the left side of the document. If leaving, it is written on the right.  

A worktime calculation is also written into the document. It should take into account human error while reading the tag.

After writing the document, it is saved in the program's folder and copied into NextCloud's client folder in order to sync it with the server.
