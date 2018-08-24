import os
import sys
import glob

#checks for python 3
if(sys.version_info<(3,0,0)):
	print('You are not using Python 3, please use Python 3 to run this script')
	input('Press Enter to close')
	quit()

filesMissing = []
scannedFiles = []
sdFiles = []

# Lists of required files
requiredFiles = {
	'hiyaCFW': [
		'bootcode.dsi', 
		'hiya/bootloader.nds', 
		'shared1/TWLCFG0.dat', 
		'shared1/TWLCFG1.dat', 
		'shared2/0000', 
		'shared2/launcher/wrap.bin', 
		'sys/cert.sys', 
		'sys/dev.kp', 
		'sys/HWID.sgn', 
		'sys/HWINFO_N.dat', 
		'sys/HWINFO_S.dat', 
		'sys/TWLFontTable.dat'
	],
	'dsimenuplusplus': [
		'BOOT.NDS', 
		'_nds/GBARunner2_fc.nds', 
		'_nds/GBARunner2.nds', 
		'_nds/nds-bootstrap-hb-nightly.nds', 
		'_nds/nds-bootstrap-hb-release.nds', 
		'_nds/nds-bootstrap-nightly.nds', 
		'_nds/nds-bootstrap-release.nds', 
		'_nds/nds-bootstrap.ini', 
		'_nds/dsimenuplusplus/dsimenu.srldr', 
		'_nds/dsimenuplusplus/gbaswitch.srldr', 
		'_nds/dsimenuplusplus/main.srldr', 
		'_nds/dsimenuplusplus/nightly-bootstrap', 
		'_nds/dsimenuplusplus/r4menu.srldr', 
		'_nds/dsimenuplusplus/release-bootstrap', 
		'_nds/dsimenuplusplus/slot1launch.srldr', 
		'_nds/dsimenuplusplus/emulators/gameyob.nds', 
		'_nds/dsimenuplusplus/emulators/nesds.nds', 
		'_nds/dsimenuplusplus/emulators/nestwl.nds', 
		'hiya/autoboot.bin', 
		'title/00030015/534c524e/content/00000000.app', 
		'title/00030015/534c524e/content/title.tmd', 
		'title/00030015/53524c41/content/00000000.app', 
		'title/00030015/53524c41/content/title.tmd'
	]			
}
if __name__ == "__main__":
	# Scan the files in the current work directory.
	for path, subdirs, files in os.walk('.'):
		for name in files:
			filePath = os.path.join(os.getcwd(), path[2:], name)
			scannedFiles.append(filePath)

	#checking files
	for file in scannedFiles:
		# print(file)
		currentFile = file[3:]
		# Check if HiyaCFW is installed.
		# print(currentFile)
		if currentFile == "hiya\settings.ini":
			print("HiyaCFW files detected, verifying files...")
			HiyaFiles = requiredFiles['hiyaCFW']
			region = input('What region is your DSi? (U/J/E/A) ').upper()
			while region:
				if(region == 'U'):
					HiyaFiles.extend(['title/00030017/484e4145/content/title.tmd', 'title/00030017/484e4145/content/title.tmd'])
					break
				elif(region == 'J'):
					HiyaFiles.extend(['title/00030017/484e414a/content/00000002.app', 'title/00030017/484e414a/content/title.tmd'])
					break
				elif(region == 'E'):
					HiyaFiles.extend(['title/00030017/484e4150/content/00000002.app', 'title/00030017/484e4150/content/title.tmd'])
					break
				elif(region == 'A'):
					HiyaFiles.extend(['title/00030017/484e4155/content/00000002.app', 'title/00030017/484e4155/content/title.tmd'])
					break
				else:
					print('Invalid Region')
					region = input('What region is your DSi? (U/J/E/A) ').upper()
			sdFiles.extend(HiyaFiles)
		# Check if DSiMenuPlusPlus is installed.
		elif currentFile == "_nds\dsimenuplusplus\main.srldr":
			print("DSiMenuPlusPlus files detected, verifying files...")
			sdFiles.extend(requiredFiles['dsimenuplusplus'])
		else:
			pass

	fileTree = sdFiles
	for file in fileTree:
		filePath = os.path.join(os.getcwd(), file)
		if os.path.exists(filePath):
			pass
		else:
			filesMissing.append(file)
	if filesMissing.count != 0:
		print("You are missing files: \n")
		for missingFile in filesMissing:
			print("{}\n".format(missingFile))
	else:
		print('Your SD Card is good!')

	input('Press Enter to quit')
	quit()

