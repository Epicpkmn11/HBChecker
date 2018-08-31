import os
import sys
import glob

# Fixes Python 2 compatibility
if(sys.version_info.major < (3)):
	input = raw_input

# Creating variables
filesMissing = []
scannedFiles = []
sdFiles = []
isHiyaPresent = False
isDSiMemuPPPresnt = False

# Lists of required files
requiredFiles = {
	'hiyaCFW': [
		'bootcode.dsi \nFrom the downloaded "HiyaCFW/for SDNAND SD card"',
		'hiya/bootloader.nds \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
		'shared1/TWLCFG0.dat \nFrom your NAND backup',
		'shared1/TWLCFG1.dat \nFrom your NAND backup',
		'shared2/0000 \nFrom your NAND backup',
		'shared2/launcher/wrap.bin \nFrom your NAND backup',
		'sys/cert.sys \nFrom your NAND backup',
		'sys/dev.kp \nFrom your NAND backup',
		'sys/HWID.sgn \nFrom your NAND backup',
		'sys/HWINFO_N.dat \nFrom your NAND backup',
		'sys/HWINFO_S.dat \nFrom your NAND backup',
		'sys/TWLFontTable.dat \nFrom your NAND backup'
	],
	'dsimenuplusplus': [
		'BOOT.NDS \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2_fc.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/GBARunner2.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-hb-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-nightly.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap-release.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/nds-bootstrap.ini \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/dsimenu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/gbaswitch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/main.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/nightly-bootstrap \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/r4menu.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/release-bootstrap \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/slot1launch.srldr \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/gameyob.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nesds.nds \nFrom the downloaded "DSiMenuPP"',
		'_nds/dsimenuplusplus/emulators/nestwl.nds \nFrom the downloaded "DSiMenuPP"',
		'hiya/autoboot.bin \nFrom the downloaded "DSiMenuPP/Autoboot for HiyaCFW"',
		'title/00030015/534c524e/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/534c524e/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/00000000.app \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"',
		'title/00030015/53524c41/content/title.tmd \nFrom the downloaded "DSiMenuPP/CFW - SDNAND root"'
	]
}
if __name__ == "__main__":
	# Scan the files in the current working directory.
	for path, subdirs, files in os.walk('.'):
		for name in files:
			filePath = os.path.join(os.getcwd(), path[2:], name)
			scannedFiles.append(filePath)

	# Checks files
	for file in scannedFiles:
		# Checks if your on Windows and removes the file path before the cwd
		if sys.platform == "win32":
			currentFile = file[len(os.getcwd()):]
		else:
			currentFile = file[(len(os.getcwd())+1):]
		# Check if HiyaCFW is installed.
		if currentFile == ("bootcode.dsi"):
			isHiyaPresent = True
			print("HiyaCFW files detected, verifying files...")
			HiyaFiles = requiredFiles['hiyaCFW']
			region = input('What region is your DSi? (U/J/E/A) ').upper()
			while region:
				if(region == 'U'):
					HiyaFiles.extend(
						['title/00030017/484e4145/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
						'title/00030017/484e4145/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'])
					break
				elif(region == 'J'):
					HiyaFiles.extend(
						['title/00030017/484e414a/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
						'title/00030017/484e414a/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'])
					break
				elif(region == 'E'):
					HiyaFiles.extend(
						['title/00030017/484e4150/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
						'title/00030017/484e4150/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'])
					break
				elif(region == 'A'):
					HiyaFiles.extend(
						['title/00030017/484e4155/content/00000002.app \nFrom the downloaded "HiyaCFW/for PC/Modified Files" after running HiyaCFW Helper',
						'title/00030017/484e4155/content/title.tmd \nFrom the downloaded "HiyaCFW/for SDNAND SD card"'])
					break
				else:
					print('Invalid Region')
					region = input('What region is your DSi? (U/J/E/A) ').upper()
			sdFiles.extend(HiyaFiles)
		# Check if DSiMenuPlusPlus is installed.
		elif currentFile == os.path.join("_nds", "dsimenuplusplus", "main.srldr"):
			isDSiMemuPPPresnt = True
			print("DSiMenu++ files detected, verifying files...")
			sdFiles.extend(requiredFiles['dsimenuplusplus'])
		else:
			pass

	# Checking if Hiya/DSiMenu++ are missing and lets you force a check
	if isHiyaPresent == False:
		print("HiyaCFW NOT detected")
		if input("Force check HiyaCFW? (Doesn't check region specific files) (Y/N) ").upper() == 'Y':
			sdFiles.extend(requiredFiles['hiyaCFW'])
	if isDSiMemuPPPresnt == False:
		print("DSiMenu++ NOT detected")
		if input("Force check DSiMenu++? (Y/N) ").upper() == 'Y':
			sdFiles.extend(requiredFiles['dsimenuplusplus'])		

	fileTree = sdFiles
	for file in fileTree:
		fileCopy = file
		comment = fileCopy.find('\n')
		if comment != -1:
			fileCopy = fileCopy[:(comment-1)]
		filePath = os.path.join(os.getcwd(), fileCopy)
		if os.path.exists(filePath):
			pass
		else:
			filesMissing.append(file)
	if len(filesMissing) != 0:
		print("You are missing the following files: \n")
		for missingFile in filesMissing:
			print("{}\n".format(missingFile))
	else:
		print('Your SD Card is good!')

	input('Press Enter to quit')
	quit()
