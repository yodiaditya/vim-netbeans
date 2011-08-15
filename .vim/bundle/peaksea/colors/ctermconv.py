#!/usr/bin/python

import re

def check_level(value):
    "for xterm standard style: 005f87afd7ff"
    if (value < 0x30):
        return 0
    elif (value < 0x73):
        return 1
    elif (value < 0x9b):
        return 2
    elif (value < 0xc3):
        return 3
    elif (value < 0xeb):
        return 4
    else:
        return 5

def check_level_k(value):
    "for Konsole and rxvt style: 00336699ccff"
    if (value < 0x1a):
        return 0
    elif (value < 0x4d):
        return 1
    elif (value < 0x80):
        return 2
    elif (value < 0xb3):
        return 3
    elif (value < 0xe6):
        return 4
    else:
        return 5

def level_index(level_r, level_g, level_b, isgrey=0):
    if isgrey:
        if level_r < 4:
            return 16
        elif level_r >= 0xf6:
            return 231
        elif level_r >= 233:
            return 255
        else:
            return ((level_r-3)/10)+232;
    else:
        return 16 + level_r*6*6 + level_g*6 + level_b;

def calc_index(rgb):
    r = eval('0x' + rgb[0:2])
    g = eval('0x' + rgb[2:4])
    b = eval('0x' + rgb[4:6])
    if r==g and g==b:
        index = level_index(r, g, b, 1)
    else:
        index = level_index(check_level(r), check_level(g), check_level(b))
    return index

import sys

argc = len(sys.argv)
if argc==1:
    filename = 'peaksea_t.vim'
else:
    filename = sys.argv[1]

try:
    infile = open(filename, 'r')

    try:
        outfile = open(filename[:-6]+'.vim', 'w')
        print 'Now convert file', filename, 'to', outfile.name
        pattern = re.compile('![a-fA-F0-9]{6}')
        for line in infile:
            matchlist = re.findall(pattern, line)
            if matchlist:
                replaced_line = line
                for matchpattern in matchlist:
                    index = calc_index(matchpattern[1:])
                    replaced_line = re.sub(matchpattern, str(index), replaced_line)
                outfile.write(replaced_line)
            else:
                outfile.write(line)

        outfile.close()
    except IOError:
        print 'cannot open file', outfile
    infile.close()

except IOError:
    print 'cannot open file', filename


