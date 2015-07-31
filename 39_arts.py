# encoding: utf-8
__author__ = 'Greg'
import csv, os, sys, subprocess


def print_barcode(ean='', name=''):
    if os.path.isfile('{}{}'.format(png_directory, name)):
        name = '.{}'.format(name)
    long_string = r'{0} -o "{2}{3}.png" -b 9 --height=50 --border=10 -d "{1}"'  # CODE 93 = b 25 CODE 39 = b 9
    long_string = long_string.format(zint_exe, ean, png_directory, name)
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
zint_exe = os.path.dirname(os.path.realpath(__file__)) + r'\Zint\zint'
arts_csv = os.path.dirname(os.path.realpath(__file__)) + r'\arts.csv'

try:
    with open(arts_csv, newline='', encoding='utf-8') as arts_file:
        csv_reader = csv.reader(arts_file)
        for row in csv_reader:
            list_of_arts = ['{}'.format(row.rstrip()) for row in arts_file]
        arts_file.close()
except Exception as exc:
    print('Can\'t open catalogue file\n{}'.format(exc))
    exit(0)

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
            list_from_txt = ['{}'.format(line.rstrip()) for line in file_to_code]
        file_to_code.close()
except Exception as exc:
    exception_handler('Is it a non-empty text file?\n{}'.format(exc))
    exit(0)

if not os.path.exists(png_directory):
    os.makedirs(png_directory)

for name_from_txt in list_from_txt:
    try:
        if any(name_from_txt in s for s in list_of_arts):
            for gotcha in [s for s in list_of_arts if name_from_txt in s]:
                print_barcode(gotcha.split(',')[1], gotcha.split(',')[4])  # EAN 1, NAME 4
        else:
            print('NOT FOUND')
    except Exception as exc:
        exception_handler(exc)
