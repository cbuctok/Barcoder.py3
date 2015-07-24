# encoding: utf-8

__author__ = 'Greg'

import subprocess, os, sys


def print_barcode(code_text):
    long_string = r'{0} -o "{2}{3}.png" -b 20 --height=50 --border=10 -d "{1}"'
    long_string = long_string.format(zint_exe, code_text, png_directory, code_text.replace(' ', '_'))
    subprocess.call(long_string.translate(str.maketrans('čćžšđČĆŽŠĐ','cczsdCCZSD')), shell=True)


def exception_handler(some_error):
    print('ERROR:\n{}'.format(some_error))
    a = input('Continue? y/n Default N[o]: ')
    if a == 'N' or 'n' or 'No' or 'no' or 'NO' or None:
        exit(0)
    if a == 'Y' or 'y' or 'Yes' or 'yes' or 'YES':
        pass
    else:
        exception_handler(some_error)

current_directory = os.getcwd()
zint_exe = os.path.dirname(os.path.realpath(__file__)) + '\\Zint\\zint'


if len(sys.argv) == 2:
    names_txt = sys.argv[1]
    current_directory = os.path.dirname(names_txt)
else:
    names_txt = current_directory + '\\name.txt'

if 'System32' in current_directory:
    current_directory = 'C:'
png_directory = current_directory + '\\barcode\\'

try:
    with open(names_txt, 'r', encoding='utf-8') as file_to_code:
        for line in file_to_code:
            list_of_names = ['{}'.format(line.rstrip()) for line in file_to_code]
        file_to_code.close()
except Exception as exc:
    exception_handler('Is it a non-empty text file?\n{}'.format(exc))

if not os.path.exists(png_directory):
    os.makedirs(png_directory)

for line in list_of_names:
    try:
        print_barcode(line)
    except Exception as exc:
        exception_handler(exc)

