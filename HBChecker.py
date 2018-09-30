# HBChecker by Epicpkmn11
# https://github.com/Epicpkmn11/DSi-HB-Checker/
# Feel free to make custom HBCheckerItems.py files for other uses

import os
import sys

# Fixing Python 2 compatibility
if(sys.version_info.major < (3)):
	input = raw_input

# Trying to import items file
try:
	import HBCheckerItems as checkFiles
except:
	print('='*80)
	print('Please put "HBCheckerItems.py" in the same places as this file')
	print('='*80)
	input('Press Enter to quit')
	quit()

# Creating variables
fileSetChoices = ''
fileFoundList = ''
filesFound = []
filesMissing = []

# Defining functions
# Allows clearing the screen on win32 & unix-based systems
def clear():
	if sys.platform == "win32":
		os.system('cls')
	else:
		os.system('clear')

# Checks if the file sets exist
def checkExist(fileSet):
	found = []
	file = checkFiles.fileSets[fileSet][0]
	newLine = file.find('\n')
	if newLine != -1:
		file = file[:(newLine-1)]
	if os.path.exists(file):
		found = [fileSet]
	return(found)

# Checks if the files within a set exist
def check(fileSet):
	missing = []
	files = checkFiles.fileSets[fileSet][1:]
	for file in files:
		fileCopy = file
		newLine = fileCopy.find('\n')
		if newLine != -1:
			fileCopy = fileCopy[:(newLine-1)]
		if os.path.exists(fileCopy):
			pass
		else:
			missing += [file]
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
		print('The following files were missing:')
		print('='*80)
		print('\n'+filesMissing[:-1])
	else:
		if printLines:
			clear()
		print('='*80)
		print('No files were missing!')

# Checking if sets exist
for fileSet in checkFiles.fileSets:
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
		fileFoundList += file + ', and '
	else:
		fileFoundList += file
	i+=1

# Printing sets found
if len(fileFoundList)>0:
	clear()
	print('='*80)
	print(fileFoundList + ' were found')
else:
	print('='*80)
	print('Nothing was found')

# Printing missing files
for file in filesFound:
	filesMissing = check(file)
printMissing(filesMissing,False)

# Prepping the file set options for manual checking
fileSetsAmount = len(checkFiles.fileSets)
i=1
for fileSet in sorted(checkFiles.fileSets):
	if(i%3)!=0:
		fileSetChoices += fileSet + '	'
		if len(fileSet)<15:
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
	print('Your options are: (Enter the number, or press Enter to quit)')
	print('\n'+fileSetChoices)
	manualCheck = input('> ')
	for fileSet in checkFiles.fileSets:
		if manualCheck == '':
			quit()
		if manualCheck == fileSet[:len(manualCheck)]:
			printMissing(check(fileSet),True)
			clearScreen = False
			break
	if clearScreen:
		clear()
		print('='*80)
		print('Invalid File Set')
