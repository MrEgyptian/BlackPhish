# Source Generated with Decompyle++
# File: startup.pyc (Python 3.8)

import os
import time
red = '\x1b[1;91m'
green = '\x1b[1;92m'
yellow = '\x1b[1;93m'
blue = '\x1b[1;94m'

def slow(O000000O0O0000000, O0000O0O000OO0000):
    OO0O000O0O000000O = 0
    while OO0O000O0O000000O < len(O000000O0O0000000):
        time.sleep(O0000O0O000OO0000)
        print(O000000O0O0000000[OO0O000O0O000000O], end=str(), flush=True)
        OO0O000O0O000000O = OO0O000O0O000000O + 1
        continue


def soon():
    slow('\n                        \xe2\x96\x80                 \n  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84   \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84 \xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 \n \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x80  \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88    \xe2\x96\x88    \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88 \n \xe2\x96\x88      \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88    \xe2\x96\x88    \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88   \xe2\x96\x88 \n \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x88  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88 \n                                     \xe2\x96\x84  \xe2\x96\x88 \n                                      \xe2\x96\x80\xe2\x96\x80                           \n  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84   \xe2\x96\x84 \xe2\x96\x84\xe2\x96\x84  \n \xe2\x96\x88   \xe2\x96\x80  \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88 \n  \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84  \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x88   \xe2\x96\x88 \n \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88   \xe2\x96\x88 \xe2\x96\x84 \xe2\x96\x84 \xe2\x96\x84 \xe2\x96\x84 \xe2\x96\x84 \xe2\x96\x84 \xe2\x96\x84  \n', 0.00025)


def slogo():
    OO0OOOO00O000OO0O = b'\n____________________________________\n| \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x80\xe2\x96\x80\xe2\x96\x88                  \xe2\x96\x88     |\n| \xe2\x96\x88    \xe2\x96\x88   \xe2\x96\x88     \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84   \xe2\x96\x88   \xe2\x96\x84 |\n| \xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80   \xe2\x96\x88    \xe2\x96\x80   \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x80  \xe2\x96\x88 \xe2\x96\x84\xe2\x96\x80  |\n| \xe2\x96\x88    \xe2\x96\x88   \xe2\x96\x88    \xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88  \xe2\x96\x88      \xe2\x96\x88\xe2\x96\x80\xe2\x96\x88   |\n| \xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80   \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80  \xe2\x96\x88  \xe2\x96\x80\xe2\x96\x84 |\n|                                   |\n| \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x88        \xe2\x96\x80           \xe2\x96\x88     |\n| \xe2\x96\x88   \xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88 \xe2\x96\x84\xe2\x96\x84   \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84     \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84   \xe2\x96\x88 \xe2\x96\x84\xe2\x96\x84  |\n| \xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88    \xe2\x96\x88    \xe2\x96\x88   \xe2\x96\x80  \xe2\x96\x88\xe2\x96\x80  \xe2\x96\x88 |\n| \xe2\x96\x88      \xe2\x96\x88   \xe2\x96\x88    \xe2\x96\x88     \xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84  \xe2\x96\x88   \xe2\x96\x88 |\n| \xe2\x96\x88      \xe2\x96\x88   \xe2\x96\x88  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84  \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80  \xe2\x96\x88   \xe2\x96\x88 |\n ------------------------------------\n'.decode()
    #print(OO0OOOO00O000OO0O)
    OOO0O0O0O00000OO0 = '\x1b[1;92m#'
    slow(OO0OOOO00O000OO0O, 0.00025)
    print(OOO0O0O0O00000OO0 * 37)
    slow(OOO0O0O0O00000OO0 * 2 + '         ' + '\x1b[1;91m Coded By \x1b[1;94mAhmed' + '         ' + OOO0O0O0O00000OO0 * 2 + '\n', 0.0025)
    slow(OOO0O0O0O00000OO0 * 2 + '         ' + '\x1b[1;91mVersion \x1b[1;92m1.0\x1b[1;94m     ' + '        ' + OOO0O0O0O00000OO0 * 2 + '\n', 0.025)
    slow(OOO0O0O0O00000OO0 * 2 + '  ' + red + 'Whatsapp:' + green + 'wa.me/+201150119895 ' + '  ' + OOO0O0O0O00000OO0 * 2 + '\n', 0.0025)
    slow(OOO0O0O0O00000OO0 * 2 + ' ' + red + 'GitHub:' + yellow + 'GitHub.com/AhmedmAhmed8a' + ' ' + OOO0O0O0O00000OO0 * 2 + '\n', 0.005)
    print(OOO0O0O0O00000OO0 * 37)
    return OO0OOOO00O000OO0O

