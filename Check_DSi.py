import os
import sys
#checks for python 3
if(sys.version_info<(3,0,0)):
	print('You are not using Python 3, please use Python 3 to run this script')
	input('Press Enter to close')
	quit()

#Choosing what to check for
region = input('What region is your DSi? (U/J/E/A) ').upper()
hiyacfw = input('Would you like to check for HiyaCFW files? (Y/N) ').upper()
dsimenuplusplus = input('Would you like to check for DSiMenu++ files? (Y/N) ').upper()
output = 'You are missing: '

#Quit if both no
if(hiyacfw != 'Y'):
	if(dsimenuplusplus != 'Y'):
		print('You have not selected to check for HiyaCFW or DSiMenu++ files')
		input('Press Enter to close')
		quit()

#HiyaCFW checking
if(hiyacfw == 'Y'):
	if os.path.exists('./bootcode.dsi'):
	    pass
	else:
	    output = output+'/bootcode.dsi, '
	if os.path.exists('./hiya/bootloader.nds'):
	    pass
	else:
	    output = output+'/hiya/bootloader.nds, '
	if os.path.exists('./shared1/TWLCFG0.dat'):
	    pass
	else:
	    output = output+'/shared1/TWLCFG0.dat, '
	if os.path.exists('./shared1/TWLCFG1.dat'):
	    pass
	else:
	    output = output+'/shared1/TWLCFG1.dat, '
	if os.path.exists('./shared2/0000'):
	    pass
	else:
	    output = output+'/shared2/0000, '
	if os.path.exists('./shared2/launcher/wrap.bin'):
	    pass
	else:
	    output = output+'/shared2/launcher/wrap.bin, '
	if os.path.exists('./sys/cert.sys'):
	    pass
	else:
	    output = output+'/sys/cert.sys, '
	if os.path.exists('./sys/dev.kp'):
	    pass
	else:
	    output = output+'/sys/dev.kp, '
	if os.path.exists('./sys/HWID.sgn'):
	    pass
	else:
	    output = output+'/sys/HWID.sgn, '
	if os.path.exists('./sys/HWINFO_N.dat'):
	    pass
	else:
	    output = output+'/sys/HWINFO_N.dat, '
	if os.path.exists('./sys/HWINFO_S.dat'):
	    pass
	else:
	    output = output+'/sys/HWINFO_S.dat, '
	if os.path.exists('./sys/TWLFontTable.dat'):
	    pass
	else:
	    output = output+'/sys/TWLFontTable.dat, '

	#Regional checking
	if(region == 'U'):
	    if os.path.exists('./title/00030017/484e4145/content/00000002.app'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4145/content/00000002.app, '
	    if os.path.exists('./title/00030017/484e4145/content/title.tmd'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4145/content/title.tmd, '
	elif(region == 'J'):
	    if os.path.exists('./title/00030017/484e414a/content/00000002.app'):
	        pass
	    else:
	        output = output+'/title/00030017/484e414a/content/00000002.app, '
	    if os.path.exists('./title/00030017/484e414a/content/title.tmd'):
	        pass
	    else:
	        output = output+'/title/00030017/484e414a/content/title.tmd, '
	elif(region == 'E'):
	    if os.path.exists('./title/00030017/484e4150/content/00000002.app'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4150/content/00000002.app, '
	    if os.path.exists('./title/00030017/484e4150/content/title.tmd'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4150/content/title.tmd, '
	elif(region == 'A'):
	    if os.path.exists('./title/00030017/484e4155/content/00000002.app'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4155/content/00000002.app, '
	    if os.path.exists('./title/00030017/484e4155/content/title.tmd'):
	        pass
	    else:
	        output = output+'/title/00030017/484e4155/content/title.tmd, '
	else:
	    print('Invalid region')
	    input('Press Enter to quit')
	    quit()

#DSiMenu++ checking
if(dsimenuplusplus == 'Y'):
	if os.path.exists('./BOOT.NDS'):
		pass
	else:
		output = output+'/BOOT.NDS, '
	if os.path.exists('./_nds'):
		pass
	else:
		output = output+'/_nds, '
	if os.path.exists('./title/00030015/534c524e/content/00000000.app'):
		pass
	else:
		output = output+'/title/00030015/534c524e/content/00000000.app, '
	if os.path.exists('./title/00030015/534c524e/content/title.tmd'):
		pass
	else:
		output = output+'/title/00030015/534c524e/content/title.tmd, '
	if os.path.exists('./title/00030015/53524c41/content/00000000.app'):
		pass
	else:
		output = output+'/title/00030015/53524c41/content/00000000.app, '
	if os.path.exists('./title/00030015/53524c41/content/00000000.app'):
		pass
	else:
		output = output+'/title/00030015/53524c41/content/00000000.app, '

#Displaying results
if(output != 'You are missing: '):
    print(output)
else:
    print('Your SD card is good!')
input('Press Enter to quit')
