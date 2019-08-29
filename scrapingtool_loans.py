from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
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
import shutil
import urllib.request
import re
import csv
from lxml import html



# #    /\                          _          # #
# #   /  \   ____ ____  ____ ____ | |_  ____  # #
# #  / /\ \ / ___) _  |/ _  )  _ \|  _)/ _  | # #
# # | |__| | |  ( ( | ( (/ /| | | | |_( ( | | # #
# # |______|_|   \_|| |\____)_| |_|\___)_||_| # #
# #             (_____|                       # #
# #                                           # #

def argenta_loans():
    try:
        global arge_loans_c

    ###############################################################################################################
    ############################################ARGE0001###########################################################

        arge0001_url = 'https://action.argenta.be/pret-auto/?utm_source=site&utm_medium=pa_autolening&utm_content=2018fr&utm_campaign=autolening#simulator'
        arge0001_htmlcode = requests.get(arge0001_url)
        arge0001_soup = bs4.BeautifulSoup(arge0001_htmlcode.content, 'lxml')
        arge0001_content = arge0001_soup.find_all('h2', {'class': "gsection_title"})
        arge0001_content2 = str(str(arge0001_content).split())

        ### look for minimum and maximum amount
        for item in arge0001_content2:
            min_arge0001_1 = re.findall(r"'tussen', '(.*?)',", arge0001_content2)
            min_arge0001_2_5 = re.findall(r"van',.'(.*?)'", arge0001_content2)
            min_arge0001_6 = re.findall(r"dan',.'(.*?)'", arge0001_content2)[0]
            min_arge0001_6 = [min_arge0001_6]  # convert from str to a list

            max_arge0001_1 = re.findall(r"'en',.'(.*?)<.h2.", arge0001_content2)
            max_arge0001_2_5 = re.findall(r"'-',.'(.*?)', 'euro<.h2>", arge0001_content2)
            max_arge0001_6 = ['50.000']

            min_arge0001 = min_arge0001_1 + min_arge0001_2_5 + min_arge0001_6  # This is to append a list
            max_arge0001 = max_arge0001_1 + max_arge0001_2_5 + max_arge0001_6

        ### look for minimum and maximum months, loop is not applied since we would like to capture each term changes

        term_arge0001_1 = arge0001_soup.find_all('select', {'name': "input_122"})
        term_arge0001_2 = arge0001_soup.find_all('select', {'name': "input_121"})
        term_arge0001_3 = arge0001_soup.find_all('select', {'name': "input_120"})
        term_arge0001_4 = arge0001_soup.find_all('select', {'name': "input_119"})
        term_arge0001_5 = arge0001_soup.find_all('select', {'name': "input_118"})
        term_arge0001_6 = arge0001_soup.find_all('select', {'name': "input_117"})
        term_arge0001_7 = arge0001_soup.find_all('select', {'name': "input_113"})

        term_arge0001_1 = str(str(term_arge0001_1).split())
        term_arge0001_2 = str(str(term_arge0001_2).split())
        term_arge0001_3 = str(str(term_arge0001_3).split())
        term_arge0001_4 = str(str(term_arge0001_4).split())
        term_arge0001_5 = str(str(term_arge0001_5).split())
        term_arge0001_6 = str(str(term_arge0001_6).split())
        term_arge0001_7 = str(str(term_arge0001_7).split())

        for item in term_arge0001_1:
            minterm_arge0001_1 = re.findall(r'value="(.*?)"', term_arge0001_1)[0]
            maxterm_arge0001_1 = re.findall(r'value="(.*?)"', term_arge0001_1)[-1]
        for item in term_arge0001_2:
            minterm_arge0001_2 = re.findall(r'value="(.*?)"', term_arge0001_2)[0]
            maxterm_arge0001_2 = re.findall(r'value="(.*?)"', term_arge0001_2)[-1]
        for item in term_arge0001_3:
            minterm_arge0001_3 = re.findall(r'value="(.*?)"', term_arge0001_3)[0]
            maxterm_arge0001_3 = re.findall(r'value="(.*?)"', term_arge0001_3)[-1]
        for item in term_arge0001_4:
            minterm_arge0001_4 = re.findall(r'value="(.*?)"', term_arge0001_4)[0]
            maxterm_arge0001_4 = re.findall(r'value="(.*?)"', term_arge0001_4)[-1]
        for item in term_arge0001_5:
            minterm_arge0001_5 = re.findall(r'value="(.*?)"', term_arge0001_5)[0]
            maxterm_arge0001_5 = re.findall(r'value="(.*?)"', term_arge0001_5)[-1]
        for item in term_arge0001_6:
            minterm_arge0001_6 = re.findall(r'value="(.*?)"', term_arge0001_6)[0]
            maxterm_arge0001_6 = re.findall(r'value="(.*?)"', term_arge0001_6)[-1]
        for item in term_arge0001_7:
            minterm_arge0001_7 = re.findall(r'value="(.*?)"', term_arge0001_7)[0]
            maxterm_arge0001_7 = re.findall(r'value="(.*?)"', term_arge0001_7)[-1]

        minterm_arge0001 = [minterm_arge0001_1, minterm_arge0001_2, minterm_arge0001_3, minterm_arge0001_4, minterm_arge0001_5, minterm_arge0001_6, minterm_arge0001_7]  # append string into a list
        maxterm_arge0001 = [maxterm_arge0001_1, maxterm_arge0001_2, maxterm_arge0001_3, maxterm_arge0001_4, maxterm_arge0001_5, maxterm_arge0001_6, maxterm_arge0001_7]

        # ### look for TAEG

        arge0001_content_taeg = arge0001_soup.find_all('input', {'name': "input_9"})
        TAEG_arge0001 = str(str(arge0001_content_taeg).split())  # change the type to str so we can parse using RegEx

        for item in TAEG_arge0001:
            TAEG_argenta_1 = re.findall(r'choice_12_9_1".*value="(.*)".>.*choice_12_9_2', TAEG_arge0001)
        TAEG_arge0001 = TAEG_argenta_1 * 7  # times the number of total elements

        ### transform matrix
        arge0001_array = np.column_stack((min_arge0001, max_arge0001, minterm_arge0001, maxterm_arge0001, TAEG_arge0001))
        arge0001_tup = tuple(map(tuple, arge0001_array))

        ##########convert everything into a panda df##########

        Min_arge0001 = pd.DataFrame(min_arge0001, columns=['Min'])
        Max_arge0001 = pd.DataFrame(max_arge0001, columns=['Max'])
        amount_arge0001 = Min_arge0001.join(Max_arge0001)

        MinTerm_arge0001 = pd.DataFrame(minterm_arge0001, columns=['Min Term'])
        MaxTerm_arge0001 = pd.DataFrame(maxterm_arge0001, columns=['Max Term'])
        duration_arge0001 = MinTerm_arge0001.join(MaxTerm_arge0001)

        Taux_arge0001 = pd.DataFrame(TAEG_arge0001, columns=['Taux'])

        df_arge0001 = amount_arge0001.join(duration_arge0001)
        df_arge0001 = df_arge0001.join(Taux_arge0001)

        df_arge0001.insert(0, 'Provider', 'Argenta')
        df_arge0001.insert(1, 'Product_ID', 'ARGE0001')
        df_arge0001.insert(1, 'Category', 'Vehicle Loan')

        df_arge0001_vl = df_arge0001[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################ARGE0002###########################################################

        ### the difference between ARGE0002 and ARGE0001 is only in TAEG, but below codes are required to create independencies

        arge0002_url = 'https://action.argenta.be/pret-auto/?utm_source=site&utm_medium=pa_autolening&utm_content=2018fr&utm_campaign=autolening#simulator'
        arge0002_htmlcode = requests.get(arge0002_url)
        arge0002_soup = bs4.BeautifulSoup(arge0002_htmlcode.content, 'lxml')
        arge0002_content = arge0002_soup.find_all('h2', {'class': "gsection_title"})
        arge0002_content2 = str(str(arge0002_content).split())

        ### look for minimum and maximum amount
        for item in arge0002_content2:
            min_arge0002_1 = re.findall(r"'tussen', '(.*?)',", arge0002_content2)
            min_arge0002_2_5 = re.findall(r"van',.'(.*?)'", arge0002_content2)
            min_arge0002_6 = re.findall(r"dan',.'(.*?)'", arge0002_content2)[0]
            min_arge0002_6 = [min_arge0002_6]  # convert from str to a list

            max_arge0002_1 = re.findall(r"'en',.'(.*?)<.h2.", arge0002_content2)
            max_arge0002_2_5 = re.findall(r"'-',.'(.*?)', 'euro<.h2>", arge0002_content2)
            max_arge0002_6 = ['50.000']

            min_arge0002 = min_arge0002_1 + min_arge0002_2_5 + min_arge0002_6  # This is to append a list
            max_arge0002 = max_arge0002_1 + max_arge0002_2_5 + max_arge0002_6

        ### look for minimum and maximum months, loop is not applied since we would like to capture each term changes

        term_arge0002_1 = arge0002_soup.find_all('select', {'name': "input_122"})
        term_arge0002_2 = arge0002_soup.find_all('select', {'name': "input_121"})
        term_arge0002_3 = arge0002_soup.find_all('select', {'name': "input_120"})
        term_arge0002_4 = arge0002_soup.find_all('select', {'name': "input_119"})
        term_arge0002_5 = arge0002_soup.find_all('select', {'name': "input_118"})
        term_arge0002_6 = arge0002_soup.find_all('select', {'name': "input_117"})
        term_arge0002_7 = arge0002_soup.find_all('select', {'name': "input_113"})

        term_arge0002_1 = str(str(term_arge0002_1).split())
        term_arge0002_2 = str(str(term_arge0002_2).split())
        term_arge0002_3 = str(str(term_arge0002_3).split())
        term_arge0002_4 = str(str(term_arge0002_4).split())
        term_arge0002_5 = str(str(term_arge0002_5).split())
        term_arge0002_6 = str(str(term_arge0002_6).split())
        term_arge0002_7 = str(str(term_arge0002_7).split())

        for item in term_arge0002_1:
            minterm_arge0002_1 = re.findall(r'value="(.*?)"', term_arge0002_1)[0]
            maxterm_arge0002_1 = re.findall(r'value="(.*?)"', term_arge0002_1)[-1]
        for item in term_arge0002_2:
            minterm_arge0002_2 = re.findall(r'value="(.*?)"', term_arge0002_2)[0]
            maxterm_arge0002_2 = re.findall(r'value="(.*?)"', term_arge0002_2)[-1]
        for item in term_arge0002_3:
            minterm_arge0002_3 = re.findall(r'value="(.*?)"', term_arge0002_3)[0]
            maxterm_arge0002_3 = re.findall(r'value="(.*?)"', term_arge0002_3)[-1]
        for item in term_arge0002_4:
            minterm_arge0002_4 = re.findall(r'value="(.*?)"', term_arge0002_4)[0]
            maxterm_arge0002_4 = re.findall(r'value="(.*?)"', term_arge0002_4)[-1]
        for item in term_arge0002_5:
            minterm_arge0002_5 = re.findall(r'value="(.*?)"', term_arge0002_5)[0]
            maxterm_arge0002_5 = re.findall(r'value="(.*?)"', term_arge0002_5)[-1]
        for item in term_arge0002_6:
            minterm_arge0002_6 = re.findall(r'value="(.*?)"', term_arge0002_6)[0]
            maxterm_arge0002_6 = re.findall(r'value="(.*?)"', term_arge0002_6)[-1]
        for item in term_arge0002_7:
            minterm_arge0002_7 = re.findall(r'value="(.*?)"', term_arge0002_7)[0]
            maxterm_arge0002_7 = re.findall(r'value="(.*?)"', term_arge0002_7)[-1]

        minterm_arge0002 = [minterm_arge0002_1, minterm_arge0002_2, minterm_arge0002_3, minterm_arge0002_4, minterm_arge0002_5, minterm_arge0002_6, minterm_arge0002_7]  # append string into a list
        maxterm_arge0002 = [maxterm_arge0002_1, maxterm_arge0002_2, maxterm_arge0002_3, maxterm_arge0002_4, maxterm_arge0002_5, maxterm_arge0002_6, maxterm_arge0002_7]

        # ### look for TAEG

        arge0002_content_taeg = arge0002_soup.find_all('input', {'name': "input_9"})
        TAEG_arge0002 = str(str(arge0002_content_taeg).split())  # change the type to str so we can parse using RegEx

        for item in TAEG_arge0002:
            TAEG_argenta_2 = re.findall(r'choice_12_9_2".*value="(.*)".>.*', TAEG_arge0002)
        TAEG_arge0002 = TAEG_argenta_2 * 7  # times the number of total elements

        ### transform matrix
        arge0002_array = np.column_stack((min_arge0002, max_arge0002, minterm_arge0002, maxterm_arge0002, TAEG_arge0002))
        arge0002_tup = tuple(map(tuple, arge0002_array))

        ##########convert everything into a panda df##########

        Min_arge0002 = pd.DataFrame(min_arge0002, columns=['Min'])
        Max_arge0002 = pd.DataFrame(max_arge0002, columns=['Max'])
        amount_arge0002 = Min_arge0001.join(Max_arge0002)

        MinTerm_arge0002 = pd.DataFrame(minterm_arge0002, columns=['Min Term'])
        MaxTerm_arge0002 = pd.DataFrame(maxterm_arge0002, columns=['Max Term'])
        duration_arge0002 = MinTerm_arge0002.join(MaxTerm_arge0002)

        Taux_arge0002 = pd.DataFrame(TAEG_arge0002, columns=['Taux'])

        df_arge0002 = amount_arge0002.join(duration_arge0002)
        df_arge0002 = df_arge0002.join(Taux_arge0002)

        df_arge0002.insert(0, 'Provider', 'Argenta')
        df_arge0002.insert(1, 'Product_ID', 'ARGE0002')
        df_arge0002.insert(1, 'Category', 'Vehicle Loan')

        df_arge0002_vl = df_arge0002[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################ARGE0003###########################################################

        arge0003_url = 'https://action.argenta.be/pret-renovation/?utm_source=site&utm_medium=pa_renovatielening&utm_content=2018fr&utm_campaign=renovatielening#simulator'
        arge0003_htmlcode = requests.get(arge0003_url)
        arge0003_soup = bs4.BeautifulSoup(arge0003_htmlcode.content, 'lxml')
        arge0003_content = arge0003_soup.find_all('h2', {'class': "gsection_title"})
        arge0003_content2 = str(str(arge0003_content).split())

        ### look for minimum and maximum amount
        for item in arge0003_content2:
            min_arge0003_1 = re.findall(r"'tussen', '(.*?)',", arge0003_content2)
            min_arge0003_2_5 = re.findall(r"van',.'(.*?)'", arge0003_content2)
            min_arge0003_6 = re.findall(r"dan',.'(.*?)'", arge0003_content2)[0]
            min_arge0003_6 = [min_arge0003_6]  # convert from str to a list

            max_arge0003_1 = re.findall(r"'en',.'(.*?)<.h2.", arge0003_content2)
            max_arge0003_2_5 = re.findall(r"'-',.'(.*?)', 'euro<.h2>", arge0003_content2)
            max_arge0003_6 = ['50.000']

            min_arge0003 = min_arge0003_1 + min_arge0003_2_5 + min_arge0003_6  # This is to append a list
            max_arge0003 = max_arge0003_1 + max_arge0003_2_5 + max_arge0003_6

        ### look for minimum and maximum months, loop is not applied since we would like to capture each term changes

        term_arge0003_1 = arge0003_soup.find_all('select', {'name': "input_122"})
        term_arge0003_2 = arge0003_soup.find_all('select', {'name': "input_121"})
        term_arge0003_3 = arge0003_soup.find_all('select', {'name': "input_120"})
        term_arge0003_4 = arge0003_soup.find_all('select', {'name': "input_119"})
        term_arge0003_5 = arge0003_soup.find_all('select', {'name': "input_118"})
        term_arge0003_6 = arge0003_soup.find_all('select', {'name': "input_117"})
        term_arge0003_7 = arge0003_soup.find_all('select', {'name': "input_113"})

        term_arge0003_1 = str(str(term_arge0003_1).split())
        term_arge0003_2 = str(str(term_arge0003_2).split())
        term_arge0003_3 = str(str(term_arge0003_3).split())
        term_arge0003_4 = str(str(term_arge0003_4).split())
        term_arge0003_5 = str(str(term_arge0003_5).split())
        term_arge0003_6 = str(str(term_arge0003_6).split())
        term_arge0003_7 = str(str(term_arge0003_7).split())

        for item in term_arge0003_1:
            minterm_arge0003_1 = re.findall(r'value="(.*?)"', term_arge0003_1)[0]
            maxterm_arge0003_1 = re.findall(r'value="(.*?)"', term_arge0003_1)[-1]
        for item in term_arge0003_2:
            minterm_arge0003_2 = re.findall(r'value="(.*?)"', term_arge0003_2)[0]
            maxterm_arge0003_2 = re.findall(r'value="(.*?)"', term_arge0003_2)[-1]
        for item in term_arge0003_3:
            minterm_arge0003_3 = re.findall(r'value="(.*?)"', term_arge0003_3)[0]
            maxterm_arge0003_3 = re.findall(r'value="(.*?)"', term_arge0003_3)[-1]
        for item in term_arge0003_4:
            minterm_arge0003_4 = re.findall(r'value="(.*?)"', term_arge0003_4)[0]
            maxterm_arge0003_4 = re.findall(r'value="(.*?)"', term_arge0003_4)[-1]
        for item in term_arge0003_5:
            minterm_arge0003_5 = re.findall(r'value="(.*?)"', term_arge0003_5)[0]
            maxterm_arge0003_5 = re.findall(r'value="(.*?)"', term_arge0003_5)[-1]
        for item in term_arge0003_6:
            minterm_arge0003_6 = re.findall(r'value="(.*?)"', term_arge0003_6)[0]
            maxterm_arge0003_6 = re.findall(r'value="(.*?)"', term_arge0003_6)[-1]
        for item in term_arge0003_7:
            minterm_arge0003_7 = re.findall(r'value="(.*?)"', term_arge0003_7)[0]
            maxterm_arge0003_7 = re.findall(r'value="(.*?)"', term_arge0003_7)[-1]

        minterm_arge0003 = [minterm_arge0003_1, minterm_arge0003_2, minterm_arge0003_3, minterm_arge0003_4, minterm_arge0003_5, minterm_arge0003_6, minterm_arge0003_7]  # append string into a list
        maxterm_arge0003 = [maxterm_arge0003_1, maxterm_arge0003_2, maxterm_arge0003_3, maxterm_arge0003_4, maxterm_arge0003_5, maxterm_arge0003_6, maxterm_arge0003_7]

        # ### look for TAEG

        arge0003_content_taeg = arge0003_soup.find_all('input', {'name': "input_9"})
        TAEG_arge0003 = str(str(arge0003_content_taeg).split())  # change the type to str so we can parse using RegEx

        for item in TAEG_arge0003:
            TAEG_argenta_3 = re.findall(r'choice_11_9_0.*value="(.*?)".>.*choice_11_9_1', TAEG_arge0003)
        TAEG_arge0003 = TAEG_argenta_3 * 7  # times the number of total elements

        ### transform matrix
        arge0003_array = np.column_stack((min_arge0003, max_arge0003, minterm_arge0003, maxterm_arge0003, TAEG_arge0003))
        arge0003_tup = tuple(map(tuple, arge0003_array))

        ##########convert everything into a panda df##########

        Min_arge0003 = pd.DataFrame(min_arge0003, columns=['Min'])
        Max_arge0003 = pd.DataFrame(max_arge0003, columns=['Max'])
        amount_arge0003 = Min_arge0003.join(Max_arge0003)

        MinTerm_arge0003 = pd.DataFrame(minterm_arge0003, columns=['Min Term'])
        MaxTerm_arge0003 = pd.DataFrame(maxterm_arge0003, columns=['Max Term'])
        duration_arge0003 = MinTerm_arge0003.join(MaxTerm_arge0003)

        Taux_arge0003 = pd.DataFrame(TAEG_arge0003, columns=['Taux'])

        df_arge0003 = amount_arge0003.join(duration_arge0003)
        df_arge0003 = df_arge0003.join(Taux_arge0003)

        df_arge0003.insert(0, 'Provider', 'Argenta')
        df_arge0003.insert(1, 'Product_ID', 'ARGE0003')
        df_arge0003.insert(1, 'Category', 'Renovation Loan')

        df_arge0003_rl = df_arge0003[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################ARGE0004###########################################################

        website_url = 'https://action.argenta.be/pret-personnel/?utm_source=site&utm_medium=pa_persoonlijkelening&utm_content=2018fr&utm_campaign=persoonlijke-lening#simulator'
        html_code = requests.get(website_url)
        soup = bs4.BeautifulSoup(html_code.content, 'lxml')
        content = soup.find_all('h2', {'class': "gsection_title"})
        content2 = str(str(content).split())

        for item in content2:
            min_argenta_1 = re.findall(r"'tussen', '(.*?)',", content2)
            min_argenta_2_5 = re.findall(r"van',.'(.*?)'", content2)
            min_argenta_6 = re.findall(r"dan',.'(.*?)'", content2)
            max_argenta_1 = re.findall(r"'en',.'(.*?)<.h2.", content2)
            max_argenta_2_5 = re.findall(r"'-',.'(.*?)'", content2)
            max_argenta_6 = ['~']
            min_argenta = min_argenta_1 + min_argenta_2_5 + min_argenta_6  # This is to append a list
            max_argenta = max_argenta_1 + max_argenta_2_5 + max_argenta_6

        content_term_1 = soup.find_all('select', {'name': "input_122"})
        content_term_2 = soup.find_all('select', {'name': "input_121"})
        content_term_3 = soup.find_all('select', {'name': "input_120"})
        content_term_4 = soup.find_all('select', {'name': "input_119"})
        content_term_5 = soup.find_all('select', {'name': "input_118"})
        content_term_6 = soup.find_all('select', {'name': "input_117"})
        content_term_7 = soup.find_all('select', {'name': "input_113"})
        content_term1_1 = str(str(content_term_1).split())
        content_term2_1 = str(str(content_term_2).split())
        content_term3_1 = str(str(content_term_3).split())
        content_term4_1 = str(str(content_term_4).split())
        content_term5_1 = str(str(content_term_5).split())
        content_term6_1 = str(str(content_term_6).split())
        content_term7_1 = str(str(content_term_7).split())
        for item in content_term1_1:
            min_term_argenta_1 = re.findall(r'value="(.*?)"', content_term1_1)[0]
            max_term_argenta_1 = re.findall(r'value="(.*?)"', content_term1_1)[-1]
        for item in content_term2_1:
            min_term_argenta_2 = re.findall(r'value="(.*?)"', content_term2_1)[0]
            max_term_argenta_2 = re.findall(r'value="(.*?)"', content_term2_1)[-1]
        for item in content_term3_1:
            min_term_argenta_3 = re.findall(r'value="(.*?)"', content_term3_1)[0]
            max_term_argenta_3 = re.findall(r'value="(.*?)"', content_term3_1)[-1]
        for item in content_term4_1:
            min_term_argenta_4 = re.findall(r'value="(.*?)"', content_term4_1)[0]
            max_term_argenta_4 = re.findall(r'value="(.*?)"', content_term4_1)[-1]
        for item in content_term5_1:
            min_term_argenta_5 = re.findall(r'value="(.*?)"', content_term5_1)[0]
            max_term_argenta_5 = re.findall(r'value="(.*?)"', content_term5_1)[-1]
        for item in content_term6_1:
            min_term_argenta_6 = re.findall(r'value="(.*?)"', content_term6_1)[0]
            max_term_argenta_6 = re.findall(r'value="(.*?)"', content_term6_1)[-1]
        for item in content_term7_1:
            min_term_argenta_7 = re.findall(r'value="(.*?)"', content_term7_1)[0]
            max_term_argenta_7 = re.findall(r'value="(.*?)"', content_term7_1)[-1]
        minterm_argenta = [min_term_argenta_1, min_term_argenta_2, min_term_argenta_3, min_term_argenta_4, min_term_argenta_5, min_term_argenta_6, min_term_argenta_7]  # append string into a list
        maxterm_argenta = [max_term_argenta_1, max_term_argenta_2, max_term_argenta_3, max_term_argenta_4, max_term_argenta_5, max_term_argenta_6, max_term_argenta_7]

        TAEG_1 = soup.find_all('li', {'id': "field_19_123"})
        TAEG_2 = soup.find_all('li', {'id': "field_19_126"})
        TAEG_3 = soup.find_all('li', {'id': "field_19_128"})
        TAEG_4 = soup.find_all('li', {'id': "field_19_130"})
        TAEG_5 = soup.find_all('li', {'id': "field_19_132"})
        TAEG_6 = soup.find_all('li', {'id': "field_19_134"})
        TAEG_7 = soup.find_all('li', {'id': "field_19_136"})
        TAEG_1 = str(str(TAEG_1).split())
        TAEG_2 = str(str(TAEG_2).split())
        TAEG_3 = str(str(TAEG_3).split())
        TAEG_4 = str(str(TAEG_4).split())
        TAEG_5 = str(str(TAEG_5).split())
        TAEG_6 = str(str(TAEG_6).split())
        TAEG_7 = str(str(TAEG_7).split())
        for item in TAEG_1:
            TAEG_argenta_1 = re.findall(r"div>., .(.*?)', .%", TAEG_1)
        for item in TAEG_2:
            TAEG_argenta_2 = re.findall(r"div>., .(.*?)', .%", TAEG_2)
        for item in TAEG_3:
            TAEG_argenta_3 = re.findall(r"div>., .(.*?)', .%", TAEG_3)
        for item in TAEG_4:
            TAEG_argenta_4 = re.findall(r"div>., .(.*?)', .%", TAEG_4)
        for item in TAEG_5:
            TAEG_argenta_5 = re.findall(r"div>., .(.*?)', .%", TAEG_5)
        for item in TAEG_6:
            TAEG_argenta_6 = re.findall(r"div>., .(.*?)', .%", TAEG_6)
        for item in TAEG_7:
            TAEG_argenta_7 = re.findall(r"div>., .(.*?)', .%", TAEG_7)
        TAEG_argenta = TAEG_argenta_1 + TAEG_argenta_2 + TAEG_argenta_3 + TAEG_argenta_4 + TAEG_argenta_5 + TAEG_argenta_6 + TAEG_argenta_7

        argenta_array = np.column_stack((min_argenta, max_argenta, minterm_argenta, maxterm_argenta, TAEG_argenta))
        argenta_tup = tuple(map(tuple, argenta_array))

        ##########convert everything into a panda df##########

        Min_arge0004 = pd.DataFrame(min_argenta, columns=['Min'])
        Max_arge0004 = pd.DataFrame(max_argenta, columns=['Max'])
        amount_arge0004 = Min_arge0004.join(Max_arge0004)

        MinTerm_arge0004 = pd.DataFrame(minterm_argenta, columns=['Min Term'])
        MaxTerm_arge0004 = pd.DataFrame(maxterm_argenta, columns=['Max Term'])
        duration_arge0004 = MinTerm_arge0004.join(MaxTerm_arge0004)

        Taux_arge0004 = pd.DataFrame(TAEG_argenta, columns=['Taux'])

        df_arge0004 = amount_arge0004.join(duration_arge0004)
        df_arge0004 = df_arge0004.join(Taux_arge0004)

        df_arge0004.insert(0, 'Provider', 'Argenta')
        df_arge0004.insert(1, 'Product_ID', 'ARGE0004')
        df_arge0004.insert(1, 'Category', 'Personal Loan')

        df_arge0004_pl = df_arge0004[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################ARGE0005###########################################################

        ### the difference between ARGE0002 and ARGE0001 is only in TAEG, but below codes are required to create independencies

        arge0005_url = 'https://action.argenta.be/pret-auto/?utm_source=site&utm_medium=pa_autolening&utm_content=2018fr&utm_campaign=autolening#simulator'
        arge0005_htmlcode = requests.get(arge0005_url)
        arge0005_soup = bs4.BeautifulSoup(arge0005_htmlcode.content, 'lxml')
        arge0005_content = arge0005_soup.find_all('h2', {'class': "gsection_title"})
        arge0005_content2 = str(str(arge0005_content).split())

        ### look for minimum and maximum amount
        for item in arge0005_content2:
            min_arge0005_1 = re.findall(r"'tussen', '(.*?)',", arge0005_content2)
            min_arge0005_2_5 = re.findall(r"van',.'(.*?)'", arge0005_content2)
            min_arge0005_6 = re.findall(r"dan',.'(.*?)'", arge0005_content2)[0]
            min_arge0005_6 = [min_arge0005_6]  # convert from str to a list

            max_arge0005_1 = re.findall(r"'en',.'(.*?)<.h2.", arge0005_content2)
            max_arge0005_2_5 = re.findall(r"'-',.'(.*?)', 'euro<.h2>", arge0005_content2)
            max_arge0005_6 = ['50.000']

            min_arge0005 = min_arge0005_1 + min_arge0005_2_5 + min_arge0005_6  # This is to append a list
            max_arge0005 = max_arge0005_1 + max_arge0005_2_5 + max_arge0005_6

        ### look for minimum and maximum months, loop is not applied since we would like to capture each term changes

        term_arge0005_1 = arge0005_soup.find_all('select', {'name': "input_122"})
        term_arge0005_2 = arge0005_soup.find_all('select', {'name': "input_121"})
        term_arge0005_3 = arge0005_soup.find_all('select', {'name': "input_120"})
        term_arge0005_4 = arge0005_soup.find_all('select', {'name': "input_119"})
        term_arge0005_5 = arge0005_soup.find_all('select', {'name': "input_118"})
        term_arge0005_6 = arge0005_soup.find_all('select', {'name': "input_117"})
        term_arge0005_7 = arge0005_soup.find_all('select', {'name': "input_113"})

        term_arge0005_1 = str(str(term_arge0005_1).split())
        term_arge0005_2 = str(str(term_arge0005_2).split())
        term_arge0005_3 = str(str(term_arge0005_3).split())
        term_arge0005_4 = str(str(term_arge0005_4).split())
        term_arge0005_5 = str(str(term_arge0005_5).split())
        term_arge0005_6 = str(str(term_arge0005_6).split())
        term_arge0005_7 = str(str(term_arge0005_7).split())

        for item in term_arge0005_1:
            minterm_arge0005_1 = re.findall(r'value="(.*?)"', term_arge0005_1)[0]
            maxterm_arge0005_1 = re.findall(r'value="(.*?)"', term_arge0005_1)[-1]
        for item in term_arge0005_2:
            minterm_arge0005_2 = re.findall(r'value="(.*?)"', term_arge0005_2)[0]
            maxterm_arge0005_2 = re.findall(r'value="(.*?)"', term_arge0005_2)[-1]
        for item in term_arge0005_3:
            minterm_arge0005_3 = re.findall(r'value="(.*?)"', term_arge0005_3)[0]
            maxterm_arge0005_3 = re.findall(r'value="(.*?)"', term_arge0005_3)[-1]
        for item in term_arge0005_4:
            minterm_arge0005_4 = re.findall(r'value="(.*?)"', term_arge0005_4)[0]
            maxterm_arge0005_4 = re.findall(r'value="(.*?)"', term_arge0005_4)[-1]
        for item in term_arge0005_5:
            minterm_arge0005_5 = re.findall(r'value="(.*?)"', term_arge0005_5)[0]
            maxterm_arge0005_5 = re.findall(r'value="(.*?)"', term_arge0005_5)[-1]
        for item in term_arge0005_6:
            minterm_arge0005_6 = re.findall(r'value="(.*?)"', term_arge0005_6)[0]
            maxterm_arge0005_6 = re.findall(r'value="(.*?)"', term_arge0005_6)[-1]
        for item in term_arge0005_7:
            minterm_arge0005_7 = re.findall(r'value="(.*?)"', term_arge0005_7)[0]
            maxterm_arge0005_7 = re.findall(r'value="(.*?)"', term_arge0005_7)[-1]

        minterm_arge0005 = [minterm_arge0005_1, minterm_arge0005_2, minterm_arge0005_3, minterm_arge0005_4, minterm_arge0005_5, minterm_arge0005_6, minterm_arge0005_7]  # append string into a list
        maxterm_arge0005 = [maxterm_arge0005_1, maxterm_arge0005_2, maxterm_arge0005_3, maxterm_arge0005_4, maxterm_arge0005_5, maxterm_arge0005_6, maxterm_arge0005_7]

        # ### look for TAEG

        arge0005_content_taeg = arge0005_soup.find_all('input', {'name': "input_9"})
        TAEG_arge0005 = str(str(arge0005_content_taeg).split())  # change the type to str so we can parse using RegEx

        for item in TAEG_arge0005:
            TAEG_argenta_5 = re.findall(r'radio"., .value="(.*)".>,., .<input., .id="choice_12_9_1".', TAEG_arge0005)
        TAEG_arge0005 = TAEG_argenta_5 * 7  # times the number of total elements

        ### transform matrix
        arge0005_array = np.column_stack((min_arge0005, max_arge0005, minterm_arge0005, maxterm_arge0005, TAEG_arge0005))
        arge0005_tup = tuple(map(tuple, arge0005_array))

        ##########convert everything into a panda df##########

        Min_arge0005 = pd.DataFrame(min_arge0005, columns=['Min'])
        Max_arge0005 = pd.DataFrame(max_arge0005, columns=['Max'])
        amount_arge0005 = Min_arge0005.join(Max_arge0005)

        MinTerm_arge0005 = pd.DataFrame(minterm_arge0005, columns=['Min Term'])
        MaxTerm_arge0005 = pd.DataFrame(maxterm_arge0005, columns=['Max Term'])
        duration_arge0005 = MinTerm_arge0005.join(MaxTerm_arge0005)

        Taux_arge0005 = pd.DataFrame(TAEG_arge0005, columns=['Taux'])

        df_arge0005 = amount_arge0005.join(duration_arge0005)
        df_arge0005 = df_arge0005.join(Taux_arge0005)

        df_arge0005.insert(0, 'Provider', 'Argenta')
        df_arge0005.insert(1, 'Product_ID', 'ARGE0005')
        df_arge0005.insert(1, 'Category', 'Vehicle Loan')

        df_arge0005_vl = df_arge0005[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

    ###############################################################################################################
    ############################################ARGE0006###########################################################

        arge0006_url = 'https://action.argenta.be/pret-renovation/?utm_source=site&utm_medium=pa_renovatielening&utm_content=2018fr&utm_campaign=renovatielening#simulator'
        arge0006_htmlcode = requests.get(arge0006_url)
        arge0006_soup = bs4.BeautifulSoup(arge0006_htmlcode.content, 'lxml')
        arge0006_content = arge0006_soup.find_all('h2', {'class': "gsection_title"})
        arge0006_content2 = str(str(arge0006_content).split())

        ### look for minimum and maximum amount
        for item in arge0006_content2:
            min_arge0006_1 = re.findall(r"'tussen', '(.*?)',", arge0006_content2)
            min_arge0006_2_5 = re.findall(r"van',.'(.*?)'", arge0006_content2)
            min_arge0006_6 = re.findall(r"dan',.'(.*?)'", arge0006_content2)[0]
            min_arge0006_6 = [min_arge0006_6]  # convert from str to a list

            max_arge0006_1 = re.findall(r"'en',.'(.*?)<.h2.", arge0006_content2)
            max_arge0006_2_5 = re.findall(r"'-',.'(.*?)', 'euro<.h2>", arge0006_content2)
            max_arge0006_6 = ['50.000']

            min_arge0006 = min_arge0006_1 + min_arge0006_2_5 + min_arge0006_6  # This is to append a list
            max_arge0006 = max_arge0006_1 + max_arge0006_2_5 + max_arge0006_6

        ### look for minimum and maximum months, loop is not applied since we would like to capture each term changes

        term_arge0006_1 = arge0006_soup.find_all('select', {'name': "input_122"})
        term_arge0006_2 = arge0006_soup.find_all('select', {'name': "input_121"})
        term_arge0006_3 = arge0006_soup.find_all('select', {'name': "input_120"})
        term_arge0006_4 = arge0006_soup.find_all('select', {'name': "input_119"})
        term_arge0006_5 = arge0006_soup.find_all('select', {'name': "input_118"})
        term_arge0006_6 = arge0006_soup.find_all('select', {'name': "input_117"})
        term_arge0006_7 = arge0006_soup.find_all('select', {'name': "input_113"})

        term_arge0006_1 = str(str(term_arge0006_1).split())
        term_arge0006_2 = str(str(term_arge0006_2).split())
        term_arge0006_3 = str(str(term_arge0006_3).split())
        term_arge0006_4 = str(str(term_arge0006_4).split())
        term_arge0006_5 = str(str(term_arge0006_5).split())
        term_arge0006_6 = str(str(term_arge0006_6).split())
        term_arge0006_7 = str(str(term_arge0006_7).split())

        for item in term_arge0006_1:
            minterm_arge0006_1 = re.findall(r'value="(.*?)"', term_arge0006_1)[0]
            maxterm_arge0006_1 = re.findall(r'value="(.*?)"', term_arge0006_1)[-1]
        for item in term_arge0006_2:
            minterm_arge0006_2 = re.findall(r'value="(.*?)"', term_arge0006_2)[0]
            maxterm_arge0006_2 = re.findall(r'value="(.*?)"', term_arge0006_2)[-1]
        for item in term_arge0006_3:
            minterm_arge0006_3 = re.findall(r'value="(.*?)"', term_arge0006_3)[0]
            maxterm_arge0006_3 = re.findall(r'value="(.*?)"', term_arge0006_3)[-1]
        for item in term_arge0006_4:
            minterm_arge0006_4 = re.findall(r'value="(.*?)"', term_arge0006_4)[0]
            maxterm_arge0006_4 = re.findall(r'value="(.*?)"', term_arge0006_4)[-1]
        for item in term_arge0006_5:
            minterm_arge0006_5 = re.findall(r'value="(.*?)"', term_arge0006_5)[0]
            maxterm_arge0006_5 = re.findall(r'value="(.*?)"', term_arge0006_5)[-1]
        for item in term_arge0006_6:
            minterm_arge0006_6 = re.findall(r'value="(.*?)"', term_arge0006_6)[0]
            maxterm_arge0006_6 = re.findall(r'value="(.*?)"', term_arge0006_6)[-1]
        for item in term_arge0006_7:
            minterm_arge0006_7 = re.findall(r'value="(.*?)"', term_arge0006_7)[0]
            maxterm_arge0006_7 = re.findall(r'value="(.*?)"', term_arge0006_7)[-1]

        minterm_arge0006 = [minterm_arge0006_1, minterm_arge0006_2, minterm_arge0006_3, minterm_arge0006_4, minterm_arge0006_5, minterm_arge0006_6, minterm_arge0006_7]  # append string into a list
        maxterm_arge0006 = [maxterm_arge0006_1, maxterm_arge0006_2, maxterm_arge0006_3, maxterm_arge0006_4, maxterm_arge0006_5, maxterm_arge0006_6, maxterm_arge0006_7]

        # ### look for TAEG

        arge0006_content_taeg = arge0006_soup.find_all('input', {'name': "input_9"})
        TAEG_arge0006 = str(str(arge0006_content_taeg).split())  # change the type to str so we can parse using RegEx

        for item in TAEG_arge0006:
            TAEG_argenta_6 = re.findall(r'choice_11_9_1.*value="(.*?)".>...', TAEG_arge0006)
        TAEG_arge0006 = TAEG_argenta_6 * 7  # times the number of total elements

        ### transform matrix
        arge0006_array = np.column_stack((min_arge0006, max_arge0006, minterm_arge0006, maxterm_arge0006, TAEG_arge0006))
        arge0006_tup = tuple(map(tuple, arge0006_array))

        ##########convert everything into a panda df##########

        Min_arge0006 = pd.DataFrame(min_arge0006, columns=['Min'])
        Max_arge0006 = pd.DataFrame(max_arge0006, columns=['Max'])
        amount_arge0006 = Min_arge0006.join(Max_arge0006)

        MinTerm_arge0006 = pd.DataFrame(minterm_arge0006, columns=['Min Term'])
        MaxTerm_arge0006 = pd.DataFrame(maxterm_arge0006, columns=['Max Term'])
        duration_arge0006 = MinTerm_arge0006.join(MaxTerm_arge0006)

        Taux_arge0006 = pd.DataFrame(TAEG_arge0006, columns=['Taux'])

        df_arge0006 = amount_arge0006.join(duration_arge0006)
        df_arge0006 = df_arge0006.join(Taux_arge0006)

        df_arge0006.insert(0, 'Provider', 'Argenta')
        df_arge0006.insert(1, 'Product_ID', 'ARGE0006')
        df_arge0006.insert(1, 'Category', 'Renovation Loan')

        df_arge0006_rl = df_arge0006[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        arge_loans_c = pd.concat([pd.concat([df_arge0001_vl], axis=1),
                                  pd.concat([df_arge0002_vl], axis=1),
                                  pd.concat([df_arge0003_rl], axis=1),
                                  pd.concat([df_arge0004_pl], axis=1),
                                  pd.concat([df_arge0005_vl], axis=1),
                                  pd.concat([df_arge0006_rl], axis=1)])

        print(tabulate(arge_loans_c, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def argenta_save_loans():
    argenta_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    arge_loans_c.to_csv(os.path.join(path, file_name), index=False)


# #                    _  ___ _              # #
# #    /\              (_)/ __|_)            # #
# #   /  \  _   _ _   _ _| |__ _ ____   ____ # #
# #  / /\ \| | | ( \ / ) |  __) |  _ \ / _  |# #
# # | |__| | |_| |) X (| | |  | | | | ( ( | |# #
# # |______|\____(_/ \_)_|_|  |_|_| |_|\_||_|# #

def auxifina_loans():
    try:
        global auxi_loans_c

        ###############################################################################################################
        ############################################AUXI0001###########################################################
        with urlopen("https://auxifina.be/sites/all/themes/auxifina/dist/scripts/ngApp/data/simulator/matrix-simulator.json?1552768926329") as response:
            source_auxi0001 = response.read()

        data_auxi0001 = json.loads(source_auxi0001)

        # to return list of lists in a loop
        results = []
        for item in data_auxi0001:
            bank_auxi0001 = 'Auxifina'
            productId_aux0001 = 'AUXI0001'
            category_aux0001 = 'Personal Loan'
            credittype = item['CreditType']
            min_auxi0001 = item['MinAmount']
            max_auxi0001 = item['MaxAmount']
            minterm_auxi0001 = item['MinDuration']
            maxterm_auxi0001 = item['MaxDuration']
            TAEG_auxi0001 = item['DisplayJKP']
            auxi0001 = [credittype, bank_auxi0001, productId_aux0001, category_aux0001, min_auxi0001, max_auxi0001, minterm_auxi0001, maxterm_auxi0001, TAEG_auxi0001]  # put in list to convert to pd
            results.append(auxi0001)

        auxi0001 = pd.DataFrame(results, columns=None)
        auxi0001.columns = ['_type_', 'Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        df_auxi0001_pl = auxi0001.drop(auxi0001.index[12:62])  # to select the one with CreditType '1'
        df_auxi0001_pl.drop(auxi0001.columns[0], axis=1, inplace=True)

        ###############################################################################################################
        ############################################AUXI0002###########################################################

        with urlopen("https://auxifina.be/sites/all/themes/auxifina/dist/scripts/ngApp/data/simulator/matrix-simulator.json?1552768926329") as response:
            source_auxi0002 = response.read()

        data_auxi0002 = json.loads(source_auxi0002)

            # to return list of lists in a loop
        results = []
        for item in data_auxi0002:
            bank_auxi0002 = 'Auxifina'
            productId_aux0002 = 'AUXI0002'
            category_aux0002 = 'Vehicle Loan'
            credittype = item['CreditType']
            min_auxi0002 = item['MinAmount']
            max_auxi0002 = item['MaxAmount']
            minterm_auxi0002 = item['MinDuration']
            maxterm_auxi0002 = item['MaxDuration']
            TAEG_auxi0002 = item['DisplayJKP']
            auxi0002 = [credittype, bank_auxi0002, productId_aux0002, category_aux0002, min_auxi0002, max_auxi0002, minterm_auxi0002, maxterm_auxi0002, TAEG_auxi0002]  # put in list to convert to pd
            results.append(auxi0002)

        auxi0002 = pd.DataFrame(results, columns=None)
        auxi0002.columns = ['_type_', 'Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        df_auxi0002_vl = auxi0002.drop(auxi0002.index[0:20]).drop(auxi0002.index[29:62])  # to select the one with CreditType '3'
        df_auxi0002_vl.drop(auxi0002.columns[0], axis=1, inplace=True)

        ###############################################################################################################
        ############################################AUXI0004###########################################################

        with urlopen("https://auxifina.be/sites/all/themes/auxifina/dist/scripts/ngApp/data/simulator/matrix-simulator.json?1552768926329") as response:
            source_auxi0004 = response.read()

        data_auxi0004 = json.loads(source_auxi0004)
        # to return list of lists in a loop
        results = []
        for item in data_auxi0004:
            bank_auxi0004 = 'Auxifina'
            productId_aux0004 = 'AUXI0004'
            category_aux0004 = 'Renovation Loan'
            credittype = item['CreditType']
            min_auxi0004 = item['MinAmount']
            max_auxi0004 = item['MaxAmount']
            minterm_auxi0004 = item['MinDuration']
            maxterm_auxi0004 = item['MaxDuration']
            TAEG_auxi0004 = item['DisplayJKP']
            auxi0004 = [credittype, bank_auxi0004, productId_aux0004, category_aux0004, min_auxi0004, max_auxi0004, minterm_auxi0004, maxterm_auxi0004, TAEG_auxi0004]  # put in list to convert to pd
            results.append(auxi0004)

        auxi0004 = pd.DataFrame(results, columns=None)
        auxi0004.columns = ['_type_', 'Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        df_auxi0004_rl = auxi0004.drop(auxi0004.index[0:12]).drop(auxi0004.index[20:62])  # to select the one with CreditType '2'
        df_auxi0004_rl.drop(auxi0004.columns[0], axis=1, inplace=True)

        auxi_loans_c = pd.concat([pd.concat([df_auxi0001_pl], axis=1),
                                  pd.concat([df_auxi0002_vl], axis=1),
                                  pd.concat([df_auxi0004_rl], axis=1)])
        print(tabulate(auxi_loans_c, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def auxifina_save_loans():
    auxifina_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    auxi_loans_c.to_csv(os.path.join(path, file_name), index=False)



# #   /\  \ \  / /  /\     (____  \            | |    # #
# #  /  \  \ \/ /  /  \     ____)  ) ____ ____ | |  _ # #
# # / /\ \  )  (  / /\ \   |  __  ( / _  |  _ \| | / )# #
# #| |__| |/ /\ \| |__| |  | |__)  | ( | | | | | |< ( # #
# #|______/_/  \_\______|  |______/ \_||_|_| |_|_| \_)# #

def axabank_loans():
    try:
        ###############################################################################################################
        ############################################AXAB0005###########################################################
        global df_axab0005_loans
        df_axab0005 = read_pdf('https://www.axabank.be/-/media/axa/juridic-documents/rates-charges/privatecredits.pdf?dmc=1&la=fr&ts=20180430t1242510112', pages=1, pandas_options={'header': None})
        dfx_axab0005 = df_axab0005.drop(df_axab0005.index[[10, 11, 12]])

        bank_axa = ['AXA']
        product_Id_axab0005 = ['AXAB0005']
        category_axab0005 = ['Personal Loan']
        min_max_axa = list(dfx_axab0005.loc[8:9, 1])
        min_max_term_axa = list(dfx_axab0005.loc[8:9, 2])
        TAEG_axa = [''.join(dfx_axab0005.iloc[8, 3]).replace(',', '.')]  # Join the items within a list and replace ',' with '.'
        AXA_PL = bank_axa + product_Id_axab0005 + category_axab0005 + min_max_axa + min_max_term_axa + TAEG_axa  # Extend the items into a list
        AXA_PL = [s.strip(' EUR%') for s in AXA_PL]  # Remove the character inside the list

        df_axab0005_loans = pd.DataFrame([AXA_PL])
        df_axab0005_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        print(tabulate(df_axab0005_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def axabank_save_loans():
    axabank_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_axab0005_loans.to_csv(os.path.join(path, file_name), index=False)






# #  _           _  ___ _             # #
# # | |         | |/ __|_)            # #
# # | | _   ____| | |__ _ _   _  ___  # #
# # | || \ / _  ) |  __) | | | |/___) # #
# # | |_) | (/ /| | |  | | |_| |___ | # #
# # |____/ \____)_|_|  |_|\____(___/  # #

def belfius_loans():
    try:
        global belfius_loans_c
    ###############################################################################################################
    ############################################BELF0001###########################################################

        url_belf0001 = 'https://www.belfius.be/retail/fr/produits/emprunter/vehicule/pret-voiture/index.aspx'
        html_belf0001 = requests.get(url_belf0001)
        soup_belf0001 = bs4.BeautifulSoup(html_belf0001.content, 'lxml')

        content_belf0001 = soup_belf0001.find_all('table', {'class': "embeddedTable"})
        content_belf0001_2 = soup_belf0001.find_all('section', {'class': "footnote"})
        content_belf0001 = str(str(content_belf0001).split())  # list -> str to ease the RegEx
        content_belf0001_2 = str(str(content_belf0001_2).split())  # list -> str

        for item in content_belf0001:
            min_belf0001_1 = re.findall(r"EUR.\">',.'(.*?)'<.td>'", content_belf0001)[0:1]  # 2500 #dont forget to always add : to make it str
            min_belf0001_1 = str(min_belf0001_1)
            min_belf0001_1 = re.sub('[^0-9a-zA-Z]+', '', min_belf0001_1)
            max_belf0001_1 = min_belf0001_1

            min_belf0001_2 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[0]  # 2500,01
            min_belf0001_2 = str(min_belf0001_2)
            min_belf0001_2 = re.sub("[ ']+", '', min_belf0001_2)
            min_belf0001_2 = re.sub("[,]+", '.', min_belf0001_2, 1)  # replace the first ',' occurance with '.'
            max_belf0001_2 = re.findall(r"'-', '(.*?), '<.td", content_belf0001)[0]
            max_belf0001_2 = str(max_belf0001_2)
            max_belf0001_2 = re.sub("[ ']+", '', max_belf0001_2)
            max_belf0001_2 = re.sub("[,]+", '.', max_belf0001_2, 1)  # replace the first ',' occurance with '.'

            min_belf0001_3 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[1]  # 3700,01
            min_belf0001_3 = str(min_belf0001_3)
            min_belf0001_3 = re.sub("[ ']+", '', min_belf0001_3)
            min_belf0001_3 = re.sub("[,]+", '.', min_belf0001_3, 1)  # replace the first ',' occurance with '.'
            max_belf0001_3 = re.findall(r"'-', '(.*?), '<.td", content_belf0001)[1]  # 5600
            max_belf0001_3 = str(max_belf0001_3)
            max_belf0001_3 = re.sub("[ ']+", '', max_belf0001_3)
            max_belf0001_3 = re.sub("[,]+", '.', max_belf0001_3, 1)  # replace the first ',' occurance with '.'

            min_belf0001_4 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[2]  # 5600,01
            min_belf0001_4 = str(min_belf0001_4)
            min_belf0001_4 = re.sub("[ ']+", '', min_belf0001_4)
            min_belf0001_4 = re.sub("[,]+", '.', min_belf0001_4, 1)  # replace the first ',' occurance with '.'
            max_belf0001_4 = re.findall(r"'-', '(.*?), '<.td", content_belf0001)[2]  # 7500
            max_belf0001_4 = str(max_belf0001_4)
            max_belf0001_4 = re.sub("[ ']+", '', max_belf0001_4)
            max_belf0001_4 = re.sub("[,]+", '.', max_belf0001_4, 1)  # replace the first ',' occurance with '.'

            min_belf0001_5 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[3]  # 7500,01
            min_belf0001_5 = str(min_belf0001_5)
            min_belf0001_5 = re.sub("[ ']+", '', min_belf0001_5)
            min_belf0001_5 = re.sub("[,]+", '.', min_belf0001_5, 1)  # replace the first ',' occurance with '.'
            max_belf0001_5 = re.findall(r"'-', '(.*?), '<.td", content_belf0001)[3]  # 10000
            max_belf0001_5 = str(max_belf0001_5)
            max_belf0001_5 = re.sub("[ ']+", '', max_belf0001_5)
            max_belf0001_5 = re.sub("[,]+", '.', max_belf0001_5, 1)  # replace the first ',' occurance with '.'

            min_belf0001_6 = re.findall(r"'48'.*EUR..>', '(.*?), '–', 'illimit", content_belf0001)[0]  # 10000,01
            min_belf0001_6 = str(min_belf0001_6)
            min_belf0001_6 = re.sub('[ "]+', '', min_belf0001_6)
            min_belf0001_6 = re.sub("[ ']+", '', min_belf0001_6)
            min_belf0001_6 = re.sub("[,]+", '.', min_belf0001_6, 1)  # replace the first ',' occurance with '.'
            max_belf0001_6 = re.findall(r"'–', .(.*?)'", content_belf0001)[0]  # illimité

            min_belf0001 = [min_belf0001_1, min_belf0001_2, min_belf0001_3, min_belf0001_4, min_belf0001_5, min_belf0001_6]
            max_belf0001 = [max_belf0001_1, max_belf0001_2, max_belf0001_3, max_belf0001_4, max_belf0001_5, max_belf0001_6]

            minterm_belf0001 = [12] * 6
            maxterm_belf0001 = re.findall(r"'mois.>', '(.*?)',", content_belf0001)

        for item in content_belf0001_2:
            TAEG_belf0001 = re.findall(r"fixe<.span>', ':', '(.*?)%'", content_belf0001_2) * 6

        belf0001 = (min_belf0001, max_belf0001, minterm_belf0001, maxterm_belf0001, TAEG_belf0001)

        belf0001_array = np.column_stack((min_belf0001, max_belf0001, minterm_belf0001, maxterm_belf0001, TAEG_belf0001))
        belf0001_tup = tuple(map(tuple, belf0001_array))

        ##########convert everything into a panda df##########

        Min_belf0001 = pd.DataFrame(min_belf0001, columns=['Min'])
        Max_belf0001 = pd.DataFrame(max_belf0001, columns=['Max'])
        amount_belf0001 = Min_belf0001.join(Max_belf0001)

        MinTerm_belf0001 = pd.DataFrame(minterm_belf0001, columns=['Min Term'])
        MaxTerm_belf0001 = pd.DataFrame(maxterm_belf0001, columns=['Max Term'])
        duration_belf0001 = MinTerm_belf0001.join(MaxTerm_belf0001)

        Taux_belf0001 = pd.DataFrame(TAEG_belf0001, columns=['Taux'])

        df_belf0001 = amount_belf0001.join(duration_belf0001)
        df_belf0001 = df_belf0001.join(Taux_belf0001)

        df_belf0001.insert(0, 'Provider', 'Belfius')
        df_belf0001.insert(1, 'Product_ID', 'BELF0001')
        df_belf0001.insert(1, 'Category', 'Vehicle Loan')

        df_belf0001_vl = df_belf0001[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BELF0002###########################################################

        url_belf0002 = 'https://www.belfius.be/retail/fr/produits/emprunter/vehicule/pret-voiture-occasion/index.aspx'
        html_belf0002 = requests.get(url_belf0002)
        soup_belf0002 = bs4.BeautifulSoup(html_belf0002.content, 'lxml')

        content_belf0002 = soup_belf0002.find_all('table', {'class': "embeddedTable"})
        content_belf0002_2 = soup_belf0002.find_all('section', {'class': "footnote"})
        content_belf0002 = str(str(content_belf0002).split())  # list -> str to ease the RegEx
        content_belf0002_2 = str(str(content_belf0002_2).split())  # list -> str

        for item in content_belf0002:
            min_belf0002_1 = re.findall(r"EUR.\">',.'(.*?)'<.td>'", content_belf0002)[0:1]  # 2500 #dont forget to always add : to make it str
            min_belf0002_1 = str(min_belf0002_1)
            min_belf0002_1 = re.sub('[^0-9a-zA-Z]+', '', min_belf0002_1)
            max_belf0002_1 = min_belf0002_1

            min_belf0002_2 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[0]  # 2500,01
            min_belf0002_2 = str(min_belf0002_2)
            min_belf0002_2 = re.sub("[ ']+", '', min_belf0002_2)
            min_belf0002_2 = re.sub("[,]+", '.', min_belf0002_2, 1)  # replace the first ',' occurance with '.'
            max_belf0002_2 = re.findall(r"'-', '(.*?), '<.td", content_belf0002)[0]
            max_belf0002_2 = str(max_belf0002_2)
            max_belf0002_2 = re.sub("[ ']+", '', max_belf0002_2)
            max_belf0002_2 = re.sub("[,]+", '.', max_belf0002_2, 1)  # replace the first ',' occurance with '.'

            min_belf0002_3 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[1]  # 3700,01
            min_belf0002_3 = str(min_belf0002_3)
            min_belf0002_3 = re.sub("[ ']+", '', min_belf0002_3)
            min_belf0002_3 = re.sub("[,]+", '.', min_belf0002_3, 1)  # replace the first ',' occurance with '.'
            max_belf0002_3 = re.findall(r"'-', '(.*?), '<.td", content_belf0002)[1]  # 5600
            max_belf0002_3 = str(max_belf0002_3)
            max_belf0002_3 = re.sub("[ ']+", '', max_belf0002_3)
            max_belf0002_3 = re.sub("[,]+", '.', max_belf0002_3, 1)  # replace the first ',' occurance with '.'

            min_belf0002_4 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[2]  # 5600,01
            min_belf0002_4 = str(min_belf0002_4)
            min_belf0002_4 = re.sub("[ ']+", '', min_belf0002_4)
            min_belf0002_4 = re.sub("[,]+", '.', min_belf0002_4, 1)  # replace the first ',' occurance with '.'
            max_belf0002_4 = re.findall(r"'-', '(.*?), '<.td", content_belf0002)[2]  # 7500
            max_belf0002_4 = str(max_belf0002_4)
            max_belf0002_4 = re.sub("[ ']+", '', max_belf0002_4)
            max_belf0002_4 = re.sub("[,]+", '.', max_belf0002_4, 1)  # replace the first ',' occurance with '.'

            min_belf0002_5 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[3]  # 7500,01
            min_belf0002_5 = str(min_belf0002_5)
            min_belf0002_5 = re.sub("[ ']+", '', min_belf0002_5)
            min_belf0002_5 = re.sub("[,]+", '.', min_belf0002_5, 1)  # replace the first ',' occurance with '.'
            max_belf0002_5 = re.findall(r"'-', '(.*?), '<.td", content_belf0002)[3]  # 10000
            max_belf0002_5 = str(max_belf0002_5)
            max_belf0002_5 = re.sub("[ ']+", '', max_belf0002_5)
            max_belf0002_5 = re.sub("[,]+", '.', max_belf0002_5, 1)  # replace the first ',' occurance with '.'

            min_belf0002_6 = re.findall(r"'48'.*EUR..>', '(.*?), '–', 'illimit", content_belf0002)[0]  # 10000,01
            min_belf0002_6 = str(min_belf0002_6)
            min_belf0002_6 = re.sub('[ "]+', '', min_belf0002_6)
            min_belf0002_6 = re.sub("[ ']+", '', min_belf0002_6)
            min_belf0002_6 = re.sub("[,]+", '.', min_belf0002_6, 1)  # replace the first ',' occurance with '.'
            max_belf0002_6 = re.findall(r"'–', .(.*?)'", content_belf0002)[0]  # illimité

            min_belf0002 = [min_belf0002_1, min_belf0002_2, min_belf0002_3, min_belf0002_4, min_belf0002_5, min_belf0002_6]
            max_belf0002 = [max_belf0002_1, max_belf0002_2, max_belf0002_3, max_belf0002_4, max_belf0002_5, max_belf0002_6]

            minterm_belf0002 = [12] * 6
            maxterm_belf0002 = re.findall(r"'mois.>', '(.*?)',", content_belf0002)

        for item in content_belf0002_2:
            TAEG_belf0002 = re.findall(r"fixe<.span>', ':', '(.*?)%'", content_belf0002_2) * 6

        belf0002 = (min_belf0002, max_belf0002, minterm_belf0002, maxterm_belf0002, TAEG_belf0002)

        belf0002_array = np.column_stack((min_belf0002, max_belf0002, minterm_belf0002, maxterm_belf0002, TAEG_belf0002))
        belf0002_tup = tuple(map(tuple, belf0002_array))

        ##########convert everything into a panda df##########

        Min_belf0002 = pd.DataFrame(min_belf0002, columns=['Min'])
        Max_belf0002 = pd.DataFrame(max_belf0002, columns=['Max'])
        amount_belf0002 = Min_belf0002.join(Max_belf0002)

        MinTerm_belf0002 = pd.DataFrame(minterm_belf0002, columns=['Min Term'])
        MaxTerm_belf0002 = pd.DataFrame(maxterm_belf0002, columns=['Max Term'])
        duration_belf0002 = MinTerm_belf0002.join(MaxTerm_belf0002)

        Taux_belf0002 = pd.DataFrame(TAEG_belf0002, columns=['Taux'])

        df_belf0002 = amount_belf0002.join(duration_belf0002)
        df_belf0002 = df_belf0002.join(Taux_belf0002)

        df_belf0002.insert(0, 'Provider', 'Belfius')
        df_belf0002.insert(1, 'Product_ID', 'BELF0002')
        df_belf0002.insert(1, 'Category', 'Vehicle Loan')

        df_belf0002_vl = df_belf0002[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BELF0003###########################################################

        url_belf0003 = 'https://www.belfius.be/retail/fr/produits/emprunter/vehicule/pret-auto-eco/index.aspx'
        html_belf0003 = requests.get(url_belf0003)
        soup_belf0003 = bs4.BeautifulSoup(html_belf0003.content, 'lxml')

        content_belf0003 = soup_belf0003.find_all('table', {'class': "embeddedTable"})
        content_belf0003_2 = soup_belf0003.find_all('section', {'class': "footnote"})
        content_belf0003 = str(str(content_belf0003).split())  # list -> str to ease the RegEx
        content_belf0003_2 = str(str(content_belf0003_2).split())  # list -> str

        for item in content_belf0003:
            min_belf0003_1 = re.findall(r"EUR.\">',.'(.*?)'<.td>'", content_belf0003)[0:1]  # 2500 #dont forget to always add : to make it str
            min_belf0003_1 = str(min_belf0003_1)
            min_belf0003_1 = re.sub('[^0-9a-zA-Z]+', '', min_belf0003_1)
            max_belf0003_1 = min_belf0003_1

            min_belf0003_2 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[0]  # 2500,01
            min_belf0003_2 = str(min_belf0003_2)
            min_belf0003_2 = re.sub("[ ']+", '', min_belf0003_2)
            min_belf0003_2 = re.sub("[,]+", '.', min_belf0003_2, 1)  # replace the first ',' occurance with '.'
            max_belf0003_2 = re.findall(r"'-', '(.*?), '<.td", content_belf0003)[0]
            max_belf0003_2 = str(max_belf0003_2)
            max_belf0003_2 = re.sub("[ ']+", '', max_belf0003_2)
            max_belf0003_2 = re.sub("[,]+", '.', max_belf0003_2, 1)  # replace the first ',' occurance with '.'

            min_belf0003_3 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[1]  # 3700,01
            min_belf0003_3 = str(min_belf0003_3)
            min_belf0003_3 = re.sub("[ ']+", '', min_belf0003_3)
            min_belf0003_3 = re.sub("[,]+", '.', min_belf0003_3, 1)  # replace the first ',' occurance with '.'
            max_belf0003_3 = re.findall(r"'-', '(.*?), '<.td", content_belf0003)[1]  # 5600
            max_belf0003_3 = str(max_belf0003_3)
            max_belf0003_3 = re.sub("[ ']+", '', max_belf0003_3)
            max_belf0003_3 = re.sub("[,]+", '.', max_belf0003_3, 1)  # replace the first ',' occurance with '.'

            min_belf0003_4 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[2]  # 5600,01
            min_belf0003_4 = str(min_belf0003_4)
            min_belf0003_4 = re.sub("[ ']+", '', min_belf0003_4)
            min_belf0003_4 = re.sub("[,]+", '.', min_belf0003_4, 1)  # replace the first ',' occurance with '.'
            max_belf0003_4 = re.findall(r"'-', '(.*?), '<.td", content_belf0003)[2]  # 7500
            max_belf0003_4 = str(max_belf0003_4)
            max_belf0003_4 = re.sub("[ ']+", '', max_belf0003_4)
            max_belf0003_4 = re.sub("[,]+", '.', max_belf0003_4, 1)  # replace the first ',' occurance with '.'

            min_belf0003_5 = re.findall(r"<.td>', '<.tr>', '<tr>', '<td', 'data-title=.Montant', '.en', 'EUR..>', '(.*?)', '-'", content_belf0001)[3]  # 7500,01
            min_belf0003_5 = str(min_belf0003_5)
            min_belf0003_5 = re.sub("[ ']+", '', min_belf0003_5)
            min_belf0003_5 = re.sub("[,]+", '.', min_belf0003_5, 1)  # replace the first ',' occurance with '.'
            max_belf0003_5 = re.findall(r"'-', '(.*?), '<.td", content_belf0003)[3]  # 10000
            max_belf0003_5 = str(max_belf0003_5)
            max_belf0003_5 = re.sub("[ ']+", '', max_belf0003_5)
            max_belf0003_5 = re.sub("[,]+", '.', max_belf0003_5, 1)  # replace the first ',' occurance with '.'

            min_belf0003_6 = re.findall(r"'48'.*EUR..>', '(.*?), '–', 'illimit", content_belf0003)[0]  # 10000,01
            min_belf0003_6 = str(min_belf0003_6)
            min_belf0003_6 = re.sub('[ "]+', '', min_belf0003_6)
            min_belf0003_6 = re.sub("[ ']+", '', min_belf0003_6)
            min_belf0003_6 = re.sub("[,]+", '.', min_belf0003_6, 1)  # replace the first ',' occurance with '.'
            max_belf0003_6 = re.findall(r"'–', .(.*?)'", content_belf0003)[0]  # illimité

            min_belf0003 = [min_belf0003_1, min_belf0003_2, min_belf0003_3, min_belf0003_4, min_belf0003_5, min_belf0003_6]
            max_belf0003 = [max_belf0003_1, max_belf0003_2, max_belf0003_3, max_belf0003_4, max_belf0003_5, max_belf0003_6]

            minterm_belf0003 = [4] * 6
            maxterm_belf0003 = re.findall(r"'mois.>', '(.*?)',", content_belf0003)

        for item in content_belf0003_2:
            TAEG_belf0003 = re.findall(r">fixe<.span>', ':(.*?)%., .", content_belf0003_2) * 6

        belf0003 = (min_belf0003, max_belf0003, minterm_belf0003, maxterm_belf0003, TAEG_belf0003)

        belf0003_array = np.column_stack((min_belf0003, max_belf0003, minterm_belf0003, maxterm_belf0003, TAEG_belf0003))
        belf0003_tup = tuple(map(tuple, belf0003_array))

        ##########convert everything into a panda df##########

        Min_belf0003 = pd.DataFrame(min_belf0003, columns=['Min'])
        Max_belf0003 = pd.DataFrame(max_belf0003, columns=['Max'])
        amount_belf0003 = Min_belf0003.join(Max_belf0003)

        MinTerm_belf0003 = pd.DataFrame(minterm_belf0003, columns=['Min Term'])
        MaxTerm_belf0003 = pd.DataFrame(maxterm_belf0003, columns=['Max Term'])
        duration_belf0003 = MinTerm_belf0003.join(MaxTerm_belf0003)

        Taux_belf0003 = pd.DataFrame(TAEG_belf0003, columns=['Taux'])

        df_belf0003 = amount_belf0003.join(duration_belf0003)
        df_belf0003 = df_belf0003.join(Taux_belf0003)

        df_belf0003.insert(0, 'Provider', 'Belfius')
        df_belf0003.insert(1, 'Product_ID', 'BELF0003')
        df_belf0003.insert(1, 'Category', 'Vehicle Loan')

        df_belf0003_vl = df_belf0003[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BELF0001###########################################################

        url_belf0004 = 'https://www.belfius.be/retail/fr/produits/emprunter/habitation/pret-renovation/index.aspx'
        html_belf0004 = requests.get(url_belf0004)
        soup_belf0004 = bs4.BeautifulSoup(html_belf0004.content, 'lxml')

        content_belf0004 = soup_belf0004.find_all('table', {'class': "embeddedTable"})
        content_belf0004_2 = soup_belf0004.find_all('section', {'class': "footnote"})
        content_belf0004 = str(str(content_belf0004).split())  # list -> str to ease the RegEx
        content_belf0004_2 = str(str(content_belf0004_2).split())  # list -> str

        for item in content_belf0004:
            min_belf0004 = re.findall(r"EUR.\">',.'(.*?).. '.', ", content_belf0004)
            max_belf0004 = re.findall(r".. '.', '(.*?)', '<.td>',", content_belf0004)
            minterm_belf0004 = [4, 4, 4, 4, 4, 4, 49, 85]
            maxterm_belf0004 = re.findall(r"'mois.>', '(.*?)',", content_belf0004)

        for item in content_belf0004_2:
            TAEG_belf0004 = re.findall(r">fixe<.span>', ':(.*?)%., .", content_belf0004_2) * 8

        belf0004 = (min_belf0004, max_belf0004, minterm_belf0004, maxterm_belf0004, TAEG_belf0004)

        belf0004_array = np.column_stack((min_belf0004, max_belf0004, minterm_belf0004, maxterm_belf0004, TAEG_belf0004))
        belf0004_tup = tuple(map(tuple, belf0004_array))

        ########convert everything into a panda df##########

        Min_belf0004 = pd.DataFrame(min_belf0004, columns=['Min'])
        Max_belf0004 = pd.DataFrame(max_belf0004, columns=['Max'])
        amount_belf0004 = Min_belf0004.join(Max_belf0004)

        MinTerm_belf0004 = pd.DataFrame(minterm_belf0004, columns=['Min Term'])
        MaxTerm_belf0004 = pd.DataFrame(maxterm_belf0004, columns=['Max Term'])
        duration_belf0004 = MinTerm_belf0004.join(MaxTerm_belf0004)

        Taux_belf0004 = pd.DataFrame(TAEG_belf0004, columns=['Taux'])

        df_belf0004 = amount_belf0004.join(duration_belf0004)
        df_belf0004 = df_belf0004.join(Taux_belf0004)

        df_belf0004.insert(0, 'Provider', 'Belfius')
        df_belf0004.insert(1, 'Product_ID', 'BELF0004')
        df_belf0004.insert(1, 'Category', 'Renovation Loan')

        df_belf0004_vl = df_belf0004[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns


        ###############################################################################################################
        ############################################BELF0005###########################################################

        url_belf0005 = 'https://www.belfius.be/retail/fr/produits/emprunter/habitation/pret-renovation-eco/index.aspx'
        html_belf0005 = requests.get(url_belf0005)
        soup_belf0005 = bs4.BeautifulSoup(html_belf0005.content, 'lxml')

        content_belf0005 = soup_belf0005.find_all('table', {'class': "embeddedTable"})
        content_belf0005_2 = soup_belf0005.find_all('section', {'class': "footnote"})
        content_belf0005 = str(str(content_belf0005).split())  # list -> str to ease the RegEx
        content_belf0005_2 = str(str(content_belf0005_2).split())  # list -> str

        for item in content_belf0005:
            min_belf0005 = re.findall(r"en', 'EUR..>', '(.*?)', ", content_belf0005)
            max_belf0005 = re.findall(r"'.', '(.*?)', '..td", content_belf0005)
            minterm_belf0005 = [4, 25, 25, 37, 37, 49, 61, 85]
            maxterm_belf0005 = re.findall(r"'mois.>', '(.*?)',", content_belf0005)

        for item in content_belf0005_2:
            TAEG_belf0005 = re.findall(r"fixe<.span>:', '(.*?)%'. ..br.", content_belf0005_2) * 8

        belf0005 = (min_belf0005, max_belf0005, minterm_belf0005, maxterm_belf0005, TAEG_belf0005)

        belf0005_array = np.column_stack((belf0005))
        belf0005_tup = tuple(map(tuple, belf0005_array))

        ########convert everything into a panda df##########

        Min_belf0005 = pd.DataFrame(min_belf0005, columns=['Min'])
        Max_belf0005 = pd.DataFrame(max_belf0005, columns=['Max'])
        amount_belf0005 = Min_belf0005.join(Max_belf0005)

        MinTerm_belf0005 = pd.DataFrame(minterm_belf0005, columns=['Min Term'])
        MaxTerm_belf0005 = pd.DataFrame(maxterm_belf0005, columns=['Max Term'])
        duration_belf0005 = MinTerm_belf0005.join(MaxTerm_belf0005)

        Taux_belf0005 = pd.DataFrame(TAEG_belf0005, columns=['Taux'])

        df_belf0005 = amount_belf0005.join(duration_belf0005)
        df_belf0005 = df_belf0005.join(Taux_belf0005)

        df_belf0005.insert(0, 'Provider', 'Belfius')
        df_belf0005.insert(1, 'Product_ID', 'BELF0005')
        df_belf0005.insert(1, 'Category', 'Energy Loan')

        df_belf0005_el = df_belf0005[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BELF0006###########################################################

        url_belf0006 = 'https://www.belfius.be/retail/fr/produits/emprunter/autres-depenses/pret-personnel/index.aspx'

        html_belf0006 = requests.get(url_belf0006)
        soup_belf0006 = bs4.BeautifulSoup(html_belf0006.content, 'lxml')
        content_belf0006 = soup_belf0006.find_all('table', {'class': "embeddedTable"})
        content_belf0006_2 = soup_belf0006.find_all('section', {'id': "tcm87-87989"})
        content_belf0006 = str(str(content_belf0006).split()) #list -> str
        content_belf0006_2 = str(str(content_belf0006_2).split()) #list -> str
        for item in content_belf0006:
            min_belf0006 = re.findall(r"EUR.\">',.'(.*?)',",content_belf0006)
            max_belf0006 = re.findall(r"'.', '(.*?)', '<.td>'",content_belf0006)
            minterm_belf0006 = [12]*8
            maxterm_belf0006 = re.findall(r"mois..'. '(.*?)',",content_belf0006)
        for item in content_belf0006_2:
            TAEG_belf0006 = re.findall(r"de', '(.*?)%",content_belf0006_2)*8
        belf0006  = (min_belf0006, max_belf0006, minterm_belf0006, maxterm_belf0006, TAEG_belf0006)


        belf0006_array = np.column_stack((min_belf0006, max_belf0006, minterm_belf0006, maxterm_belf0006, TAEG_belf0006))
        belf0006_tup = tuple(map(tuple, belf0006_array))

        ##########convert everything into a panda df##########

        Min_belf0006 = pd.DataFrame(min_belf0006, columns=['Min'])
        Max_belf0006 = pd.DataFrame(max_belf0006, columns=['Max'])
        amount_belf0006 = Min_belf0006.join(Max_belf0006)

        MinTerm_belf0006 = pd.DataFrame(minterm_belf0006, columns=['Min Term'])
        MaxTerm_belf0006 = pd.DataFrame(maxterm_belf0006, columns=['Max Term'])
        duration_belf0006 = MinTerm_belf0006.join(MaxTerm_belf0006)

        Taux_belf0006 = pd.DataFrame(TAEG_belf0006, columns=['Taux'])

        df_belf0006 = amount_belf0006.join(duration_belf0006)
        df_belf0006 = df_belf0006.join(Taux_belf0006)

        df_belf0006.insert(0, 'Provider', 'Belfius')
        df_belf0006.insert(1, 'Product_ID', 'BELF0006')
        df_belf0006.insert(1, 'Category', 'Personal Loan')

        df_belf0006_pl = df_belf0006[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']] # Change order of columns

        belfius_loans_c = pd.concat([pd.concat([df_belf0001_vl], axis=1),
                                     pd.concat([df_belf0002_vl], axis=1),
                                     pd.concat([df_belf0003_vl], axis=1),
                                     pd.concat([df_belf0004_vl], axis=1),
                                     pd.concat([df_belf0005_el], axis=1),
                                     pd.concat([df_belf0006_pl], axis=1)])
        print(tabulate(belfius_loans_c, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass


def belfius_save_loans():
    belfius_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    belfius_loans_c.to_csv(os.path.join(path, file_name), index=False)


# #  _                _                 _     # #
# # | |              | |               | |    # #
# # | | _   ____ ___ | | _   ____ ____ | |  _ # #
# # | || \ / _  ) _ \| || \ / _  |  _ \| | / )# #
# # | |_) | (/ / |_| | |_) | ( | | | | | |< ( # #
# # |____/ \____)___/|____/ \_||_|_| |_|_| \_)# #

def beobank_loans():
    try:
        global df_beob0001_loans
        url_beob0001_loans = 'https://www.beobank.be/fr/particulier/emprunter/prets-pour-projet/pret-personnel?dclid=CMfY_b6jzNQCFZiadwodwB0Osg'
        page_beob0001_loans = requests.get(url_beob0001_loans).content
        soup_beob0001_loans = BeautifulSoup(page_beob0001_loans, "lxml")
        pattern_beob0001_loans = re.compile(r"beobank_simulator")
        script_beob0001_loans = soup_beob0001_loans.find("script", text=pattern_beob0001_loans)

        PL_beob0001_loans = str(script_beob0001_loans)

        for item in PL_beob0001_loans:
            bank_beob0001_loans = ['Beobank']
            product_id_beob0001_loans = ['BEOB0001']
            category_beob00001_loans = ['Personal Loan']
            min_beob0001_loans = re.findall(r'"amount":{"min":"(.*?)",', PL_beob0001_loans)
            max_beob0001_loans = re.findall(r'"max":"(.*?)","value"', PL_beob0001_loans)
            minterm_beob0001_loans = re.findall(r'"customTerm":{"min":"(.*?)"', PL_beob0001_loans)
            maxterm_beob0001_loans = re.findall(r'"12","max":"(.*?)",', PL_beob0001_loans)
            TAEG_beob0001_loans = re.findall(r'"tarif":"(.*?)"', PL_beob0001_loans)
        all_beob0001 = bank_beob0001_loans + product_id_beob0001_loans + category_beob00001_loans + min_beob0001_loans + max_beob0001_loans + minterm_beob0001_loans + maxterm_beob0001_loans + TAEG_beob0001_loans

        df_beob0001_loans = pd.DataFrame([all_beob0001])
        df_beob0001_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        print(tabulate(df_beob0001_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def beobank_save_loans():
    beobank_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_beob0001_loans.to_csv(os.path.join(path, file_name), index=False)


# # _                            # #
# # | |                     _    # #
# # | | _  ____   ___   ___| |_  # #
# # | || \|  _ \ / _ \ /___)  _) # #
# # | |_) ) | | | |_| |___ | |__ # #
# # |____/| ||_/ \___/(___/ \___)# #
# #       |_|                    # #

def bpost_loans():
    try:
        global bpost_loans_c
        ###############################################################################################################
        ############################################BPOS0001###########################################################

        with urlopen("https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json?id=e1dba04d-b17e-48ed-a81e-ee469446682e") as response:
            source_bpos0001 = response.read()

        data_bpos0001 = json.loads(source_bpos0001)
        data_bpos0001 = json.dumps(data_bpos0001, indent=1)

        for item in data_bpos0001:
            min_bpos0001_3 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[3]
            max_bpos0001_3 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[3]
            minterm_bpos0001_3 = re.findall(r'duration.:.(.*?),', data_bpos0001)[22]
            maxterm_bpos0001_3 = re.findall(r'duration.:.(.*?),', data_bpos0001)[24]
            TAEG_bpos0001_3 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[33]

            min_bpos0001_4 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[4]
            max_bpos0001_4 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[4]
            minterm_bpos0001_4 = re.findall(r'duration.:.(.*?),', data_bpos0001)[33]
            maxterm_bpos0001_4 = re.findall(r'duration.:.(.*?),', data_bpos0001)[36]
            TAEG_bpos0001_4 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[33]

            min_bpos0001_5 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[5]
            max_bpos0001_5 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[5]
            minterm_bpos0001_5 = re.findall(r'duration.:.(.*?),', data_bpos0001)[44]
            maxterm_bpos0001_5 = re.findall(r'duration.:.(.*?),', data_bpos0001)[48]
            TAEG_bpos0001_5 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[44]

            min_bpos0001_6 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[6]
            max_bpos0001_6 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[6]
            minterm_bpos0001_6 = re.findall(r'duration.:.(.*?),', data_bpos0001)[55]
            maxterm_bpos0001_6 = re.findall(r'duration.:.(.*?),', data_bpos0001)[60]
            TAEG_bpos0001_6 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[55]

            min_bpos0001_7 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[7]
            max_bpos0001_7 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[7]
            minterm_bpos0001_7 = re.findall(r'duration.:.(.*?),', data_bpos0001)[66]
            maxterm_bpos0001_7 = re.findall(r'duration.:.(.*?),', data_bpos0001)[73]
            TAEG_bpos0001_7 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[66]

            min_bpos0001_8 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[8]
            max_bpos0001_8 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[8]
            minterm_bpos0001_8 = re.findall(r'duration.:.(.*?),', data_bpos0001)[77]
            maxterm_bpos0001_8 = re.findall(r'duration.:.(.*?),', data_bpos0001)[84]
            TAEG_bpos0001_8 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[77]

            min_bpos0001_9 = re.findall(r'amountMin.:.(.*?),', data_bpos0001)[9]
            max_bpos0001_9 = re.findall(r'amountMax.:.(.*?),', data_bpos0001)[9]
            minterm_bpos0001_9 = re.findall(r'duration.:.(.*?),', data_bpos0001)[88]
            maxterm_bpos0001_9 = re.findall(r'duration.:.(.*?),', data_bpos0001)[95]
            TAEG_bpos0001_9 = re.findall(r'rate.:.(.*?)\n', data_bpos0001)[88]

            ####### concat everything
            min_bpos0001 = min_bpos0001_3, min_bpos0001_4, min_bpos0001_5, min_bpos0001_6, min_bpos0001_7, min_bpos0001_8, min_bpos0001_9
            max_bpos0001 = max_bpos0001_3, max_bpos0001_4, max_bpos0001_5, max_bpos0001_6, max_bpos0001_7, max_bpos0001_8, max_bpos0001_9
            minterm_bpos0001 = minterm_bpos0001_3, minterm_bpos0001_4, minterm_bpos0001_5, minterm_bpos0001_6, minterm_bpos0001_7, minterm_bpos0001_8, minterm_bpos0001_9
            maxterm_bpos0001 = maxterm_bpos0001_3, maxterm_bpos0001_4, maxterm_bpos0001_5, maxterm_bpos0001_6, maxterm_bpos0001_7, maxterm_bpos0001_8, maxterm_bpos0001_9
            TAEG_bpos0001 = TAEG_bpos0001_3, TAEG_bpos0001_4, TAEG_bpos0001_5, TAEG_bpos0001_6, TAEG_bpos0001_7, TAEG_bpos0001_8, TAEG_bpos0001_9

        bpos0001_array = np.column_stack((min_bpos0001, max_bpos0001, minterm_bpos0001, maxterm_bpos0001, TAEG_bpos0001))
        bpos0001_tup = tuple(map(tuple, bpos0001_array))

        ########convert everything into a panda df##########

        Min_bpos0001 = pd.DataFrame(min_bpos0001, columns=['Min'])
        Max_bpos0001 = pd.DataFrame(max_bpos0001, columns=['Max'])
        amount_bpos0001 = Min_bpos0001.join(Max_bpos0001)

        MinTerm_bpos0001 = pd.DataFrame(minterm_bpos0001, columns=['Min Term'])
        MaxTerm_bpos0001 = pd.DataFrame(maxterm_bpos0001, columns=['Max Term'])
        duration_bpos0001 = MinTerm_bpos0001.join(MaxTerm_bpos0001)

        Taux_bpos0001 = pd.DataFrame(TAEG_bpos0001, columns=['Taux'])

        df_bpos0001 = amount_bpos0001.join(duration_bpos0001)
        df_bpos0001 = df_bpos0001.join(Taux_bpos0001)

        df_bpos0001.insert(0, 'Provider', 'BPost')
        df_bpos0001.insert(1, 'Product_ID', 'BPOS0001')
        df_bpos0001.insert(1, 'Category', 'Vehicle Loan')

        df_bpos0001_vl = df_bpos0001[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BPOS0002###########################################################

        with urlopen("https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json?id=5df19404-aba6-4378-8305-67dc65d8eca1") as response:
            source_bpos0002 = response.read()

        data_bpos0002 = json.loads(source_bpos0002)
        data_bpos0002 = json.dumps(data_bpos0002, indent=1)

        for item in data_bpos0002:
            min_bpos0002_3 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[3]
            max_bpos0002_3 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[3]
            minterm_bpos0002_3 = re.findall(r'duration.:.(.*?),', data_bpos0002)[22]
            maxterm_bpos0002_3 = re.findall(r'duration.:.(.*?),', data_bpos0002)[24]
            TAEG_bpos0002_3 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[33]

            min_bpos0002_4 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[4]
            max_bpos0002_4 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[4]
            minterm_bpos0002_4 = re.findall(r'duration.:.(.*?),', data_bpos0002)[33]
            maxterm_bpos0002_4 = re.findall(r'duration.:.(.*?),', data_bpos0002)[36]
            TAEG_bpos0002_4 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[33]

            min_bpos0002_5 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[5]
            max_bpos0002_5 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[5]
            minterm_bpos0002_5 = re.findall(r'duration.:.(.*?),', data_bpos0002)[44]
            maxterm_bpos0002_5 = re.findall(r'duration.:.(.*?),', data_bpos0002)[48]
            TAEG_bpos0002_5 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[44]

            min_bpos0002_6 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[6]
            max_bpos0002_6 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[6]
            minterm_bpos0002_6 = re.findall(r'duration.:.(.*?),', data_bpos0002)[55]
            maxterm_bpos0002_6 = re.findall(r'duration.:.(.*?),', data_bpos0002)[60]
            TAEG_bpos0002_6 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[55]

            min_bpos0002_7 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[7]
            max_bpos0002_7 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[7]
            minterm_bpos0002_7 = re.findall(r'duration.:.(.*?),', data_bpos0002)[66]
            maxterm_bpos0002_7 = re.findall(r'duration.:.(.*?),', data_bpos0002)[73]
            TAEG_bpos0002_7 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[66]

            min_bpos0002_8 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[8]
            max_bpos0002_8 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[8]
            minterm_bpos0002_8 = re.findall(r'duration.:.(.*?),', data_bpos0002)[77]
            maxterm_bpos0002_8 = re.findall(r'duration.:.(.*?),', data_bpos0002)[84]
            TAEG_bpos0002_8 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[77]

            min_bpos0002_9 = re.findall(r'amountMin.:.(.*?),', data_bpos0002)[9]
            max_bpos0002_9 = re.findall(r'amountMax.:.(.*?),', data_bpos0002)[9]
            minterm_bpos0002_9 = re.findall(r'duration.:.(.*?),', data_bpos0002)[88]
            maxterm_bpos0002_9 = re.findall(r'duration.:.(.*?),', data_bpos0002)[95]
            TAEG_bpos0002_9 = re.findall(r'rate.:.(.*?)\n', data_bpos0002)[88]

            ####### concat everything
            min_bpos0002 = min_bpos0002_3, min_bpos0002_4, min_bpos0002_5, min_bpos0002_6, min_bpos0002_7, min_bpos0002_8, min_bpos0002_9
            max_bpos0002 = max_bpos0002_3, max_bpos0002_4, max_bpos0002_5, max_bpos0002_6, max_bpos0002_7, max_bpos0002_8, max_bpos0002_9
            minterm_bpos0002 = minterm_bpos0002_3, minterm_bpos0002_4, minterm_bpos0002_5, minterm_bpos0002_6, minterm_bpos0002_7, minterm_bpos0002_8, minterm_bpos0002_9
            maxterm_bpos0002 = maxterm_bpos0002_3, maxterm_bpos0002_4, maxterm_bpos0002_5, maxterm_bpos0002_6, maxterm_bpos0002_7, maxterm_bpos0002_8, maxterm_bpos0002_9
            TAEG_bpos0002 = TAEG_bpos0002_3, TAEG_bpos0002_4, TAEG_bpos0002_5, TAEG_bpos0002_6, TAEG_bpos0002_7, TAEG_bpos0002_8, TAEG_bpos0002_9

        bpos0002_array = np.column_stack((min_bpos0002, max_bpos0002, minterm_bpos0002, maxterm_bpos0002, TAEG_bpos0002))
        bpos0002_tup = tuple(map(tuple, bpos0002_array))

        ########convert everything into a panda df##########

        Min_bpos0002 = pd.DataFrame(min_bpos0002, columns=['Min'])
        Max_bpos0002 = pd.DataFrame(max_bpos0002, columns=['Max'])
        amount_bpos0002 = Min_bpos0002.join(Max_bpos0002)

        MinTerm_bpos0002 = pd.DataFrame(minterm_bpos0002, columns=['Min Term'])
        MaxTerm_bpos0002 = pd.DataFrame(maxterm_bpos0002, columns=['Max Term'])
        duration_bpos0002 = MinTerm_bpos0002.join(MaxTerm_bpos0002)

        Taux_bpos0002 = pd.DataFrame(TAEG_bpos0002, columns=['Taux'])

        df_bpos0002 = amount_bpos0002.join(duration_bpos0002)
        df_bpos0002 = df_bpos0002.join(Taux_bpos0002)

        df_bpos0002.insert(0, 'Provider', 'BPost')
        df_bpos0002.insert(1, 'Product_ID', 'BPOS0002')
        df_bpos0002.insert(1, 'Category', 'Vehicle Loan')

        df_bpos0002_vl = df_bpos0002[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BPOS0003###########################################################

        with urlopen("https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json?id=a8e34124-daf4-4138-b7b9-c8e65ec0fcf6") as response:
            source_bpos0003 = response.read()

        data_bpos0003 = json.loads(source_bpos0003)
        data_bpos0003 = json.dumps(data_bpos0003, indent=1)

        for item in data_bpos0003:
            min_bpos0003_2 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[2]
            max_bpos0003_2 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[2]
            minterm_bpos0003_2 = re.findall(r'duration.:.(.*?),', data_bpos0003)[22]
            maxterm_bpos0003_2 = re.findall(r'duration.:.(.*?),', data_bpos0003)[24]
            TAEG_bpos0003_2 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[22]

            min_bpos0003_3 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[3]
            max_bpos0003_3 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[3]
            minterm_bpos0003_3 = re.findall(r'duration.:.(.*?),', data_bpos0003)[33]
            maxterm_bpos0003_3 = re.findall(r'duration.:.(.*?),', data_bpos0003)[36]
            TAEG_bpos0003_3 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[33]

            min_bpos0003_4 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[4]
            max_bpos0003_4 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[4]
            minterm_bpos0003_4 = re.findall(r'duration.:.(.*?),', data_bpos0003)[44]
            maxterm_bpos0003_4 = re.findall(r'duration.:.(.*?),', data_bpos0003)[48]
            TAEG_bpos0003_4 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[44]

            min_bpos0003_5 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[5]
            max_bpos0003_5 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[5]
            minterm_bpos0003_5 = re.findall(r'duration.:.(.*?),', data_bpos0003)[55]
            maxterm_bpos0003_5 = re.findall(r'duration.:.(.*?),', data_bpos0003)[60]
            TAEG_bpos0003_5 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[55]

            min_bpos0003_6 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[6]
            max_bpos0003_6 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[6]
            minterm_bpos0003_6 = re.findall(r'duration.:.(.*?),', data_bpos0003)[66]
            maxterm_bpos0003_6 = re.findall(r'duration.:.(.*?),', data_bpos0003)[73]
            TAEG_bpos0003_6 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[67]

            min_bpos0003_7 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[7]
            max_bpos0003_7 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[7]
            minterm_bpos0003_7 = re.findall(r'duration.:.(.*?),', data_bpos0003)[77]
            maxterm_bpos0003_7 = re.findall(r'duration.:.(.*?),', data_bpos0003)[87]
            TAEG_bpos0003_7 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[78]

            min_bpos0003_8 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[8]
            max_bpos0003_8 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[8]
            minterm_bpos0003_8 = re.findall(r'duration.:.(.*?),', data_bpos0003)[88]
            maxterm_bpos0003_8 = re.findall(r'duration.:.(.*?),', data_bpos0003)[98]
            TAEG_bpos0003_8 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[88]

            min_bpos0003_9 = re.findall(r'amountMin.:.(.*?),', data_bpos0003)[9]
            max_bpos0003_9 = re.findall(r'amountMax.:.(.*?),', data_bpos0003)[9]
            minterm_bpos0003_9 = re.findall(r'duration.:.(.*?),', data_bpos0003)[99]
            maxterm_bpos0003_9 = re.findall(r'duration.:.(.*?),', data_bpos0003)[109]
            TAEG_bpos0003_9 = re.findall(r'rate.:.(.*?)\n', data_bpos0003)[99]

            ####### concat everything
            min_bpos0003 = min_bpos0003_2, min_bpos0003_3, min_bpos0003_4, min_bpos0003_5, min_bpos0003_6, min_bpos0003_7, min_bpos0003_8, min_bpos0003_9
            max_bpos0003 = max_bpos0003_2, max_bpos0003_3, max_bpos0003_4, max_bpos0003_5, max_bpos0003_6, max_bpos0003_7, max_bpos0003_8, max_bpos0003_9
            minterm_bpos0003 = minterm_bpos0003_2, minterm_bpos0003_3, minterm_bpos0003_4, minterm_bpos0003_5, minterm_bpos0003_6, minterm_bpos0003_7, minterm_bpos0003_8, minterm_bpos0003_9
            maxterm_bpos0003 = maxterm_bpos0003_2, maxterm_bpos0003_3, maxterm_bpos0003_4, maxterm_bpos0003_5, maxterm_bpos0003_6, maxterm_bpos0003_7, maxterm_bpos0003_8, maxterm_bpos0003_9
            TAEG_bpos0003 = TAEG_bpos0003_2, TAEG_bpos0003_3, TAEG_bpos0003_4, TAEG_bpos0003_5, TAEG_bpos0003_6, TAEG_bpos0003_7, TAEG_bpos0003_8, TAEG_bpos0003_9

        bpos0003_array = np.column_stack((min_bpos0003, max_bpos0003, minterm_bpos0003, maxterm_bpos0003, TAEG_bpos0003))
        bpos0003_tup = tuple(map(tuple, bpos0003_array))

        ########convert everything into a panda df##########

        Min_bpos0003 = pd.DataFrame(min_bpos0003, columns=['Min'])
        Max_bpos0003 = pd.DataFrame(max_bpos0003, columns=['Max'])
        amount_bpos0003 = Min_bpos0003.join(Max_bpos0003)

        MinTerm_bpos0003 = pd.DataFrame(minterm_bpos0003, columns=['Min Term'])
        MaxTerm_bpos0003 = pd.DataFrame(maxterm_bpos0003, columns=['Max Term'])
        duration_bpos0003 = MinTerm_bpos0003.join(MaxTerm_bpos0003)

        Taux_bpos0003 = pd.DataFrame(TAEG_bpos0003, columns=['Taux'])

        df_bpos0003 = amount_bpos0003.join(duration_bpos0003)
        df_bpos0003 = df_bpos0003.join(Taux_bpos0003)

        df_bpos0003.insert(0, 'Provider', 'BPost')
        df_bpos0003.insert(1, 'Product_ID', 'BPOS0003')
        df_bpos0003.insert(1, 'Category', 'Energy Loan')

        df_bpos0003_el = df_bpos0003[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BPOS0004###########################################################

        with urlopen("https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json?id=21a13d82-44cc-4080-8715-8d866ed7b5df") as response:
            source_bpos0004 = response.read()

        data_bpos0004 = json.loads(source_bpos0004)
        data_bpos0004 = json.dumps(data_bpos0004, indent=1)

        for item in data_bpos0004:
            min_bpos0004_3 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[3]
            max_bpos0004_3 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[3]
            minterm_bpos0004_3 = re.findall(r'duration.:.(.*?),', data_bpos0004)[22]
            maxterm_bpos0004_3 = re.findall(r'duration.:.(.*?),', data_bpos0004)[24]
            TAEG_bpos0004_3 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[33]

            min_bpos0004_4 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[4]
            max_bpos0004_4 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[4]
            minterm_bpos0004_4 = re.findall(r'duration.:.(.*?),', data_bpos0004)[33]
            maxterm_bpos0004_4 = re.findall(r'duration.:.(.*?),', data_bpos0004)[36]
            TAEG_bpos0004_4 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[33]

            min_bpos0004_5 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[5]
            max_bpos0004_5 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[5]
            minterm_bpos0004_5 = re.findall(r'duration.:.(.*?),', data_bpos0004)[44]
            maxterm_bpos0004_5 = re.findall(r'duration.:.(.*?),', data_bpos0004)[48]
            TAEG_bpos0004_5 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[44]

            min_bpos0004_6 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[6]
            max_bpos0004_6 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[6]
            minterm_bpos0004_6 = re.findall(r'duration.:.(.*?),', data_bpos0004)[55]
            maxterm_bpos0004_6 = re.findall(r'duration.:.(.*?),', data_bpos0004)[60]
            TAEG_bpos0004_6 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[55]

            min_bpos0004_7 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[7]
            max_bpos0004_7 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[7]
            minterm_bpos0004_7 = re.findall(r'duration.:.(.*?),', data_bpos0004)[66]
            maxterm_bpos0004_7 = re.findall(r'duration.:.(.*?),', data_bpos0004)[73]
            TAEG_bpos0004_7 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[66]

            min_bpos0004_8 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[8]
            max_bpos0004_8 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[8]
            minterm_bpos0004_8 = re.findall(r'duration.:.(.*?),', data_bpos0004)[77]
            maxterm_bpos0004_8 = re.findall(r'duration.:.(.*?),', data_bpos0004)[84]
            TAEG_bpos0004_8 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[77]

            min_bpos0004_9 = re.findall(r'amountMin.:.(.*?),', data_bpos0004)[9]
            max_bpos0004_9 = re.findall(r'amountMax.:.(.*?),', data_bpos0004)[9]
            minterm_bpos0004_9 = re.findall(r'duration.:.(.*?),', data_bpos0004)[88]
            maxterm_bpos0004_9 = re.findall(r'duration.:.(.*?),', data_bpos0004)[95]
            TAEG_bpos0004_9 = re.findall(r'rate.:.(.*?)\n', data_bpos0004)[88]

            ####### concat everything
            min_bpos0004 = min_bpos0004_3, min_bpos0004_4, min_bpos0004_5, min_bpos0004_6, min_bpos0004_7, min_bpos0004_8, min_bpos0004_9
            max_bpos0004 = max_bpos0004_3, max_bpos0004_4, max_bpos0004_5, max_bpos0004_6, max_bpos0004_7, max_bpos0004_8, max_bpos0004_9
            minterm_bpos0004 = minterm_bpos0004_3, minterm_bpos0004_4, minterm_bpos0004_5, minterm_bpos0004_6, minterm_bpos0004_7, minterm_bpos0004_8, minterm_bpos0004_9
            maxterm_bpos0004 = maxterm_bpos0004_3, maxterm_bpos0004_4, maxterm_bpos0004_5, maxterm_bpos0004_6, maxterm_bpos0004_7, maxterm_bpos0004_8, maxterm_bpos0004_9
            TAEG_bpos0004 = TAEG_bpos0004_3, TAEG_bpos0004_4, TAEG_bpos0004_5, TAEG_bpos0004_6, TAEG_bpos0004_7, TAEG_bpos0004_8, TAEG_bpos0004_9

        bpos0004_array = np.column_stack((min_bpos0004, max_bpos0004, minterm_bpos0004, maxterm_bpos0004, TAEG_bpos0004))
        bpos0004_tup = tuple(map(tuple, bpos0004_array))

        ########convert everything into a panda df##########

        Min_bpos0004 = pd.DataFrame(min_bpos0004, columns=['Min'])
        Max_bpos0004 = pd.DataFrame(max_bpos0004, columns=['Max'])
        amount_bpos0004 = Min_bpos0004.join(Max_bpos0004)

        MinTerm_bpos0004 = pd.DataFrame(minterm_bpos0004, columns=['Min Term'])
        MaxTerm_bpos0004 = pd.DataFrame(maxterm_bpos0004, columns=['Max Term'])
        duration_bpos0004 = MinTerm_bpos0004.join(MaxTerm_bpos0004)

        Taux_bpos0004 = pd.DataFrame(TAEG_bpos0004, columns=['Taux'])

        df_bpos0004 = amount_bpos0004.join(duration_bpos0004)
        df_bpos0004 = df_bpos0004.join(Taux_bpos0004)

        df_bpos0004.insert(0, 'Provider', 'BPost')
        df_bpos0004.insert(1, 'Product_ID', 'BPOS0004')
        df_bpos0004.insert(1, 'Category', 'Renovation Loan')

        df_bpos0004_rl = df_bpos0004[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        ###############################################################################################################
        ############################################BPOS0005###########################################################

        with urlopen("https://www.bpostbanque.be/bpb/content/atom/03c8f78e-d33a-47a5-9778-76ee8239a51c/content/data.json?id=f0c6687c-ceba-405d-9e44-565dcc749344") as response:
            source_bpos0005 = response.read()

        data_bpos0005 = json.loads(source_bpos0005)
        # print(json.dumps(data_bpost, indent=1))
        data_bpos0005 = json.dumps(data_bpos0005, indent=1)

        for item in data_bpos0005:
            min_bpos0005_1 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[0]
            max_bpos0005_1 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[0]
            minterm_bpos0005_1 = re.findall(r'duration.:.(.*?),', data_bpos0005)[0]
            maxterm_bpos0005_1 = re.findall(r'duration.:.(.*?),', data_bpos0005)[0]
            TAEG_bpos0005_1 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[0]

            min_bpos0005_2 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[1]
            max_bpos0005_2 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[1]
            minterm_bpos0005_2 = re.findall(r'duration.:.(.*?),', data_bpos0005)[11]
            maxterm_bpos0005_2 = re.findall(r'duration.:.(.*?),', data_bpos0005)[12]
            TAEG_bpos0005_2 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[11]

            min_bpos0005_3 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[2]
            max_bpos0005_3 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[2]
            minterm_bpos0005_3 = re.findall(r'duration.:.(.*?),', data_bpos0005)[22]
            maxterm_bpos0005_3 = re.findall(r'duration.:.(.*?),', data_bpos0005)[23]
            TAEG_bpos0005_3 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[22]
            minterm_bpos0005_3b = re.findall(r'duration.:.(.*?),', data_bpos0005)[24]
            maxterm_bpos0005_3b = re.findall(r'duration.:.(.*?),', data_bpos0005)[24]
            TAEG_bpos0005_3b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[24]

            min_bpos0005_4 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[3]
            max_bpos0005_4 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[3]
            minterm_bpos0005_4 = re.findall(r'duration.:.(.*?),', data_bpos0005)[33]
            maxterm_bpos0005_4 = re.findall(r'duration.:.(.*?),', data_bpos0005)[33]
            TAEG_bpos0005_4 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[33]
            minterm_bpos0005_4b = re.findall(r'duration.:.(.*?),', data_bpos0005)[35]
            maxterm_bpos0005_4b = re.findall(r'duration.:.(.*?),', data_bpos0005)[35]
            TAEG_bpos0005_4b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[35]

            min_bpos0005_5 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[4]
            max_bpos0005_5 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[4]
            minterm_bpos0005_5 = re.findall(r'duration.:.(.*?),', data_bpos0005)[44]
            maxterm_bpos0005_5 = re.findall(r'duration.:.(.*?),', data_bpos0005)[45]
            TAEG_bpos0005_5 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[44]
            minterm_bpos0005_5b = re.findall(r'duration.:.(.*?),', data_bpos0005)[46]
            maxterm_bpos0005_5b = re.findall(r'duration.:.(.*?),', data_bpos0005)[46]
            TAEG_bpos0005_5b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[46]
            minterm_bpos0005_5c = re.findall(r'duration.:.(.*?),', data_bpos0005)[47]
            maxterm_bpos0005_5c = re.findall(r'duration.:.(.*?),', data_bpos0005)[47]
            TAEG_bpos0005_5c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[47]

            min_bpos0005_6 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[5]
            max_bpos0005_6 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[5]
            minterm_bpos0005_6 = re.findall(r'duration.:.(.*?),', data_bpos0005)[55]
            maxterm_bpos0005_6 = re.findall(r'duration.:.(.*?),', data_bpos0005)[56]
            TAEG_bpos0005_6 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[55]
            minterm_bpos0005_6b = re.findall(r'duration.:.(.*?),', data_bpos0005)[57]
            maxterm_bpos0005_6b = re.findall(r'duration.:.(.*?),', data_bpos0005)[57]
            TAEG_bpos0005_6b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[57]
            minterm_bpos0005_6c = re.findall(r'duration.:.(.*?),', data_bpos0005)[58]
            maxterm_bpos0005_6c = re.findall(r'duration.:.(.*?),', data_bpos0005)[58]
            TAEG_bpos0005_6c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[58]
            minterm_bpos0005_6d = re.findall(r'duration.:.(.*?),', data_bpos0005)[59]
            maxterm_bpos0005_6d = re.findall(r'duration.:.(.*?),', data_bpos0005)[59]
            TAEG_bpos0005_6d = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[59]

            min_bpos0005_7 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[6]
            max_bpos0005_7 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[6]
            minterm_bpos0005_7b = re.findall(r'duration.:.(.*?),', data_bpos0005)[66]
            maxterm_bpos0005_7b = re.findall(r'duration.:.(.*?),', data_bpos0005)[67]
            TAEG_bpos0005_7b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[67]
            minterm_bpos0005_7c = re.findall(r'duration.:.(.*?),', data_bpos0005)[68]
            maxterm_bpos0005_7c = re.findall(r'duration.:.(.*?),', data_bpos0005)[68]
            TAEG_bpos0005_7c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[68]
            minterm_bpos0005_7d = re.findall(r'duration.:.(.*?),', data_bpos0005)[69]
            maxterm_bpos0005_7d = re.findall(r'duration.:.(.*?),', data_bpos0005)[69]
            TAEG_bpos0005_7d = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[69]
            minterm_bpos0005_7e = re.findall(r'duration.:.(.*?),', data_bpos0005)[70]
            maxterm_bpos0005_7e = re.findall(r'duration.:.(.*?),', data_bpos0005)[70]
            TAEG_bpos0005_7e = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[70]
            minterm_bpos0005_7f = re.findall(r'duration.:.(.*?),', data_bpos0005)[71]
            maxterm_bpos0005_7f = re.findall(r'duration.:.(.*?),', data_bpos0005)[71]
            TAEG_bpos0005_7f = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[71]

            min_bpos0005_8 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[7]
            max_bpos0005_8 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[7]
            minterm_bpos0005_8 = re.findall(r'duration.:.(.*?),', data_bpos0005)[77]
            maxterm_bpos0005_8 = re.findall(r'duration.:.(.*?),', data_bpos0005)[78]
            TAEG_bpos0005_8 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[77]
            minterm_bpos0005_8b = re.findall(r'duration.:.(.*?),', data_bpos0005)[79]
            maxterm_bpos0005_8b = re.findall(r'duration.:.(.*?),', data_bpos0005)[79]
            TAEG_bpos0005_8b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[79]
            minterm_bpos0005_8c = re.findall(r'duration.:.(.*?),', data_bpos0005)[80]
            maxterm_bpos0005_8c = re.findall(r'duration.:.(.*?),', data_bpos0005)[80]
            TAEG_bpos0005_8c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[80]
            minterm_bpos0005_8d = re.findall(r'duration.:.(.*?),', data_bpos0005)[81]
            maxterm_bpos0005_8d = re.findall(r'duration.:.(.*?),', data_bpos0005)[81]
            TAEG_bpos0005_8d = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[81]
            minterm_bpos0005_8e = re.findall(r'duration.:.(.*?),', data_bpos0005)[82]
            maxterm_bpos0005_8e = re.findall(r'duration.:.(.*?),', data_bpos0005)[82]
            TAEG_bpos0005_8e = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[82]
            minterm_bpos0005_8f = re.findall(r'duration.:.(.*?),', data_bpos0005)[83]
            maxterm_bpos0005_8f = re.findall(r'duration.:.(.*?),', data_bpos0005)[84]
            TAEG_bpos0005_8f = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[83]

            min_bpost_9 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[8]
            max_bpost_9 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[8]
            minterm_bpost_9 = re.findall(r'duration.:.(.*?),', data_bpos0005)[88]
            maxterm_bpost_9 = re.findall(r'duration.:.(.*?),', data_bpos0005)[89]
            TAEG_bpost_9 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[88]
            minterm_bpost_9b = re.findall(r'duration.:.(.*?),', data_bpos0005)[90]
            maxterm_bpost_9b = re.findall(r'duration.:.(.*?),', data_bpos0005)[90]
            TAEG_bpost_9b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[90]
            minterm_bpost_9c = re.findall(r'duration.:.(.*?),', data_bpos0005)[91]
            maxterm_bpost_9c = re.findall(r'duration.:.(.*?),', data_bpos0005)[91]
            TAEG_bpost_9c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[91]
            minterm_bpost_9d = re.findall(r'duration.:.(.*?),', data_bpos0005)[92]
            maxterm_bpost_9d = re.findall(r'duration.:.(.*?),', data_bpos0005)[92]
            TAEG_bpost_9d = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[92]
            minterm_bpost_9e = re.findall(r'duration.:.(.*?),', data_bpos0005)[93]
            maxterm_bpost_9e = re.findall(r'duration.:.(.*?),', data_bpos0005)[93]
            TAEG_bpost_9e = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[93]
            minterm_bpost_9f = re.findall(r'duration.:.(.*?),', data_bpos0005)[94]
            maxterm_bpost_9f = re.findall(r'duration.:.(.*?),', data_bpos0005)[95]
            TAEG_bpost_9f = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[94]
            minterm_bpost_9g = re.findall(r'duration.:.(.*?),', data_bpos0005)[96]
            maxterm_bpost_9g = re.findall(r'duration.:.(.*?),', data_bpos0005)[98]
            TAEG_bpost_9g = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[96]

            min_bpost_10 = re.findall(r'amountMin.:.(.*?),', data_bpos0005)[9]
            max_bpost_10 = re.findall(r'amountMax.:.(.*?),', data_bpos0005)[9]
            minterm_bpost_10 = re.findall(r'duration.:.(.*?),', data_bpos0005)[99]
            maxterm_bpost_10 = re.findall(r'duration.:.(.*?),', data_bpos0005)[100]
            TAEG_bpost_10 = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[99]

            minterm_bpost_10b = re.findall(r'duration.:.(.*?),', data_bpos0005)[101]
            maxterm_bpost_10b = re.findall(r'duration.:.(.*?),', data_bpos0005)[101]
            TAEG_bpost_10b = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[101]

            minterm_bpost_10c = re.findall(r'duration.:.(.*?),', data_bpos0005)[102]
            maxterm_bpost_10c = re.findall(r'duration.:.(.*?),', data_bpos0005)[102]
            TAEG_bpost_10c = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[102]

            minterm_bpost_10d = re.findall(r'duration.:.(.*?),', data_bpos0005)[103]
            maxterm_bpost_10d = re.findall(r'duration.:.(.*?),', data_bpos0005)[103]
            TAEG_bpost_10d = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[103]

            minterm_bpost_10e = re.findall(r'duration.:.(.*?),', data_bpos0005)[104]
            maxterm_bpost_10e = re.findall(r'duration.:.(.*?),', data_bpos0005)[104]
            TAEG_bpost_10e = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[104]

            minterm_bpost_10f = re.findall(r'duration.:.(.*?),', data_bpos0005)[105]
            maxterm_bpost_10f = re.findall(r'duration.:.(.*?),', data_bpos0005)[106]
            TAEG_bpost_10f = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[105]

            minterm_bpost_10g = re.findall(r'duration.:.(.*?),', data_bpos0005)[107]
            maxterm_bpost_10g = re.findall(r'duration.:.(.*?),', data_bpos0005)[109]
            TAEG_bpost_10g = re.findall(r'rate.:.(.*?)\n', data_bpos0005)[107]

            ####### concat everything
            min_bpos0005 = min_bpos0005_1, min_bpos0005_2, min_bpos0005_3, min_bpos0005_3, min_bpos0005_4, min_bpos0005_4, min_bpos0005_5, min_bpos0005_5, min_bpos0005_5, min_bpos0005_6, min_bpos0005_6, min_bpos0005_6, min_bpos0005_6, min_bpos0005_7, min_bpos0005_7, min_bpos0005_7, min_bpos0005_7, min_bpos0005_7, min_bpos0005_8, min_bpos0005_8, min_bpos0005_8, min_bpos0005_8, min_bpos0005_8, min_bpos0005_8, min_bpost_9, min_bpost_9, min_bpost_9, min_bpost_9, min_bpost_9, min_bpost_9, min_bpost_9, min_bpost_10, min_bpost_10, min_bpost_10, min_bpost_10, min_bpost_10, min_bpost_10, min_bpost_10
            max_bpos0005 = max_bpos0005_1, max_bpos0005_2, max_bpos0005_3, max_bpos0005_3, max_bpos0005_4, max_bpos0005_4, max_bpos0005_5, max_bpos0005_5, max_bpos0005_5, max_bpos0005_6, max_bpos0005_6, max_bpos0005_6, max_bpos0005_6, max_bpos0005_7, max_bpos0005_7, max_bpos0005_7, max_bpos0005_7, max_bpos0005_7, max_bpos0005_8, max_bpos0005_8, max_bpos0005_8, max_bpos0005_8, max_bpos0005_8, max_bpos0005_8, max_bpost_9, max_bpost_9, max_bpost_9, max_bpost_9, max_bpost_9, max_bpost_9, max_bpost_9, max_bpost_10, max_bpost_10, max_bpost_10, max_bpost_10, max_bpost_10, max_bpost_10, max_bpost_10
            minterm_bpos0005 = minterm_bpos0005_1, minterm_bpos0005_2, minterm_bpos0005_3, minterm_bpos0005_3b, minterm_bpos0005_4, minterm_bpos0005_4b, minterm_bpos0005_5, minterm_bpos0005_5b, minterm_bpos0005_5c, minterm_bpos0005_6, minterm_bpos0005_6b, minterm_bpos0005_6c, minterm_bpos0005_6d, minterm_bpos0005_7b, minterm_bpos0005_7c, minterm_bpos0005_7d, minterm_bpos0005_7e, minterm_bpos0005_7f, minterm_bpos0005_8, minterm_bpos0005_8b, minterm_bpos0005_8c, minterm_bpos0005_8d, minterm_bpos0005_8e, minterm_bpos0005_8f, minterm_bpost_9, minterm_bpost_9b, minterm_bpost_9c, minterm_bpost_9d, minterm_bpost_9e, minterm_bpost_9f, minterm_bpost_9g, minterm_bpost_10, minterm_bpost_10b, minterm_bpost_10c, minterm_bpost_10d, minterm_bpost_10e, minterm_bpost_10f, minterm_bpost_10g
            maxterm_bpos0005 = maxterm_bpos0005_1, maxterm_bpos0005_2, maxterm_bpos0005_3, maxterm_bpos0005_3b, maxterm_bpos0005_4, maxterm_bpos0005_4b, maxterm_bpos0005_5, maxterm_bpos0005_5b, maxterm_bpos0005_5c, maxterm_bpos0005_6, maxterm_bpos0005_6b, maxterm_bpos0005_6c, maxterm_bpos0005_6d, maxterm_bpos0005_7b, maxterm_bpos0005_7c, maxterm_bpos0005_7d, maxterm_bpos0005_7e, maxterm_bpos0005_7f, maxterm_bpos0005_8, maxterm_bpos0005_8b, maxterm_bpos0005_8c, maxterm_bpos0005_8d, maxterm_bpos0005_8e, maxterm_bpos0005_8f, maxterm_bpost_9, maxterm_bpost_9b, maxterm_bpost_9c, maxterm_bpost_9d, maxterm_bpost_9e, maxterm_bpost_9f, maxterm_bpost_9g, maxterm_bpost_10, maxterm_bpost_10b, maxterm_bpost_10c, maxterm_bpost_10d, maxterm_bpost_10e, maxterm_bpost_10f, maxterm_bpost_10g
            TAEG_bpos0005 = TAEG_bpos0005_1, TAEG_bpos0005_2, TAEG_bpos0005_3, TAEG_bpos0005_3b, TAEG_bpos0005_4, TAEG_bpos0005_4b, TAEG_bpos0005_5, TAEG_bpos0005_5b, TAEG_bpos0005_5c, TAEG_bpos0005_6, TAEG_bpos0005_6b, TAEG_bpos0005_6c, TAEG_bpos0005_6d, TAEG_bpos0005_7b, TAEG_bpos0005_7c, TAEG_bpos0005_7d, TAEG_bpos0005_7e, TAEG_bpos0005_7f, TAEG_bpos0005_8, TAEG_bpos0005_8b, TAEG_bpos0005_8c, TAEG_bpos0005_8d, TAEG_bpos0005_8e, TAEG_bpos0005_8f, TAEG_bpost_9, TAEG_bpost_9b, TAEG_bpost_9c, TAEG_bpost_9d, TAEG_bpost_9e, TAEG_bpost_9f, maxterm_bpost_9g, TAEG_bpost_10, TAEG_bpost_10b, TAEG_bpost_10c, TAEG_bpost_10d, TAEG_bpost_10e, TAEG_bpost_10f, TAEG_bpost_10g

        bpos0005_array = np.column_stack((min_bpos0005, max_bpos0005, minterm_bpos0005, maxterm_bpos0005, TAEG_bpos0005))
        bpos0005_tup = tuple(map(tuple, bpos0005_array))

        ########convert everything into a panda df##########

        Min_bpos0005 = pd.DataFrame(min_bpos0005, columns=['Min'])
        Max_bpos0005 = pd.DataFrame(max_bpos0005, columns=['Max'])
        amount_bpos0005 = Min_bpos0005.join(Max_bpos0005)

        MinTerm_bpos0005 = pd.DataFrame(minterm_bpos0005, columns=['Min Term'])
        MaxTerm_bpos0005 = pd.DataFrame(maxterm_bpos0005, columns=['Max Term'])
        duration_bpos0005 = MinTerm_bpos0005.join(MaxTerm_bpos0005)

        Taux_bpos0005 = pd.DataFrame(TAEG_bpos0005, columns=['Taux'])

        df_bpos0005 = amount_bpos0005.join(duration_bpos0005)
        df_bpos0005 = df_bpos0005.join(Taux_bpos0005)

        df_bpos0005.insert(0, 'Provider', 'BPost')
        df_bpos0005.insert(1, 'Product_ID', 'BPOS0005')
        df_bpos0005.insert(1, 'Category', 'Personal Loan')

        df_bpos0005_pl = df_bpos0005[['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']]  # Change order of columns

        bpost_loans_c = pd.concat([pd.concat([df_bpos0001_vl], axis=1),
                                     pd.concat([df_bpos0002_vl], axis=1),
                                     pd.concat([df_bpos0003_el], axis=1),
                                     pd.concat([df_bpos0004_rl], axis=1),
                                     pd.concat([df_bpos0005_pl], axis=1)])
        print(tabulate(bpost_loans_c, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass


def bpost_save_loans():
    bpost_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    bpost_loans_c.to_csv(os.path.join(path, file_name), index=False)

# # | |                                   # #
# # | | _  _   _ _   _ _ _ _  ____ _   _  # #
# # | || \| | | | | | | | | |/ _  | | | | # #
# # | |_) ) |_| | |_| | | | ( ( | | |_| | # #
# # |____/ \____|\__  |\____|\_||_|\__  | # #
# #             (____/            (____/  # #

def buyway_loans():
    try:
        global df_buyw0001_loans
        url_buyw0001 = 'https://www.buyway.be/pret-personnel.php'
        page_buyw0001 = requests.get(url_buyw0001).content
        soup_buyw0001 = BeautifulSoup(page_buyw0001, "html.parser")
        pattern_buyw0001 = re.compile(r"var rates = .")
        script_buyw0001 = soup_buyw0001.find("script", text=pattern_buyw0001)
        script_buyw0001 = str(script_buyw0001)

        for item in script_buyw0001:
            bank_buyw0001_loans = ['BuyWay'] * 6
            product_id_buyw0001_loans = ['BUYW0001'] * 6
            category_buyw0001_loans = ['Personal Loan'] * 6
            min_buyw0001 = re.findall(r'{minAmount:"(.*?)", maxAmount:', script_buyw0001)
            max_buyw0001 = re.findall(r'maxAmount:"(.*?)", minTerms', script_buyw0001)
            minterm_buyw0001 = re.findall(r'minTerms : "(.*?)", maxTerms', script_buyw0001)
            maxterm_buyw0001 = re.findall(r'maxTerms : "(.*?)", taeg', script_buyw0001)
            TAEG_buyw0001 = re.findall(r'taeg : "(.*?)", teg', script_buyw0001)

        all_buyw0001 = bank_buyw0001_loans, product_id_buyw0001_loans, category_buyw0001_loans, min_buyw0001, max_buyw0001, minterm_buyw0001, maxterm_buyw0001, TAEG_buyw0001
        buyw0001_array = np.column_stack((bank_buyw0001_loans, product_id_buyw0001_loans, category_buyw0001_loans, min_buyw0001, max_buyw0001, minterm_buyw0001, maxterm_buyw0001, TAEG_buyw0001))
        df_buyw0001_loans = pd.DataFrame(list(buyw0001_array))

        df_buyw0001_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        print(tabulate(df_buyw0001_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def buyway_save_loans():
    buyway_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_buyw0001_loans.to_csv(os.path.join(path, file_name), index=False)


# #  _______ _                  _      # #
# # (_______) |            _   (_)     # #
# #  _____  | | ____ ____ | |_  _  ___ # #
# # |  ___) | |/ _  |  _ \|  _)| |/___)# #
# # | |_____| ( ( | | | | | |__| |___ |# #
# # |_______)_|\_||_|_| |_|\___)_(___/ # #


def elantis_loans():
    try:
        global df_elan0001_loans
        page_elan0001 = requests.get('https://www.elantis.be/fr/simulateur-pret-a-temperament/?objective=personal&personal-amount=5.000')
        tree_elan0001 = html.fromstring(page_elan0001.content)
        buyers_elan0001 = tree_elan0001.xpath('//*[@id="barba-wrapper"]/div/script/text()')  # This will create a list of buyers
        data_elan0001 = '{\\"'.join(buyers_elan0001)
        PL_elan0001 = re.findall(r'\\"personal\\":(.*?)}]}],\\"min', data_elan0001)
        PL_elan0001 = '{\\"'.join(PL_elan0001)

        for item in PL_elan0001:
            bank_elan0001_loans = ['Elantis'] * 8
            productid_elan0001_loans = ['ELAN0001'] * 8
            category_elan0001_loans = ['Personal Loan'] * 8

            min_elan0001_1 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[0]
            max_elan0001_1 = re.findall(r'max\\":(.*?),', PL_elan0001)[0]
            minterm_elan0001_1 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[0]
            maxterm_elan0001_1 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[1]
            taeg_elan0001_1 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[0]

            min_elan0001_2 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[1]
            max_elan0001_2 = re.findall(r'max\\":(.*?),', PL_elan0001)[1]
            minterm_elan0001_2 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[1]
            minterm_elan0001_2 = int(minterm_elan0001_2) + 1
            maxterm_elan0001_2 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[2]
            taeg_elan0001_2 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[1]

            min_elan0001_3 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[2]
            max_elan0001_3 = re.findall(r'max\\":(.*?),', PL_elan0001)[2]
            minterm_elan0001_3 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[3]
            maxterm_elan0001_3 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[3]
            taeg_elan0001_3 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[3]

            min_elan0001_4 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[3]
            max_elan0001_4 = re.findall(r'max\\":(.*?),', PL_elan0001)[3]
            minterm_elan0001_4 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[4]
            maxterm_elan0001_4 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[5]
            taeg_elan0001_4 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[4]

            min_elan0001_5 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[4]
            max_elan0001_5 = re.findall(r'max\\":(.*?),', PL_elan0001)[4]
            minterm_elan0001_5 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[6]
            maxterm_elan0001_5 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[6]
            taeg_elan0001_5 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[5]

            min_elan0001_6 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[5]
            max_elan0001_6 = re.findall(r'max\\":(.*?),', PL_elan0001)[5]
            minterm_elan0001_6 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[7]
            maxterm_elan0001_6 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[10]
            taeg_elan0001_6 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[9]

            min_elan0001_7 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[6]
            max_elan0001_7 = re.findall(r'max\\":(.*?),', PL_elan0001)[6]
            minterm_elan0001_7 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[11]
            maxterm_elan0001_7 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[12]
            taeg_elan0001_7 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[10]

            min_elan0001_8 = re.findall(r'min\\":(.*?),\\"max', PL_elan0001)[7]
            max_elan0001_8 = re.findall(r'max\\":(.*?),', PL_elan0001)[7]
            minterm_elan0001_8 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[13]
            maxterm_elan0001_8 = re.findall(r'duration\\":(.*?),\\"taeg', PL_elan0001)[14]
            taeg_elan0001_8 = re.findall(r'\\"taeg\\":(.*?)}', PL_elan0001)[13]

            ####### concat everything
            min_elan0001 = min_elan0001_1, min_elan0001_2, min_elan0001_3, min_elan0001_4, min_elan0001_5, min_elan0001_6, min_elan0001_7, min_elan0001_8
            max_elan0001 = max_elan0001_1, max_elan0001_2, max_elan0001_3, max_elan0001_4, max_elan0001_5, max_elan0001_6, max_elan0001_7, max_elan0001_8
            minterm_elan0001 = minterm_elan0001_1, minterm_elan0001_2, minterm_elan0001_3, minterm_elan0001_4, minterm_elan0001_5, minterm_elan0001_6, minterm_elan0001_7, minterm_elan0001_8
            maxterm_elan0001 = maxterm_elan0001_1, maxterm_elan0001_2, maxterm_elan0001_3, maxterm_elan0001_4, maxterm_elan0001_5, maxterm_elan0001_6, maxterm_elan0001_7, maxterm_elan0001_8
            TAEG_elan0001 = taeg_elan0001_1, taeg_elan0001_2, taeg_elan0001_3, taeg_elan0001_4, taeg_elan0001_5, taeg_elan0001_6, taeg_elan0001_7, taeg_elan0001_8

        elan0001_array = np.column_stack((bank_elan0001_loans, productid_elan0001_loans, category_elan0001_loans, min_elan0001, max_elan0001, minterm_elan0001, maxterm_elan0001, TAEG_elan0001))
        df_elan0001_loans = pd.DataFrame(list(elan0001_array))
        df_elan0001_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        print(tabulate(df_elan0001_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def elantis_save_loans():
    elantis_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_elan0001_loans.to_csv(os.path.join(path, file_name), index=False)


# # _______                             _                 _      # #
# # (_______)                           | |               | |    # #
# #  _____  _   _  ____ ___  ____   ____| | _   ____ ____ | |  _ # #
# # |  ___)| | | |/ ___) _ \|  _ \ / _  | || \ / _  |  _ \| | / )# #
# # | |____| |_| | |  | |_| | | | ( ( | | |_) | ( | | | | | |< ( # #
# # |_______)____|_|   \___/| ||_/ \_||_|____/ \_||_|_| |_|_| \_)# #
# #                         |_|                                  # #
def europabank_loans():
    try:
        global df_euro0001_loans
        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=2500") as response:
            url_euro0001_1 = response.read()
            data_euro0001_1 = json.loads(url_euro0001_1)
            # print(json.dumps(data_europabank, indent=1))
            for item in data_euro0001_1:
                bank_euro0001_1 = 'Europabank'
                productid_euro0001 = 'EURO0001'
                category_euro0001 = 'Personal Loan'
                min_euro0001_1 = item['amount']
                max_euro0001_1 = min_euro0001_1
                minterm_euro0001_1 = item["looptijd"][0]["maanden"]
                maxterm_euro0001_1 = item["looptijd"][1]["maanden"]
                TAEG_euro0001_1 = item["looptijd"][0]["jkp"]
                all_euro0001_1 = bank_euro0001_1, productid_euro0001, category_euro0001, min_euro0001_1, max_euro0001_1, minterm_euro0001_1, maxterm_euro0001_1, TAEG_euro0001_1

        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=3700") as response:
            url_euro0001_2 = response.read()
            data_euro0001_2 = json.loads(url_euro0001_2)
            # print(json.dumps(data_europabank, indent=1))
            for item in data_euro0001_2:
                bank_euro0001_2 = 'Europabank'
                productid_euro0002 = 'EURO0001'
                category_euro0002 = 'Personal Loan'
                min_euro0001_2 = item['amount']
                max_euro0001_2 = min_euro0001_2
                max_euro0001_2 = min_euro0001_2
                minterm_euro0001_2 = item["looptijd"][1]["maanden"]
                maxterm_euro0001_2 = item["looptijd"][2]["maanden"]
                TAEG_euro0001_2 = item["looptijd"][0]["jkp"]
                all_euro0001_2 = bank_euro0001_2, productid_euro0002, category_euro0002, min_euro0001_2, max_euro0001_2, minterm_euro0001_2, maxterm_euro0001_2, TAEG_euro0001_2

        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=4999") as response:
            url_euro0001_3 = response.read()
            data_euro0001_3 = json.loads(url_euro0001_3)
            # print(json.dumps(data_europabank, indent=1))
            for item in data_euro0001_3:
                bank_euro0001_3 = 'Europabank'
                productid_euro0003 = 'EURO0001'
                category_euro0003 = 'Personal Loan'
                min_euro0001_3 = item['amount']
                max_euro0001_3 = min_euro0001_3
                minterm_euro0001_3 = item["looptijd"][0]["maanden"]
                maxterm_euro0001_3 = item["looptijd"][3]["maanden"]
                TAEG_euro0001_3 = item["looptijd"][0]["jkp"]
                all_euro0001_3 = bank_euro0001_3, productid_euro0003, category_euro0003, min_euro0001_3, max_euro0001_3, minterm_euro0001_3, maxterm_euro0001_3, TAEG_euro0001_3

        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=5000") as response:
            url_euro0001_4 = response.read()
            data_euro0001_4 = json.loads(url_euro0001_4)
            # print(json.dumps(data_europabank, indent=1))
            for item in data_euro0001_4:
                bank_euro0001_4 = 'Europabank'
                productid_euro0004 = 'EURO0001'
                category_euro0004 = 'Personal Loan'
                min_euro0001_4 = item['amount']
                max_euro0001_4 = min_euro0001_4
                minterm_euro0001_4 = item["looptijd"][0]["maanden"]
                maxterm_euro0001_4 = item["looptijd"][2]["maanden"]
                TAEG_euro0001_4 = item["looptijd"][0]["jkp"]
                all_euro0001_4 = bank_euro0001_4, productid_euro0004, category_euro0004, min_euro0001_4, max_euro0001_4, minterm_euro0001_4, maxterm_euro0001_4, TAEG_euro0001_4
            for item in data_euro0001_4:
                bank_euro0001_4_1 = 'Europabank'
                productid_euro0004 = 'EURO0001'
                category_euro0004 = 'Personal Loan'
                min_euro0001_4_1 = item['amount']
                max_euro0001_4_1 = min_euro0001_4_1
                minterm_euro0001_4_1 = item["looptijd"][3]["maanden"]
                maxterm_euro0001_4_1 = item["looptijd"][3]["maanden"]
                TAEG_euro0001_4_1 = item["looptijd"][3]["jkp"]
                all_euro0001_4_1 = bank_euro0001_4_1, productid_euro0004, category_euro0004, min_euro0001_4_1, max_euro0001_4_1, minterm_euro0001_4_1, maxterm_euro0001_4_1, TAEG_euro0001_4_1

        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=5600") as response:
            url_euro0001_5 = response.read()
            data_euro0001_5 = json.loads(url_euro0001_5)
            for item in data_euro0001_5:
                bank_euro0001_5 = 'Europabank'
                productid_euro0005 = 'EURO0001'
                category_euro0005 = 'Personal Loan'
                min_euro0001_5 = item['amount']
                max_euro0001_5 = min_euro0001_5
                minterm_euro0001_5 = item["looptijd"][0]["maanden"]
                maxterm_euro0001_5 = item["looptijd"][2]["maanden"]
                TAEG_euro0001_5 = item["looptijd"][0]["jkp"]
                all_euro0001_5 = bank_euro0001_5, productid_euro0005, category_euro0005, min_euro0001_5, max_euro0001_5, minterm_euro0001_5, maxterm_euro0001_5, TAEG_euro0001_5
            for item in data_euro0001_5:
                bank_euro0001_5_1 = 'Europabank'
                productid_euro0005 = 'EURO0001'
                category_euro0005 = 'Personal Loan'
                min_euro0001_5_1 = item['amount']
                max_euro0001_5_1 = min_euro0001_5_1
                minterm_euro0001_5_1 = item["looptijd"][3]["maanden"]
                maxterm_euro0001_5_1 = item["looptijd"][3]["maanden"]
                TAEG_euro0001_5_1 = item["looptijd"][3]["jkp"]
                all_euro0001_5_1 = bank_euro0001_5_1, productid_euro0005, category_euro0005, min_euro0001_5_1, max_euro0001_5_1, minterm_euro0001_5_1, maxterm_euro0001_5_1, TAEG_euro0001_5_1

        with urlopen("https://www.europabank.be/WebsiteAPI/rest/loan/amounts?type=PL&bedrag=7500") as response:
            url_euro0001_6 = response.read()
            data_euro0001_6 = json.loads(url_euro0001_6)
            # print(json.dumps(data_europabank, indent=1))
            for item in data_euro0001_6:
                bank_euro0001_6 = 'Europabank'
                productid_euro0006 = 'EURO0001'
                category_euro0006 = 'Personal Loan'
                min_euro0001_6 = item['amount']
                max_euro0001_6 = min_euro0001_6
                minterm_euro0001_6 = item["looptijd"][0]["maanden"]
                maxterm_euro0001_6 = item["looptijd"][2]["maanden"]
                TAEG_euro0001_6 = item["looptijd"][0]["jkp"]
                all_euro0001_6 = bank_euro0001_6, productid_euro0006, category_euro0006, min_euro0001_6, max_euro0001_6, minterm_euro0001_6, maxterm_euro0001_6, TAEG_euro0001_6
            for item in data_euro0001_6:
                bank_euro0001_6_1 = 'Europabank'
                productid_euro0006 = 'EURO0001'
                category_euro0006 = 'Personal Loan'
                min_euro0001_6_1 = item['amount']
                max_euro0001_6_1 = min_euro0001_6_1
                minterm_euro0001_6_1 = item["looptijd"][3]["maanden"]
                maxterm_euro0001_6_1 = item["looptijd"][4]["maanden"]
                TAEG_euro0001_6_1 = item["looptijd"][3]["jkp"]
                all_euro0001_6_1 = bank_euro0001_6_1, productid_euro0006, category_euro0006, min_euro0001_6_1, max_euro0001_6_1, minterm_euro0001_6_1, maxterm_euro0001_6_1, TAEG_euro0001_6_1

        concat_euro0001 = all_euro0001_1, all_euro0001_2, all_euro0001_3, all_euro0001_4, all_euro0001_4_1, all_euro0001_5, all_euro0001_5_1, all_euro0001_6, all_euro0001_6_1
        df_euro0001_loans = pd.DataFrame(list(concat_euro0001))
        df_euro0001_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']
        print(tabulate(df_euro0001_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def europabank_save_loans():
    europabank_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_euro0001_loans.to_csv(os.path.join(path, file_name), index=False)



# #  _                                        # #
# # | |                                       # #
# # | |      ____ ____ ____   ____ ____   ___ # #
# # | |     / _  ) _  )    \ / _  |  _ \ /___)# #
# # | |____( (/ ( (/ /| | | ( ( | | | | |___ |# #
# # |_______)____)____)_|_|_|\_||_|_| |_(___/ # #

def leemans_loans():
    try:
        global leemans_loans_c
        ###############################################################################################################
        ############################################LEEM0001###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=12&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=6") as response:
            source_leem0001 = response.read()
            url_leem0001 = json.loads(source_leem0001)
            url_leem0001 = json.dumps(url_leem0001, indent=1)
            for item in url_leem0001:
                min_leem0001 = re.findall(r'"from":.(.*?),', url_leem0001)
                max_leem0001 = re.findall(r'"till":.(.*?),', url_leem0001)
                minterm_leem0001 = re.findall(r'."min":.(.*?),', url_leem0001)[0:10]
                maxterm_leem0001 = re.findall(r'"max":.(.*?),', url_leem0001)[0:10]
                TAEG_leem0001 = re.findall(r'"12": "(.*?)",', url_leem0001)
        array_leem0001 = np.column_stack((min_leem0001, max_leem0001, minterm_leem0001, maxterm_leem0001, TAEG_leem0001))
        tup_leem0001 = tuple(map(tuple, array_leem0001))
        df_leem0001_loans = pd.DataFrame(list(tup_leem0001))
        df_leem0001_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0001_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0001_loans.insert(1, 'Product_ID', 'LEEM0001')
        df_leem0001_loans.insert(2, 'Category', 'Personal Loan')

        ###############################################################################################################
        ############################################LEEM0002###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=10&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=1") as response:
            source_leem0002 = response.read()
            url_leem0002 = json.loads(source_leem0002)
            url_leem0002 = json.dumps(url_leem0002, indent=1)
            for item in url_leem0002:
                min_leem0002 = re.findall(r'"from":.(.*?),', url_leem0002)
                max_leem0002 = re.findall(r'"till":.(.*?),', url_leem0002)
                minterm_leem0002 = re.findall(r'."min":.(.*?),', url_leem0002)[0:9]
                maxterm_leem0002 = re.findall(r'"max":.(.*?),', url_leem0002)[0:9]
                TAEG_leem0002 = re.findall(r'"12": "(.*?)",', url_leem0002)

        array_leem0002 = np.column_stack((min_leem0002, max_leem0002, minterm_leem0002, maxterm_leem0002, TAEG_leem0002))
        tup_leem0002 = tuple(map(tuple, array_leem0002))
        df_leem0002_loans = pd.DataFrame(list(tup_leem0002))
        df_leem0002_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0002_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0002_loans.insert(1, 'Product_ID', 'LEEM0002')
        df_leem0002_loans.insert(2, 'Category', 'Vehicle Loan')

        ###############################################################################################################
        ############################################LEEM0003###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=575&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=5") as response:
            source_leem0003 = response.read()
            url_leem0003 = json.loads(source_leem0003)
            url_leem0003 = json.dumps(url_leem0003, indent=1)
            for item in url_leem0003:
                min_leem0003 = re.findall(r'"from":.(.*?),', url_leem0003)
                max_leem0003 = re.findall(r'"till":.(.*?),', url_leem0003)
                minterm_leem0003 = re.findall(r'."min":.(.*?),', url_leem0003)[0:7]
                maxterm_leem0003 = re.findall(r'"max":.(.*?),', url_leem0003)[0:7]
                TAEG_leem0003 = re.findall(r'"12": "(.*?)",', url_leem0003)

        array_leem0003 = np.column_stack((min_leem0003, max_leem0003, minterm_leem0003, maxterm_leem0003, TAEG_leem0003))
        tup_leem0003 = tuple(map(tuple, array_leem0003))
        df_leem0003_loans = pd.DataFrame(list(tup_leem0003))
        df_leem0003_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0003_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0003_loans.insert(1, 'Product_ID', 'LEEM0003')
        df_leem0003_loans.insert(2, 'Category', 'Vehicle Loan')

        ###############################################################################################################
        ############################################LEEM0004###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=926&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=23") as response:
            source_leem0004 = response.read()
            url_leem0004 = json.loads(source_leem0004)
            url_leem0004 = json.dumps(url_leem0004, indent=1)
            for item in url_leem0004:
                min_leem0004 = re.findall(r'"from":.(.*?),', url_leem0004)
                max_leem0004 = re.findall(r'"till":.(.*?),', url_leem0004)
                minterm_leem0004 = re.findall(r'."min":.(.*?),', url_leem0004)[0:6]
                maxterm_leem0004 = re.findall(r'"max":.(.*?),', url_leem0004)[0:6]
                TAEG_leem0004 = re.findall(r'"36": "(.*?)",', url_leem0004)

        array_leem0004 = np.column_stack((min_leem0004, max_leem0004, minterm_leem0004, maxterm_leem0004, TAEG_leem0004))
        tup_leem0004 = tuple(map(tuple, array_leem0004))
        df_leem0004_loans = pd.DataFrame(list(tup_leem0004))
        df_leem0004_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0004_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0004_loans.insert(1, 'Product_ID', 'LEEM0004')
        df_leem0004_loans.insert(2, 'Category', 'Vehicle Loan')

        ###############################################################################################################
        ############################################LEEM0005###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=588&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=2") as response:
            source_leem0005 = response.read()
            url_leem0005 = json.loads(source_leem0005)
            url_leem0005 = json.dumps(url_leem0005, indent=1)
            for item in url_leem0005:
                min_leem0005 = re.findall(r'"from":.(.*?),', url_leem0005)
                max_leem0005 = re.findall(r'"till":.(.*?),', url_leem0005)
                minterm_leem0005 = re.findall(r'."min":.(.*?),', url_leem0005)[0:10]
                maxterm_leem0005 = re.findall(r'"max":.(.*?),', url_leem0005)[0:10]
                TAEG_leem0005 = re.findall(r'"12": "(.*?)",', url_leem0005)

        array_leem0005 = np.column_stack((min_leem0005, max_leem0005, minterm_leem0005, maxterm_leem0005, TAEG_leem0005))
        tup_leem0005 = tuple(map(tuple, array_leem0005))
        df_leem0005_loans = pd.DataFrame(list(tup_leem0005))
        df_leem0005_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0005_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0005_loans.insert(1, 'Product_ID', 'LEEM0005')
        df_leem0005_loans.insert(2, 'Category', 'Personal Loan')

        ###############################################################################################################
        ############################################LEEM0006###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=495&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=8") as response:
            source_leem0006 = response.read()
            url_leem0006 = json.loads(source_leem0006)
            url_leem0006 = json.dumps(url_leem0006, indent=1)
            for item in url_leem0006:
                min_leem0006 = re.findall(r'"from":.(.*?),', url_leem0006)
                max_leem0006 = re.findall(r'"till":.(.*?),', url_leem0006)
                minterm_leem0006 = re.findall(r'."min":.(.*?),', url_leem0006)[0:8]
                maxterm_leem0006 = re.findall(r'"max":.(.*?),', url_leem0006)[0:8]
                TAEG_leem0006 = re.findall(r'"12": "(.*?)",', url_leem0006)

        array_leem0006 = np.column_stack((min_leem0006, max_leem0006, minterm_leem0006, maxterm_leem0006, TAEG_leem0006))
        tup_leem0006 = tuple(map(tuple, array_leem0006))
        df_leem0006_loans = pd.DataFrame(list(tup_leem0006))
        df_leem0006_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0006_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0006_loans.insert(1, 'Product_ID', 'LEEM0006')
        df_leem0006_loans.insert(2, 'Category', 'Renovation Loan')

        ###############################################################################################################
        ############################################LEEM0007###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=525&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=22") as response:
            source_leem0007 = response.read()
            url_leem0007 = json.loads(source_leem0007)
            url_leem0007 = json.dumps(url_leem0007, indent=1)
            for item in url_leem0007:
                min_leem0007 = re.findall(r'"from":.(.*?),', url_leem0007)
                max_leem0007 = re.findall(r'"till":.(.*?),', url_leem0007)
                minterm_leem0007 = re.findall(r'."min":.(.*?),', url_leem0007)[0:8]
                maxterm_leem0007 = re.findall(r'"max":.(.*?),', url_leem0007)[0:8]
                TAEG_leem0007 = re.findall(r'"12": "(.*?)",', url_leem0007)

        array_leem0007 = np.column_stack((min_leem0007, max_leem0007, minterm_leem0007, maxterm_leem0007, TAEG_leem0007))
        tup_leem0007 = tuple(map(tuple, array_leem0007))
        df_leem0007_loans = pd.DataFrame(list(tup_leem0007))
        df_leem0007_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0007_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0007_loans.insert(1, 'Product_ID', 'LEEM0007')
        df_leem0007_loans.insert(2, 'Category', 'Energy Loan')

        ###############################################################################################################
        ############################################LEEM0008###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=494&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=9") as response:
            source_leem0008 = response.read()
            url_leem0008 = json.loads(source_leem0008)
            url_leem0008 = json.dumps(url_leem0008, indent=1)
            for item in url_leem0008:
                min_leem0008 = re.findall(r'"from":.(.*?),', url_leem0008)
                max_leem0008 = re.findall(r'"till":.(.*?),', url_leem0008)
                minterm_leem0008 = re.findall(r'."min":.(.*?),', url_leem0008)[0:9]
                maxterm_leem0008 = re.findall(r'"max":.(.*?),', url_leem0008)[0:9]
                TAEG_leem0008 = re.findall(r'"12": "(.*?)",', url_leem0008)

        array_leem0008 = np.column_stack((min_leem0008, max_leem0008, minterm_leem0008, maxterm_leem0008, TAEG_leem0008))
        tup_leem0008 = tuple(map(tuple, array_leem0008))
        df_leem0008_loans = pd.DataFrame(list(tup_leem0008))
        df_leem0008_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0008_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0008_loans.insert(1, 'Product_ID', 'LEEM0008')
        df_leem0008_loans.insert(2, 'Category', 'Personal Loan')

        ###############################################################################################################
        ############################################LEEM0009###########################################################
        with urlopen("http://www.leemanskredieten.be/index.php?id=526&type=666&tx_caltool_pi1[action]=kredietajax&tx_caltool_pi1[controller]=CalculationType&tx_caltool_pi1[kredietId]=7") as response:
            source_leem0009 = response.read()
            url_leem0009 = json.loads(source_leem0009)
            url_leem0009 = json.dumps(url_leem0009, indent=1)
            for item in url_leem0009:
                min_leem0009 = re.findall(r'"from":.(.*?),', url_leem0009)
                max_leem0009 = re.findall(r'"till":.(.*?),', url_leem0009)
                minterm_leem0009 = re.findall(r'."min":.(.*?),', url_leem0009)[0:10]
                maxterm_leem0009 = re.findall(r'"max":.(.*?),', url_leem0009)[0:10]
                TAEG_leem0009 = re.findall(r'"12": "(.*?)",', url_leem0009)

        array_leem0009 = np.column_stack((min_leem0009, max_leem0009, minterm_leem0009, maxterm_leem0009, TAEG_leem0009))
        tup_leem0009 = tuple(map(tuple, array_leem0009))
        df_leem0009_loans = pd.DataFrame(list(tup_leem0009))
        df_leem0009_loans.columns = ['Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        df_leem0009_loans.insert(0, 'Provider', 'Leemans Kredieten')
        df_leem0009_loans.insert(1, 'Product_ID', 'LEEM0009')
        df_leem0009_loans.insert(2, 'Category', 'Personal Loan')

        leemans_loans_c = pd.concat([pd.concat([df_leem0001_loans], axis=1),
                                     pd.concat([df_leem0002_loans], axis=1),
                                     pd.concat([df_leem0003_loans], axis=1),
                                     pd.concat([df_leem0004_loans], axis=1),
                                     pd.concat([df_leem0005_loans], axis=1),
                                     pd.concat([df_leem0006_loans], axis=1),
                                     pd.concat([df_leem0007_loans], axis=1),
                                     pd.concat([df_leem0008_loans], axis=1),
                                     pd.concat([df_leem0009_loans], axis=1),])
        print(tabulate(leemans_loans_c, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass

def leemans_save_loans():
    leemans_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    leemans_loans_c.to_csv(os.path.join(path, file_name), index=False)

# # ______                                     # #
# # |  ___ \                                   # #
# # | | _ | | ___ _____ _____ ____ ____   ___  # #
# # | || || |/ _ (___  |___  ) _  )  _ \ / _ \ # #
# # | || || | |_| / __/ / __( (/ /| | | | |_| |# #
# # |_||_||_|\___(_____|_____)____)_| |_|\___/ # #


def mozzeno_loans():
    try:
        global df_mozz0004_loans
        ###############################################################################################################
        ############################################LEEM0001###########################################################

        with urlopen("https://api.mozzeno.com/api/products/e30ac5c4-2ec3-11e9-8116-020ac2993ecb") as response:
            source_mozz0004_1 = response.read()
            data_mozz0004_1 = json.loads(source_mozz0004_1)
            data_mozz0004_1_pp = json.dumps(data_mozz0004_1, indent=1)
            for item in data_mozz0004_1_pp:
                bank_mozz0004 = ['Mozzeno']
                productid_mozz0004 = ['MOZZ0004']
                category_mozz0004 = ['Personal Loan']
                min_mozz0004_1 = re.findall(r'low_amount": (.*?),', data_mozz0004_1_pp)
                max_mozz0004_1 = re.findall(r'high_amount": (.*?),', data_mozz0004_1_pp)
                minterm_mozz0004_1 = re.findall(r'duration":.(.*?),', data_mozz0004_1_pp)
                maxterm_mozz0004_1 = re.findall(r'duration":.(.*?),', data_mozz0004_1_pp)
                TAEG_mozz0004_1 = re.findall(r'rate_apr":.(.*?),', data_mozz0004_1_pp)
            mozz0004_1 = bank_mozz0004 + productid_mozz0004 + category_mozz0004 + min_mozz0004_1 + max_mozz0004_1 + minterm_mozz0004_1 + maxterm_mozz0004_1 + TAEG_mozz0004_1

        with urlopen("https://api.mozzeno.com/api/products/e30ac629-2ec3-11e9-8116-020ac2993ecb") as response:
            source_mozz0004_2 = response.read()
            data_mozz0004_2 = json.loads(source_mozz0004_2)
            data_mozz0004_2_pp = json.dumps(data_mozz0004_2, indent=1)
            for item in data_mozz0004_2_pp:
                bank_mozz0004 = ['Mozzeno']
                productid_mozz0004 = ['MOZZ0004']
                category_mozz0004 = ['Personal Loan']
                min_mozz0004_2 = re.findall(r'low_amount": (.*?),', data_mozz0004_2_pp)
                max_mozz0004_2 = re.findall(r'high_amount": (.*?),', data_mozz0004_2_pp)
                minterm_mozz0004_2 = re.findall(r'duration":.(.*?),', data_mozz0004_2_pp)
                maxterm_mozz0004_2 = re.findall(r'duration":.(.*?),', data_mozz0004_2_pp)
                TAEG_mozz0004_2 = re.findall(r'rate_apr":.(.*?),', data_mozz0004_2_pp)
            mozz0004_2 = bank_mozz0004 + productid_mozz0004 + category_mozz0004 + min_mozz0004_2 + max_mozz0004_2 + minterm_mozz0004_2 + maxterm_mozz0004_2 + TAEG_mozz0004_2

        with urlopen("https://api.mozzeno.com/api/products/e30ac696-2ec3-11e9-8116-020ac2993ecb") as response:
            source_mozz0004_3 = response.read()
            data_mozz0004_3 = json.loads(source_mozz0004_3)
            data_mozz0004_3_pp = json.dumps(data_mozz0004_3, indent=1)
            for item in data_mozz0004_3_pp:
                bank_mozz0004 = ['Mozzeno']
                productid_mozz0004 = ['MOZZ0004']
                category_mozz0004 = ['Personal Loan']
                min_mozz0004_3 = re.findall(r'low_amount": (.*?),', data_mozz0004_3_pp)
                max_mozz0004_3 = re.findall(r'high_amount": (.*?),', data_mozz0004_3_pp)
                minterm_mozz0004_3 = re.findall(r'duration":.(.*?),', data_mozz0004_3_pp)
                maxterm_mozz0004_3 = re.findall(r'duration":.(.*?),', data_mozz0004_3_pp)
                TAEG_mozz0004_3 = re.findall(r'rate_apr":.(.*?),', data_mozz0004_3_pp)
            mozz0004_3 = bank_mozz0004 + productid_mozz0004 + category_mozz0004 + min_mozz0004_3 + max_mozz0004_3 + minterm_mozz0004_3 + maxterm_mozz0004_3 + TAEG_mozz0004_3

        with urlopen("https://api.mozzeno.com/api/products/e30ac6f7-2ec3-11e9-8116-020ac2993ecb") as response:
            source_mozz0004_4 = response.read()
            data_mozz0004_4 = json.loads(source_mozz0004_4)
            data_mozz0004_4_pp = json.dumps(data_mozz0004_4, indent=1)
            for item in data_mozz0004_4_pp:
                bank_mozz0004 = ['Mozzeno']
                productid_mozz0004 = ['MOZZ0004']
                category_mozz0004 = ['Personal Loan']
                min_mozz0004_4 = re.findall(r'low_amount": (.*?),', data_mozz0004_4_pp)
                max_mozz0004_4 = re.findall(r'high_amount": (.*?),', data_mozz0004_4_pp)
                minterm_mozz0004_4 = re.findall(r'duration":.(.*?),', data_mozz0004_4_pp)
                maxterm_mozz0004_4 = re.findall(r'duration":.(.*?),', data_mozz0004_4_pp)
                TAEG_mozz0004_4 = re.findall(r'rate_apr":.(.*?),', data_mozz0004_4_pp)
            mozz0004_4 = bank_mozz0004 + productid_mozz0004 + category_mozz0004 + min_mozz0004_4 + max_mozz0004_4 + minterm_mozz0004_4 + maxterm_mozz0004_4 + TAEG_mozz0004_4

        mozz0004_all = mozz0004_1, mozz0004_2, mozz0004_3, mozz0004_4

        mozz0004_array = np.asarray(mozz0004_all)  # convert to array
        df_mozz0004_loans = pd.DataFrame(list(mozz0004_array))  # convert list of array to df
        df_mozz0004_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        print(tabulate(df_mozz0004_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass


def mozzeno_save_loans():
    mozzeno_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_mozz0004_loans.to_csv(os.path.join(path, file_name), index=False)


# #     _                                    _             # #
# #    | |               _                  | |            # #
# #     \ \   ____ ____ | |_  ____ ____   _ | | ____  ____ # #
# #      \ \ / _  |  _ \|  _)/ _  |  _ \ / || |/ _  )/ ___)# #
# #  _____) | ( | | | | | |_( ( | | | | ( (_| ( (/ /| |    # #
# # (______/ \_||_|_| |_|\___)_||_|_| |_|\____|\____)_|    # #
def santander_loans():
    try:
        global df_sant0001_loans
        ###############################################################################################################
        ############################################SANT0001###########################################################
        url = "https://www.santander.be/Calculate/CalculateInstallment/"

        #############################################1ST RATE 2500-2500###############################################
        payload_1 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 2500,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_1 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_1 = requests.request("POST", url, data=payload_1, headers=headers_1)
        santander_1 = response_1.text

        for item in santander_1:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_1 = re.findall(r'"LoanAmount":(.*?),"', santander_1)[0]
            max_santander_1 = re.findall(r'"LoanAmount":(.*?),"', santander_1)[2]
            minterm_santander_1 = re.findall(r'term=(.*?)",', santander_1)[4]
            maxterm_santander_1 = re.findall(r'term=(.*?)",', santander_1)[0]
            TAEG_santander_1 = re.findall(r'"InterestRate":(.*?),', santander_1)[0]
        sant_1 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_1, max_santander_1, minterm_santander_1, maxterm_santander_1, TAEG_santander_1]

        #############################################2ND RATE 2500-3700###############################################

        payload_2 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 3700,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_2 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_2 = requests.request("POST", url, data=payload_2, headers=headers_2)
        santander_2 = response_2.text

        for item in santander_2:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_2 = float(max_santander_1) + 1
            max_santander_2 = re.findall(r'"LoanAmount":(.*?),"', santander_2)[2]
            minterm_santander_2 = re.findall(r'term=(.*?)",', santander_2)[4]
            minterm_santander_2 = int(minterm_santander_2)
            maxterm_santander_2 = re.findall(r'term=(.*?)",', santander_2)[0]
            TAEG_santander_2 = re.findall(r'"InterestRate":(.*?),', santander_2)[0]
        sant_2 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_2, max_santander_2, minterm_santander_2, maxterm_santander_2, TAEG_santander_2]

        #############################################3ND RATE 3701-5000###############################################

        payload_3 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 5000,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_3 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_3 = requests.request("POST", url, data=payload_3, headers=headers_3)
        santander_3 = response_3.text

        for item in santander_3:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_3 = float(max_santander_2) + 1
            max_santander_3 = re.findall(r'"LoanAmount":(.*?),"', santander_3)[2]
            minterm_santander_3 = re.findall(r'term=(.*?)",', santander_3)[4]
            minterm_santander_3 = int(minterm_santander_3) - 12  # This data and similar liner below are adjusted based on WebUI min
            maxterm_santander_3 = re.findall(r'term=(.*?)",', santander_3)[0]
            TAEG_santander_3 = re.findall(r'"InterestRate":(.*?),', santander_3)[0]
        sant_3 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_3, max_santander_3, minterm_santander_3, maxterm_santander_3, TAEG_santander_3]

        #############################################4TH RATE 5001-5600###############################################

        payload_4 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 5600,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_4 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_4 = requests.request("POST", url, data=payload_4, headers=headers_4)
        santander_4 = response_4.text

        for item in santander_4:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_4 = float(max_santander_2) + 1
            max_santander_4 = re.findall(r'"LoanAmount":(.*?),"', santander_4)[2]
            minterm_santander_4 = re.findall(r'term=(.*?)",', santander_4)[4]
            minterm_santander_4 = int(minterm_santander_4) - 12
            maxterm_santander_4 = re.findall(r'term=(.*?)",', santander_4)[0]
            TAEG_santander_4 = re.findall(r'"InterestRate":(.*?),', santander_4)[0]
        sant_4 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_4, max_santander_4, minterm_santander_4, maxterm_santander_4, TAEG_santander_4]

        #############################################5TH RATE 5601-7500###############################################

        payload_5 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 7500,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_5 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_5 = requests.request("POST", url, data=payload_5, headers=headers_5)
        santander_5 = response_5.text

        for item in santander_5:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_5 = float(max_santander_4) + 1
            max_santander_5 = re.findall(r'"LoanAmount":(.*?),"', santander_5)[2]
            minterm_santander_5 = re.findall(r'term=(.*?)",', santander_5)[4]
            minterm_santander_5 = int(minterm_santander_5) - 18
            maxterm_santander_5 = re.findall(r'term=(.*?)",', santander_5)[0]
            TAEG_santander_5 = re.findall(r'"InterestRate":(.*?),', santander_5)[0]
        sant_5 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_5, max_santander_5, minterm_santander_5, maxterm_santander_5, TAEG_santander_5]

        #############################################6TH RATE 7501-10000###############################################

        payload_6 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 10000,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_6 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_6 = requests.request("POST", url, data=payload_6, headers=headers_6)
        santander_6 = response_6.text

        for item in santander_6:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_6 = float(max_santander_5) + 1
            max_santander_6 = re.findall(r'"LoanAmount":(.*?),"', santander_6)[2]
            minterm_santander_6 = re.findall(r'term=(.*?)",', santander_6)[4]
            minterm_santander_6 = int(minterm_santander_6) - 24
            maxterm_santander_6 = re.findall(r'term=(.*?)",', santander_6)[0]
            TAEG_santander_6 = re.findall(r'"InterestRate":(.*?),', santander_6)[0]
        sant_6 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_6, max_santander_6, minterm_santander_6, maxterm_santander_6, TAEG_santander_6]

        #############################################7TH RATE 10001-14999###############################################

        payload_7 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 14999,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_7 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_7 = requests.request("POST", url, data=payload_7, headers=headers_7)
        santander_7 = response_7.text

        for item in santander_7:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_7 = float(max_santander_6) + 1
            max_santander_7 = re.findall(r'"LoanAmount":(.*?),"', santander_7)[2]
            minterm_santander_7 = re.findall(r'term=(.*?)",', santander_7)[4]
            minterm_santander_7 = int(minterm_santander_7) - 36
            maxterm_santander_7 = re.findall(r'term=(.*?)",', santander_7)[0]
            TAEG_santander_7 = re.findall(r'"InterestRate":(.*?),', santander_7)[0]
        sant_7 = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_7, max_santander_7, minterm_santander_7, maxterm_santander_7, TAEG_santander_7]

        #############################################8TH RATE 15000-15000###############################################
        #####Based on the value in WebUI, this rate span is missing 6.95% TAEG at months 12-30##########################

        payload_8 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 15000,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_8 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_8 = requests.request("POST", url, data=payload_8, headers=headers_8)
        santander_8 = response_8.text

        for item in santander_8:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_8a = float(max_santander_7) + 1
            max_santander_8a = re.findall(r'"LoanAmount":(.*?),"', santander_8)[2]
            minterm_santander_8a = re.findall(r'term=(.*?)",', santander_8)[4]
            minterm_santander_8a = int(minterm_santander_8a) + 1
            maxterm_santander_8a = re.findall(r'term=(.*?)",', santander_8)[0]
            TAEG_santander_8a = re.findall(r'"InterestRate":(.*?),', santander_8)[0]
        sant_8a = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_8a, max_santander_8a, minterm_santander_8a, maxterm_santander_8a, TAEG_santander_8a]

        for item in santander_8:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_8b = float(max_santander_7) + 1
            max_santander_8b = re.findall(r'"LoanAmount":(.*?),"', santander_8)[2]
            minterm_santander_8b = re.findall(r'term=(.*?)",', santander_8)[4]
            minterm_santander_8b = int(minterm_santander_8b) - 17
            maxterm_santander_8b = re.findall(r'term=(.*?)",', santander_8)[4]
            TAEG_santander_8b = re.findall(r'"InterestRate":(.*?),', santander_8)[2]
        sant_8b = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_8b, max_santander_8b, minterm_santander_8b, maxterm_santander_8b, TAEG_santander_8b]

        #############################################9TH RATE 15001-20000###############################################
        #####Based on the value in WebUI, this rate span is missing 7.95% TAEG at months 21-48##########################
        #####Based on the value in WebUI, this rate span is missing 6.95% TAEG at months 12-30##########################

        payload_9 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 20000,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_9 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_9 = requests.request("POST", url, data=payload_9, headers=headers_9)
        santander_9 = response_9.text

        for item in santander_9:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_9a = float(max_santander_8a) + 1
            max_santander_9a = re.findall(r'"LoanAmount":(.*?),"', santander_9)[2]
            minterm_santander_9a = re.findall(r'term=(.*?)",', santander_9)[4]
            minterm_santander_9a = int(minterm_santander_9a) - 23
            maxterm_santander_9a = int(minterm_santander_9a) + 11
            minterm_santander_9b = int(minterm_santander_9a) + 12
            maxterm_santander_9b = re.findall(r'term=(.*?)",', santander_9)[0]
            TAEG_santander_9a = re.findall(r'"InterestRate":(.*?),', santander_9)[0]
        sant_9a = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_9a, max_santander_9a, minterm_santander_9a, maxterm_santander_9a, TAEG_santander_9a]
        sant_9b = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_9a, max_santander_9a, minterm_santander_9b, maxterm_santander_9b, TAEG_santander_9a]

        #############################################10TH RATE 20001-50000###############################################
        #####Based on the value in WebUI, this rate span is missing 5.5% TAEG at months 12-30##########################
        #####Based on the value in WebUI, this rate span is missing 7.95% TAEG at months 31-48##########################

        payload_10 = "{\n\t\"CalculationType\": 1,\n\t\"ProductType\": 1,\n\t\"LoanAmount\": 50000,\n\t\"MonthAmount\": 250,\n\t\"SelectedOptionIndex\": null,\n\t\"UmbracoNodeId\": 1282\n}"
        headers_10 = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "8d87eebb-43a9-4f8f-870c-d883cf572849"
        }

        response_10 = requests.request("POST", url, data=payload_10, headers=headers_10)
        santander_10 = response_10.text

        for item in santander_10:
            bank_sant0001 = 'Santander'
            productid_sant0001 = 'SANT0001'
            category_sant0001 = 'Personal Loan'
            min_santander_10 = float(max_santander_9a) + 1
            max_santander_10 = re.findall(r'"LoanAmount":(.*?),"', santander_10)[0]

            minterm_santander_10b = re.findall(r'term=(.*?)",', santander_10)[4]
            minterm_santander_10b = int(minterm_santander_10b) - 59
            minterm_santander_10c = int(minterm_santander_10b) + 12
            minterm_santander_10d = re.findall(r'term=(.*?)",', santander_10)[4]
            minterm_santander_10d = int(minterm_santander_10d) - 23

            maxterm_santander_10d = re.findall(r'term=(.*?)",', santander_10)[0]
            maxterm_santander_10b = int(maxterm_santander_10d) - 60
            maxterm_santander_10c = int(maxterm_santander_10d) - 36

            TAEG_santander_10 = re.findall(r'"InterestRate":(.*?),', santander_10)[0]

        sant_10b = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_10, max_santander_10, minterm_santander_10b, maxterm_santander_10b, TAEG_santander_10]
        sant_10c = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_10, max_santander_10, minterm_santander_10c, maxterm_santander_10c, TAEG_santander_10]
        sant_10d = [bank_sant0001, productid_sant0001, category_sant0001, min_santander_10, max_santander_10, minterm_santander_10d, maxterm_santander_10d, TAEG_santander_10]

        sant_all = sant_1, sant_2, sant_3, sant_4, sant_5, sant_6, sant_7, sant_8a, sant_8b, sant_9a, sant_9b, sant_10b, sant_10c, sant_10d

        sant0001_array = np.asarray(sant_all)  # convert to array
        df_sant0001_loans = pd.DataFrame(list(sant0001_array))  # convert list of array to df
        df_sant0001_loans.columns = ['Provider', 'Product_ID', 'Category', 'Min', 'Max', 'Min Term', 'Max Term', 'Taux']

        print(tabulate(df_sant0001_loans, headers='keys', tablefmt='psql', showindex="never"))
    except:
        pass


def santander_save_loans():
    santander_loans()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    df_sant0001_loans.to_csv(os.path.join(path, file_name), index=False)

def all_loans():
    try:
        argenta_loans()
    except:
        pass
    try:
        auxifina_loans()
    except:
        pass
    try:
        axabank_loans()
    except:
        pass
    try:
        belfius_loans()
    except:
        pass
    try:
        beobank_loans()
    except:
        pass
    try:
        bpost_loans()
    except:
        pass
    try:
        buyway_loans()
    except:
        pass
    try:
        elantis_loans()
    except:
        pass
    try:
        europabank_loans()
    except:
        pass
    try:
        leemans_loans()
    except:
        pass
    try:
        mozzeno_loans()
    except:
        pass
    try:
        santander_loans()
    except:
        pass

    all_c_loans = pd.concat([
        pd.concat([arge_loans_c], axis=1),
        pd.concat([auxi_loans_c], axis=1),
        pd.concat([df_axab0005_loans], axis=1),
        pd.concat([belfius_loans_c], axis=1),
        pd.concat([df_beob0001_loans], axis=1),
        pd.concat([bpost_loans_c], axis=1),
        pd.concat([df_buyw0001_loans], axis=1),
        pd.concat([df_elan0001_loans], axis=1),
        pd.concat([df_euro0001_loans], axis=1),
        pd.concat([leemans_loans_c], axis=1),
        pd.concat([df_mozz0004_loans], axis=1),
        pd.concat([df_sant0001_loans], axis=1),
    ])

    print(tabulate(all_c_loans, headers='keys', tablefmt='psql', showindex="never"))

    path = os.path.abspath("History/")
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    all_c_loans.to_csv(os.path.join(path, file_name), index=False)


