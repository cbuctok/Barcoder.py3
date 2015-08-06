# encoding: utf-8
__author__ = 'Greg'

import csv, re, os


def return_analogs(search_what, search_in):
    s_to_return = ''
    just_model = ''.join(re.findall('([A-Za-z &]+)', search_what))
    for x, y in enumerate(search_in):
        if just_model in y:
            k = y.split(',')
            s_to_return += '{} - {} pair(s) for {}\n'.format(k[0], k[1], k[6]).replace('.00000000', '')

    return s_to_return


def disco(new_price):
    old_price = float(new_price[:-4])/0.8
    return '\tOLD PRICE: {} EUR'.format(old_price)


def printer(what_to_print):
    print('EAN:\t{}\nNAME:\t{}\nPRICE:\t{}{}\n\nDEPOT:\n{}'.format(what_to_print[1], what_to_print[4],
                                                                    what_to_print[10], disco(what_to_print[10]),
                                                                    return_analogs(what_to_print[4], ware)))


print('\nxXxXx Warehouse Check xXxXx\n')

try:
    with open('arts.csv', newline='', encoding='utf-8') as arts_file:
        csv_reader = csv.reader(arts_file)
        for row in csv_reader:
            # print(', '.join(row))
            list_of_arts = ['{}'.format(row.rstrip()) for row in arts_file]
        arts_file.close()
except Exception as exc:
    print('Can\'t open catalogue file\n{}'.format(exc))
    exit(0)

try:
    with open('warehouse.csv', newline='', encoding='utf-8') as warehouse_file:
        csv_reader = csv.reader(warehouse_file)
        for row in csv_reader:
            ware = ['{}'.format(row.rstrip()) for row in warehouse_file]
        warehouse_file.close()
except Exception as exc:
    print('Can\'t open warehouse file\n{}'.format(exc))
    exit(0)

# EAN_number = '8024820003326'
while True:
    EAN_number = input('Name or Barcode: ')
    os.system('cls')
    print('RESULTS\t{}:'.format(EAN_number))
    if any(EAN_number in s for s in list_of_arts):
        for gotcha in [s for s in list_of_arts if EAN_number in s]:
            printer(gotcha.split(','))
    else:
        print('NOT FOUND')
