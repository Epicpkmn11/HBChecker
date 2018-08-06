import os
import sys

#checks for python 3
if(sys.version_info<(3,0,0)):
	print('You are not using Python 3, please use Python 3 to run this script')
	input('Press Enter to close')
	quit()

#creating functions
def end():
	input('Press Enter to quit')
	quit()

#defining variables
missingFiles = 'You\'re missing '
files = ['']

#choosing what to check for
hiyacfw = input('Would you like to check for HiyaCFW files? (Y/N) ').upper()
if(hiyacfw == 'Y'):
	region = input('What region is your DSi? (U/J/E/A) ').upper()
dsimenuplusplus = input('Would you like to check for DSiMenu++ files? (Y/N) ').upper()

#determining files to check
if(hiyacfw == 'Y'):
	files = ['bootcode.dsi', 'hiya/bootloader.nds', 'shared1/TWLCFG0.dat', 'shared1/TWLCFG1.dat', 'shared2/0000', 'shared2/launcher/wrap.bin', 'sys/cert.sys', 'sys/dev.kp', 'sys/HWID.sgn', 'sys/HWINFO_N.dat', 'sys/HWINFO_S.dat', 'sys/TWLFontTable.dat']
	if(region == 'U'):
		files = files + ['title/00030017/484e4145/content/00000002.app', 'title/00030017/484e4145/content/title.tmd']
	elif(region == 'J'):
		files = files + ['title/00030017/484e414a/content/00000002.app', 'title/00030017/484e414a/content/title.tmd']
	elif(region == 'E'):
		files = files + ['title/00030017/484e4150/content/00000002.app', 'title/00030017/484e4150/content/title.tmd']
	elif(region == 'A'):
		files = files + ['title/00030017/484e4155/content/00000002.app', 'title/00030017/484e4155/content/title.tmd']
	else:
		print('Invalid Region')
		end()
if(dsimenuplusplus == 'Y'):
	files = files + ['BOOT.NDS','_nds/GBARunner2_fc.nds', '_nds/GBARunner2.nds', '_nds/hb-bootstrap.nds', '_nds/nds-bootstrap.ini', '_nds/nightly-bootstrap-sdk5.nds', '_nds/nightly-bootstrap.nds', '_nds/release-bootstrap-sdk5.nds', '_nds/release-bootstrap.nds', '_nds/dsimenuplusplus/dsimenu.srldr', '_nds/dsimenuplusplus/gbaswitch.srldr', '_nds/dsimenuplusplus/main.srldr', '_nds/dsimenuplusplus/nightly-bootstrap', '_nds/dsimenuplusplus/nightly-bootstrap-sdk5', '_nds/dsimenuplusplus/r4menu.srldr', '_nds/dsimenuplusplus/release-bootstrap','_nds/dsimenuplusplus/release-bootstrap-sdk5', '_nds/dsimenuplusplus/slot1launch.srldr', '_nds/dsimenuplusplus/emulators/gameyob.nds', '_nds/dsimenuplusplus/emulators/nesds.nds', '_nds/dsimenuplusplus/emulators/nestwl.nds', 'title/00030015/534c524e/content/00000000.app', 'title/00030015/534c524e/content/title.tmd', 'title/00030015/53524c41/content/00000000.app', 'title/00030015/53524c41/content/title.tmd']
if(dsimenuplusplus == hiyacfw != 'Y'):
	print('You have not selected to check for HiyaCFW or DSiMenu++ files')
	end()

#checking files
for file in files:
	fileExists = os.path.exists(file)
	if fileExists == False:
		missingFiles = missingFiles + '/' + file + ', '

#displaying results
if(missingFiles != 'You\'re missing '):
	missingFiles = missingFiles[:-2]
	print(missingFiles)
	end()
else:
	print('Your SD Card is good!')
	end()