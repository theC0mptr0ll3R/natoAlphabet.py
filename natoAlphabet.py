#!/usr/bin/env python

import sys

d = {'A':'ALFA', 'B':'BRAVO', 'C':'CHARLIE', 'D':'DELTA', 'E':'ECHO', 'F':'FOXTROT', 'G':'GOLF', 'H':'HOTEL', 'I':'INDIA', 'J':'JULIETT', 'K':'KILO', 'L':'LIMA', 'M':'MIKE', 'N':'NOVEMBER', 'O':'OSCAR', 'P':'PAPA', 'Q':'QUEBEC', 'R':'ROMEO', 'S':'SIERRA', 'T':'TANGO', 'U':'UNIFORM', 'V':'VICTOR', 'W':'WHISKEY', 'X':'XRAY', 'Y':'YANKEE', 'Z':'ZULU', '1':'Wun', '2':'Two', '3':'Tree', '4':'Fower', '5':'Fife', '6':'Six', '7':'Seven', '8':'Ait', '9':'Niner', '0':'Zeero'}

try:
    arg = sys.argv[1]
except IndexError:
    print('ERROR: a word must be entered. Exiting...')
    sys.exit(0)

for i in arg.upper():
    try:
        print(d[i])
    except KeyError:
        pass

print('\"... read back, please.\"')
