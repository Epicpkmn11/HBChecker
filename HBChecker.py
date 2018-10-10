# HBChecker by Epicpkmn11
# https://github.com/Epicpkmn11/HBChecker/
# Feel free to make custom HBCheckerItems.py files for other uses

import os
import sys
import json
import zlib

# Fixing Python 2 compatibility
if(sys.version_info.major < (3)):
	input = raw_input

# Creating variables
fileSetChoices = ''
fileFoundList = ''
filesFound = []
filesMissing = []
fileSets = {}
itemsFile = 'HBCheckerItems.json'
bufferSize = 65536
checkCRC = True

# Defining functions
# Allows clearing the screen on win32 & unix-based systems
def clear():
	if sys.platform == 'win32':
		os.system('cls')
	else:
		os.system('clear')

# Let's you convert a base 16 int to a string properly
def intToStr(n,base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return intToStr(n//base,base) + convertString[n%base]

# Checks if the file sets exist
def checkExist(fileSet):
	found = []
	file = fileSets[fileSet][0]
	chksum = file.find(';')
	if chksum != -1:
		crc = file[chksum+1:].upper()
		file = file[:chksum]
	newLine = file.find('\n')
	if newLine != -1:
		file = file[:(newLine-1)]

	if os.path.exists(file):
		if checkCRC:
			if chksum != -1:
				checkFile = open(file, 'rb')
				buffr = checkFile.read(bufferSize)
				crcValue = 0
				while len(buffr) > 0:
					crcValue = zlib.crc32(buffr, crcValue)
					buffr = checkFile.read(bufferSize)
				crcString = intToStr(crcValue, 16)
				while len(crcString)<8:
					crcString = '0' + crcString
				if crcString == crc:
					found = [fileSet]
			else:
				found = [fileSet]
		else:
			found = [fileSet]
	return(found)

# Checks if the files within a set exist
def check(fileSet):
	missing = []
	files = fileSets[fileSet][1:]
	for file in files:
		fileCopy = file
		newLine = fileCopy.find('\n')
		if newLine != -1:
			fileCopy = fileCopy[:(newLine-1)]
		chksum = file.find(';')
		if chksum != -1:
			crc = file[chksum+1:].upper()
			file = file[:chksum]

		if os.path.exists(fileCopy):
			if checkCRC:
				if chksum != -1:
					checkFile = open(fileCopy, 'rb')
					buffr = checkFile.read(bufferSize)
					crcValue = 0
					while len(buffr) > 0:
						crcValue = zlib.crc32(buffr, crcValue)
						buffr = checkFile.read(bufferSize)
					crcString = intToStr(crcValue, 16)
					while len(crcString)<8:
						crcString = '0' + crcString
					if crcString != crc:
						missing += [file + '\nwas corrupted: CRC-32 DIDN\'T MATCH ' + intToStr(crcValue, 16) + ':'+ crc]
		else:
			missing += [file + '\nwas missing']
	return(missing)

# Prints out the missing files from a set
def printMissing(missingList, printLines):
	filesMissing = ''
	for file in missingList:
		filesMissing += file + '\n\n'

	if len(filesMissing)>0:
		if printLines:
			clear()
		print('='*80)
		if checkCRC:
			print('The following files were missing or corrupted:')
		else:
			print('The following files were missing:')
		print('='*80)
		print('\n'+filesMissing[:-1])
	else:
		if printLines:
			clear()
		print('='*80)
		if not printLines:
			print('No files were missing! (^ Make sure everything you need checked was found)')
		else:
			if checkCRC:
				print('No files were missing or corrupted!')
			else:
				print('No files were missing!')

# Loading items json file
while True:
	try:
		with open(itemsFile, 'r') as itemsJson:
			fileSets = json.load(itemsJson)
		break
	except:
		clear()
		print('='*80)
		print(itemsFile + ' not found')
		print('Please type the name of an items file, Drag/Drop it here, or press Enter to quit')
		print('='*80)
		itemsFile =  input('> ')
		# Remove \ on non windows systems
		if sys.platform != 'win32':
			while itemsFile.find('\\') != -1:
				bkslsh = itemsFile.find('\\')
				itemsFileCopy = itemsFile
				itemsFileCopy = itemsFile[:bkslsh]
				itemsFileCopy += itemsFile[bkslsh+1:]
				itemsFile = itemsFileCopy
		# Remove spaces from end of file names (Mac puts them on drag/drop)
		if itemsFile[-1:] == ' ':
			itemsFile = itemsFile[:-1]
		# Remove " from file names (Windows puts them on drag/drop)
		if itemsFile[1:] == '"':
			itemsFile = itemsFile[:1]
		if itemsFile[-1:] == '"':
			itemsFile = itemsFile[:-1]

		if itemsFile == '':
			quit()

# Clearing the screen
clear()

# Checking if sets exist
for fileSet in fileSets:
	filesFound += checkExist(fileSet)

# Preping to print sets found nicely
i=0
filesFoundAmount = len(filesFound)
for file in filesFound:
	space = file.find(' ')
	file = file[(space+1):]
	if(i+2)<filesFoundAmount:
		fileFoundList += file + ', '
	elif(i+1)<filesFoundAmount:
		if filesFoundAmount==2:
			fileFoundList += file + ' and '
		else:
			fileFoundList += file + ', and '
	else:
		fileFoundList += file
	i+=1

# Printing sets found
if len(fileFoundList)>0:
	clear()
	print('='*80)
	if filesFoundAmount>1:
		print(fileFoundList + ' were found')
	else:
		print(fileFoundList + ' was found')
else:
	print('='*80)
	print('Nothing was found')

# Printing missing files
for file in filesFound:
	filesMissing += check(file)
printMissing(filesMissing,False)

# Prepping the file set options for manual checking
fileSetsAmount = len(fileSets)
i=1
for fileSet in sorted(fileSets):
	if(i%3)!=0:
		fileSetChoices += fileSet + '	'
		if len(fileSet)<16:
			fileSetChoices += '	'
		if len(fileSet)<8:
			fileSetChoices += '	'
	else:
		if i<fileSetsAmount:
			fileSetChoices += fileSet + '\n'
		else:
			fileSetChoices += fileSet
	i+=1
# Infinite loop so you can check as many options as you want
while True:
	clearScreen = True
	print('='*80)
	print('Would you like to check for more?')
	if checkCRC:
		print('Your options are:\n(Enter the number, 0 to disable checksum, or press Enter to quit)')
	else:
		print('Your options are:\n(Enter the number, 0 to enable checksum, or press Enter to quit)')
	print('\n'+fileSetChoices)
	manualCheck = input('> ')
	for fileSet in fileSets:
		if manualCheck == '':
			quit()
		elif manualCheck == '0':
			if checkCRC:
				checkCRC = False
			else:
				checkCRC = True
			clearScreen = False
			clear()
			print('='*80)
			if checkCRC:
				print('Corruption detection enabled')
			else:
				print('Corruption detection disabled')
			break
		elif manualCheck == fileSet[:len(manualCheck)]:
			printMissing(check(fileSet),True)
			clearScreen = False
			break
	if clearScreen:
		clear()
		print('='*80)
		print('Invalid File Set')
