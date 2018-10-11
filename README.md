# HB Checker
This is a Python *(2 or 3)* script designed to check if specific files are present and (optionally) if they are corrupted. It was designed for checking a DSi's SD card for HiyaCFW and TWiLight Menu++, but by creating your own `HBCheckerItems.json` files you can use it for pretty much anything!

I designed this script to make it as easy as possible to make custom Items files while allowing flexability. You can add comments that won't be checked for but will be displayed with the missing files, and add CRC-32 checksums to only the files that you want to have them checked on. Check out the [wiki page](https://github.com/Epicpkmn11/HBChecker/wiki/Item-Files) for more details on how to make your own.

To use, simply place `HBChecker.py` and `HBCheckerItems.json` in the root of whatever you're checking (such as a DSi's SD card) and run it `HBChecker.py` using Python!
