from bs4 import BeautifulSoup
import urllib.request
import os
from tabula import read_pdf
import requests
import numpy as np
import pandas as pd
from tabulate import tabulate
import json
import requests, PyPDF2, io
import re
import bs4
import sys
import time
from collections import namedtuple
import datetime
import os
import glob
import shutil
import urllib.request
import re
import csv
import pdfbox
from lxml import html
from mortgage_scraper import *
from loans_scraper import *

#!/usr/bin/env python
__author__ = "Issye Margaretha Kamal"
__copyright__ = "Copyright 2019, Top Compare Scraping Tool"
__credits__ = ["Top Compare"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Issye Margaretha Kamal"
__email__ = "issye.kamal@topcompare.be"
__status__ = "Production"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

###
# Start application flow
def Start(self):

    logger.info(Back.LIGHTCYAN_EX + "Scraping Tool" + Style.RESET_ALL + " (version {version} R{release})".format(version=Conf.VERSION,
                                                                                                                            release=Conf.RELEASE))
print("""
_     _ _    _                                                                                         
| |   | (_)  | |                                                                                        
| |__ | |_   | |                                                                                        
|  __)| | |  |_|                                                                                        
| |   | | |   _                                                                                         
|_|   |_|_|  |_|                                                                                        
 _______ _     _         _         _______             ______                                      _    
(_______) |   (_)       (_)       (_______)           / _____)                                    ( )   
 _      | | _  _  ___    _  ___    _       ___  ____ | /      ___  ____  ____   ____  ____ ____   |/___ 
| |     | || \| |/___)  | |/___)  | |     / _ \|  _ \| |     / _ \|    \|  _ \ / _  |/ ___) _  )   /___)
| |_____| | | | |___ |  | |___ |  | |____| |_| | | | | \____| |_| | | | | | | ( ( | | |  ( (/ /   |___ |
 \______)_| |_|_(___/   |_(___/    \______)___/| ||_/ \______)___/|_|_|_| ||_/ \_||_|_|   \____)  (___/ 
                                               |_|                      |_|                             
  ______                  _ _                _______            _                                       
 / _____)                | (_)              (_______)          | |                                      
| /       ____ ____ _ _ _| |_ ____   ____    _       ___   ___ | |                                      
| |      / ___) _  | | | | | |  _ \ / _  |  | |     / _ \ / _ \| |                                      
| \_____| |  ( ( | | | | | | | | | ( ( | |  | |____| |_| | |_| | |                                      
 \______)_|   \_||_|\____|_|_|_| |_|\_|| |   \______)___/ \___/|_|                                      
                                   (_____|                            
""")

today_string = datetime.datetime.today().strftime('%x')


def menu(message, options, prompt):
    print('')
    print('>>> ' + message)
    for option in options:
        """ :type option:MenuOption """
        print("{id}: {name}".format(id=option.id,
              name=option.name))
    correctInput = False
    choice = 0
    while not correctInput:
        choice = inputPrompt(prompt).strip()
        correctInput = choice.isdigit()
    return int(choice)


def inputPrompt(text):
    return input('>>> ' + text)


def menu(message, options, prompt):
    print('')
    print('>>> ' + message)
    for option in options:
        """ :type option:MenuOption """
        print("{id}: {name}".format(id=option.id,
              name=option.name))
    correctInput = False
    choice = 0
    while not correctInput:
        choice = inputPrompt(prompt).strip()
        correctInput = choice.isdigit()
    return int(choice)



MenuOption = namedtuple('MenuOption', 'id, name')

###### Save to "History" folder and overwrite the today.csv file ##########

list_of_files = glob.glob("/**/*/*/*/TC_Crawling Tool/History/*.csv") # * means all if need specific format then *.csv
last_file = max(list_of_files, key=os.path.getctime) #find the name of the latest run
base_name_ext = os.path.basename(last_file) #assign the name of the latest file
base_name = os.path.splitext(base_name_ext)[0]

def last():
    path = os.path.abspath("History")
    newPath = os.path.abspath("")
    count = 1

    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith(base_name_ext):
                shutil.copy(os.path.join(root, i), os.path.join(newPath, "last" + ".csv"))
                print("Successfuly save file to the folder. Please check")
                count += 1

last()

print("The latest time you run this program is at:", base_name)



proceed_choice = int(menu('Do you want to proceed?',
                                    [MenuOption(0, 'Proceed'),
                                     MenuOption(1, 'No')],
                                    'Please enter what you would like to do: '))

loans_choice = int(menu('Which vertical would you like to scrape?',
                                    [MenuOption(0, 'Personal, Vehicle, Renovation Loan'),
                                     MenuOption(1, 'Home Loan')],
                                    'Please enter what you would like to do: '))

if proceed_choice == 0 and loans_choice == 1:
    last()
    provider_choice = int(menu('Which HL provider would you like to scrape?',
                                    [MenuOption(0, 'ALL'),
                                     MenuOption(1, 'Argenta'),
                                     MenuOption(2, 'Banque Van Breda'),
                                     MenuOption(3, 'BPost'),
                                     MenuOption(4, 'Belfius'),
                                     MenuOption(5, 'BNP Paribas Fortis'),
                                     MenuOption(6, 'CBC'),
                                     MenuOption(7, 'CPH'),
                                     MenuOption(8, 'Crelan'),
                                     MenuOption(9, 'Elantis'),
                                     MenuOption(10, 'Federale'),
                                     MenuOption(11, 'Hellobank'),
                                     MenuOption(12, 'ING'),
                                     MenuOption(13, 'KBC'),
                                     MenuOption(14, 'Keytrade'),
                                     MenuOption(15, 'Nagelmackers'),
                                     MenuOption(16, 'Triodos')],
                                    'Please enter what you would like to do: '))
elif proceed_choice == 0 and loans_choice == 0:
    last()
    provider_choice_2 = int(menu('Which PL/CL/RL provider would you like to scrape?',
                               [MenuOption(0, 'ALL'),
                                MenuOption(1, 'Argenta'),
                                MenuOption(2, 'Auxifina'),
                                MenuOption(3, 'AXA Bank'),
                                MenuOption(4, 'Belfius'),
                                MenuOption(5, 'Beobank'),
                                MenuOption(6, 'BPost'),
                                MenuOption(7, 'BuyWay'),
                                MenuOption(8, 'Elantis'),
                                MenuOption(9, 'Europabank'),
                                MenuOption(10, 'Leemans Kredieten'),
                                MenuOption(11, 'Mozzeno'),
                                MenuOption(12, 'Santander')],
                               'Please enter what you would like to do: '))
else:
    exit()

print("Please wait... We are currently retrieving prices from provider's website")


if loans_choice == 1 and provider_choice == 0:
    all()
elif loans_choice == 1 and provider_choice == 1:
    argenta_save()
elif loans_choice == 1 and provider_choice == 2:
    bvbr_save()
elif loans_choice == 1 and provider_choice == 3:
    bpost_save()
elif loans_choice == 1 and provider_choice == 4:
    belfius_save()
elif loans_choice == 1 and provider_choice == 5:
    bnpf_save()
elif loans_choice == 1 and provider_choice == 6:
    cbc_save()
elif loans_choice == 1 and provider_choice == 7:
    cph_save()
elif loans_choice == 1 and provider_choice == 8:
    crelan_save()
elif loans_choice == 1 and provider_choice == 9:
    elan_save()
elif loans_choice == 1 and provider_choice == 10:
    federale_save()
elif loans_choice == 1 and provider_choice == 11:
    hellobank_save()
elif loans_choice == 1 and provider_choice == 12:
    ing_save()
elif loans_choice == 1 and provider_choice == 13:
    kbc_save()
elif loans_choice == 1 and provider_choice == 14:
    keytrade_save()
elif loans_choice == 1 and provider_choice == 15:
    nage_save()
elif loans_choice == 1 and provider_choice == 16:
    trio_save()


if loans_choice == 0 and provider_choice_2 == 0:
    all_loans()
elif loans_choice == 0 and provider_choice_2 == 1:
    argenta_save_loans()
elif loans_choice == 0 and provider_choice_2 == 2:
    auxifina_save_loans()
elif loans_choice == 0 and provider_choice_2 == 3:
    axabank_save_loans()
elif loans_choice == 0 and provider_choice_2 == 4:
    belfius_save_loans()
elif loans_choice == 0 and provider_choice_2 == 5:
    beobank_save_loans()
elif loans_choice == 0 and provider_choice_2 == 6:
    bpost_save_loans()
elif loans_choice == 0 and provider_choice_2 == 7:
    buyway_save_loans()
elif loans_choice == 0 and provider_choice_2 == 8:
    elantis_save_loans()
elif loans_choice == 0 and provider_choice_2 == 9:
    europabank_save_loans()
elif loans_choice == 0 and provider_choice_2 == 10:
    leemans_save_loans()
elif loans_choice == 0 and provider_choice_2 == 11:
    mozzeno_save_loans()
elif loans_choice == 0 and provider_choice_2 == 12:
    santander_save_loans()
else:
    exit()




###### Save to "History" folder and overwrite the today.csv file ##########

filex = glob.glob("/**/*/*/*/TC_Crawling Tool/History/*.csv") # * means all if need specific format then *.csv
tod_file = max(filex, key=os.path.getctime) #find the name of the latest run
today_file = os.path.basename(tod_file) #assign the name of the latest file

def today():
    path = os.path.abspath("History")
    newPath = os.path.abspath("")
    count = 1

    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith(today_file):
                shutil.copy(os.path.join(root, i), os.path.join(newPath, "today" + ".csv"))
                print("Successfuly save file to the folder. Please check")
                count += 1

today()

####### Compare the file runned before with now ##########

with open(os.path.abspath('today.csv'), 'r') as t1, open(os.path.abspath('last.csv'), 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)

