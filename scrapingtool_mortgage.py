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


# #    __                                     # #
# #   /  \                         _          # #
# #  / /\ \ _____ ____  ____ ____ | |_  ____  # #
# # | /__\ |  ___) _  |/ _  )  _ \|  _)/ _  | # #
# # |  __  | |  ( ( | ( (/ /| | | | |_( ( | | # #
# # |_|  |_|_|   \_|| |\____)_| |_|\___)_||_| # #
# #             (_____|                       # #

def argenta():
    df_arge = read_pdf("https://www.argenta.be/content/dam/argenta/documents/emprunter/credit-logement/Feuille%20de%20tarifs%20Cr%C3%A9dits%20hypoth%C3%A9caires.pdf",
            encoding="ISO-8859-1", pages=2, area=[184.04, 340, 561.6, 366.48], stream= True, spreadsheet=True, pandas_options={"header": None})
    df_arge.columns=["Rates"]
    global arge_c
    try:
    
    # ARGE0001
        df_arge0001 = df_arge.drop(df_arge.index[5:43])
        df_arge0001.insert(0,'Formulas','1/1/1 CAP3')
        df_arge0001.insert(1,'Min',[0,11,14,16,19])
        df_arge0001.insert(2,'Max',[10,13,15,18,20])
        df_arge0001.insert(0, 'Provider', 'Argenta')
        df_arge0001.insert(1, 'Category', 'Home Loan')
        df_arge0001.insert(2, 'Product_ID', 'ARGE0001')
        df_arge0001["Rates"] = df_arge0001["Rates"].str.replace(",", ".").str.strip()
        df_arge0001["Rates"] = df_arge0001["Rates"].str.replace("%", "").str.strip()
        df_arge0001 = df_arge0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # ARGE0002
        df_arge0002 = df_arge.drop(df_arge.index[0:6]).drop(df_arge.index[11:43])
        df_arge0002.insert(0,'Formulas','3/3/3 CAP3')
        df_arge0002.insert(1,'Min',[3,11,14,16,19])
        df_arge0002.insert(2,'Max',[10,13,15,18,20])
        df_arge0002.insert(0, 'Provider', 'Argenta')
        df_arge0002.insert(1, 'Category', 'Home Loan')
        df_arge0002.insert(2, 'Product_ID', 'ARGE0002')
        df_arge0002["Rates"] = df_arge0002["Rates"].str.replace(",", ".").str.strip()
        df_arge0002["Rates"] = df_arge0002["Rates"].str.replace("%", "").str.strip()
        df_arge0002 = df_arge0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]
    
    # ARGE0003
        df_arge0003 = df_arge.drop(df_arge.index[0:12]).drop(df_arge.index[17:43])
        df_arge0003.insert(0,'Formulas','5/3/3 CAP3')
        df_arge0003.insert(1,'Min',[5,11,14,16,19])
        df_arge0003.insert(2,'Max',[10,13,15,18,20])
        df_arge0003.insert(0, 'Provider', 'Argenta')
        df_arge0003.insert(1, 'Category', 'Home Loan')
        df_arge0003.insert(2, 'Product_ID', 'ARGE0003')
        df_arge0003["Rates"] = df_arge0003["Rates"].str.replace(",", ".").str.strip()
        df_arge0003["Rates"] = df_arge0003["Rates"].str.replace("%", "").str.strip()
        df_arge0003 = df_arge0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # ARGE0004
        df_arge0004 = df_arge.drop(df_arge.index[0:18]).drop(df_arge.index[23:43])
        df_arge0004.insert(0,'Formulas','7/3/3 CAP3')
        df_arge0004.insert(1,'Min',[7,11,14,16,19])
        df_arge0004.insert(2,'Max',[10,13,15,18,20])
        df_arge0004.insert(0, 'Provider', 'Argenta')
        df_arge0004.insert(1, 'Category', 'Home Loan')
        df_arge0004.insert(2, 'Product_ID', 'ARGE0004')
        df_arge0004["Rates"] = df_arge0004["Rates"].str.replace(",", ".").str.strip()
        df_arge0004["Rates"] = df_arge0004["Rates"].str.replace("%", "").str.strip()
        df_arge0004 = df_arge0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # ARGE0005
        df_arge0005 = df_arge.drop(df_arge.index[0:24]).drop(df_arge.index[28:43])
        df_arge0005.insert(0,'Formulas','10/5/5 CAP3')
        df_arge0005.insert(1,'Min',[10,14,16,19])
        df_arge0005.insert(2,'Max',[13,15,18,20])
        df_arge0005.insert(0, 'Provider', 'Argenta')
        df_arge0005.insert(1, 'Category', 'Home Loan')
        df_arge0005.insert(2, 'Product_ID', 'ARGE0005')
        df_arge0005["Rates"] = df_arge0005["Rates"].str.replace(",", ".").str.strip()
        df_arge0005["Rates"] = df_arge0005["Rates"].str.replace("%", "").str.strip()
        df_arge0005 = df_arge0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # ARGE0006
        df_arge0006 = df_arge.drop(df_arge.index[0:29]).drop(df_arge.index[31:43])
        df_arge0006.insert(0,'Formulas','15/5/5 CAP5')
        df_arge0006.insert(1,'Min',[15,19])
        df_arge0006.insert(2,'Max',[18,20])
        df_arge0006.insert(0, 'Provider', 'Argenta')
        df_arge0006.insert(1, 'Category', 'Home Loan')
        df_arge0006.insert(2, 'Product_ID', 'ARGE0006')
        df_arge0006["Rates"] = df_arge0006["Rates"].str.replace(",", ".").str.strip()
        df_arge0006["Rates"] = df_arge0006["Rates"].str.replace("%", "").str.strip()
        df_arge0006 = df_arge0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # ARGE0007
        df_arge0007 = df_arge.drop(df_arge.index[0:32]).drop(df_arge.index[34:43])
        df_arge0007.insert(0,'Formulas','15/5/5 CAP5')
        df_arge0007.insert(1,'Min',[20,23])
        df_arge0007.insert(2,'Max',[22,25])
        df_arge0007.insert(0, 'Provider', 'Argenta')
        df_arge0007.insert(1, 'Category', 'Home Loan')
        df_arge0007.insert(2, 'Product_ID', 'ARGE0007')
        df_arge0007["Rates"] = df_arge0007["Rates"].str.replace(",", ".").str.strip()
        df_arge0007["Rates"] = df_arge0007["Rates"].str.replace("%", "").str.strip()
        df_arge0007 = df_arge0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # AGE0008
        df_arge0008 = df_arge.drop(df_arge.index[0:35])
        df_arge0008.insert(0,'Formulas','Fixed rate')
        df_arge0008.insert(1,'Min',[0,11,14,16,19,21,23,26])
        df_arge0008.insert(2,'Max',[10,13,15,18,20,22,25,30])
        df_arge0008.insert(0, 'Provider', 'Argenta')
        df_arge0008.insert(1, 'Category', 'Home Loan')
        df_arge0008.insert(2, 'Product_ID', 'ARGE0008')
        df_arge0008["Rates"] = df_arge0008["Rates"].str.replace(",", ".").str.strip()
        df_arge0008["Rates"] = df_arge0008["Rates"].str.replace("%", "").str.strip()
        df_arge0008 = df_arge0008[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # Concatenate
        global arge_c
        arge_c = pd.concat([
            pd.concat([df_arge0001], axis=1),
            pd.concat([df_arge0002], axis=1),
            pd.concat([df_arge0003], axis=1),
            pd.concat([df_arge0004], axis=1),
            pd.concat([df_arge0005], axis=1),
            pd.concat([df_arge0006], axis=1),
            pd.concat([df_arge0007], axis=1),
            pd.concat([df_arge0008], axis=1)])
        print(tabulate(arge_c, headers='keys', tablefmt='psql', showindex="never"))

    except:
        pass

def argenta_save():
    argenta()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    arge_c.to_csv(os.path.join(path, file_name), index=False)


# #  ______                                   _    _              ______                _       # #
# # (____  \                                 | |  | |            (____  \              | |      # #
# #  ____)  ) ____ ____   ____ _   _  ____   | |  | |___ ____     ____)  ) ____ ____ _ | | ____ # #
# # |  __  ( / _  |  _ \ / _  | | | |/ _  )   \ \/ / _  |  _ \   |  __  ( / ___) _  ) || |/ _  |# #
# # | |__)  | ( | | | | | | | | |_| ( (/ /     \  ( ( | | | | |  | |__)  ) |  ( (/ ( (_| ( ( | |# #
# # |______/ \_||_|_| |_|\_|| |\____|\____)     \/ \_||_|_| |_|  |______/|_|   \____)____|\_||_|# #
# #                         |_|                                                                 # #

def bvbr():

    try:

    # BVBR0001
        df_bvbr1 = read_pdf('https://www.banquevanbreda.be/media/2480/tariefregeling-jvb-fr-307.pdf', encoding='ISO-8859-1',
                pages=1, area=[156.83, 41.09, 229.28, 254.47], pandas_options={'header': None})
        df_bvbr0001 = df_bvbr1.drop(df_bvbr1.index[0])
        df_bvbr0001 = df_bvbr0001.drop(df_bvbr0001.columns[2:5], axis=1)
        df_bvbr0001.columns = ["Formulas", "Rates"]
        df_bvbr0001["Formulas"] = df_bvbr0001["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0001["Rates"] = df_bvbr0001["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0001["Rates"] = df_bvbr0001["Rates"].str.replace("%", "").str.strip()

        Min_bvbr0001 = pd.DataFrame({'Min': ['', '0', '2', '4', '6', '11', '16']})
        Max_bvbr0001 = pd.DataFrame({'Max': ['', '1', '3', '5', '10', '15', '20']})
        duration_bvbr0001 = Min_bvbr0001.join(Max_bvbr0001)
        df_bvbr0001.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0001.insert(0, 'Category', 'Home Loan')
        df_bvbr0001.insert(1, 'Product_ID', 'BVBR0001')
        df_bvbr0001 = df_bvbr0001.join(duration_bvbr0001)  # join newly made df with existed df
        df_bvbr0001 = df_bvbr0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0002
        df_bvbr2 = read_pdf('https://www.banquevanbreda.be/media/2480/tariefregeling-jvb-fr-307.pdf', encoding='ISO-8859-1',
                               pages=1, area=[234.04, 37.96, 286.35, 395.91], pandas_options={'header': None})

        df_bvbr0002 = df_bvbr2.drop(df_bvbr2.index[0]).drop(df_bvbr2.index[2:19])
        df_bvbr0002 = df_bvbr0002.drop(df_bvbr0002.columns[3:6], axis=1)
        df_bvbr0002.columns = ["__", "_", "Rates"]
        df_bvbr0002["Formulas"] = df_bvbr0002["__"].map(str) + df_bvbr0002["_"].map(str)  # to join Name and CAP column
        df_bvbr0002.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0002.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0002["Formulas"] = df_bvbr0002["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0002["Rates"] = df_bvbr0002["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0002["Rates"] = df_bvbr0002["Rates"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0002 = pd.DataFrame({'Min': [''] * 1 + ['']})
        Max_bvbr0002 = pd.DataFrame({'Max': [''] * 1 + ['']})
        duration_bvbr0002 = Min_bvbr0002.join(Max_bvbr0002)

        df_bvbr0002.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0002.insert(0, 'Category', 'Home Loan')
        df_bvbr0002.insert(1, 'Product_ID', 'BVBR0002')
        df_bvbr0002 = df_bvbr0002.join(duration_bvbr0002)  # join newly made df with existed df
        df_bvbr0002 = df_bvbr0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0003
        df_bvbr0003 = df_bvbr2.drop(df_bvbr2.index[0:4]).drop(df_bvbr2.index[5:19])
        df_bvbr0003 = df_bvbr0003.drop(df_bvbr0003.columns[3:6], axis=1)
        df_bvbr0003.columns = ["__", "_", "Rates"]
        df_bvbr0003["Formulas"] = df_bvbr0003["__"].map(str) + df_bvbr0003["_"].map(str)  # to join Name and CAP column
        df_bvbr0003.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0003.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0003["Formulas"] = df_bvbr0003["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0003["Rates"] = df_bvbr0003["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0003["Rates"] = df_bvbr0003["Rates"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0003 = pd.DataFrame({'Min': [''] * 4 + ['']})
        Max_bvbr0003 = pd.DataFrame({'Max': [''] * 4 + ['']})
        duration_bvbr0003 = Min_bvbr0003.join(Max_bvbr0003)

        df_bvbr0003.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0003.insert(0, 'Category', 'Home Loan')
        df_bvbr0003.insert(1, 'Product_ID', 'BVBR0003')
        df_bvbr0003 = df_bvbr0003.join(duration_bvbr0003)  # join newly made df with existed df
        df_bvbr0003 = df_bvbr0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0004

        df_bvbr0004 = df_bvbr2.drop(df_bvbr2.index[0:7]).drop(df_bvbr2.index[8:19])
        df_bvbr0004 = df_bvbr0004.drop(df_bvbr0004.columns[3:6], axis=1)
        df_bvbr0004.columns = ["__", "_", "Rates"]
        df_bvbr0004["Formulas"] = df_bvbr0004["__"].map(str) + df_bvbr0004["_"].map(str)  # to join Name and CAP column
        df_bvbr0004.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0004.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0004["Formulas"] = df_bvbr0004["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0004["Rates"] = df_bvbr0004["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0004["Rates"] = df_bvbr0004["Rates"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0004 = pd.DataFrame({'Min': [''] * 7 + ['']})
        Max_bvbr0004 = pd.DataFrame({'Max': [''] * 7 + ['']})
        duration_bvbr0004 = Min_bvbr0004.join(Max_bvbr0004)

        df_bvbr0004.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0004.insert(0, 'Category', 'Home Loan')
        df_bvbr0004.insert(1, 'Product_ID', 'BVBR0004')
        df_bvbr0004 = df_bvbr0004.join(duration_bvbr0004)  # join newly made df with existed df
        df_bvbr0004 = df_bvbr0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0005
        df_bvbr0005 = df_bvbr2.drop(df_bvbr2.index[0:10]).drop(df_bvbr2.index[11:19])
        df_bvbr0005 = df_bvbr0005.drop(df_bvbr0005.columns[3:6], axis=1)
        df_bvbr0005.columns = ["__", "_", "Rates"]
        df_bvbr0005["Formulas"] = df_bvbr0005["__"].map(str) + df_bvbr0005["_"].map(str)  # to join Name and CAP column
        df_bvbr0005.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0005.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0005["Formulas"] = df_bvbr0005["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0005["Rates"] = df_bvbr0005["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0005["Rates"] = df_bvbr0005["Rates"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0005 = pd.DataFrame({'Min': [''] * 10 + ['']})
        Max_bvbr0005 = pd.DataFrame({'Max': [''] * 10 + ['']})
        duration_bvbr0005 = Min_bvbr0005.join(Max_bvbr0005)

        df_bvbr0005.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0005.insert(0, 'Category', 'Home Loan')
        df_bvbr0005.insert(1, 'Product_ID', 'BVBR0005')
        df_bvbr0005 = df_bvbr0005.join(duration_bvbr0005)  # join newly made df with existed df
        df_bvbr0005 = df_bvbr0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0006
        df_bvbr0006 = df_bvbr2.drop(df_bvbr2.index[0:13]).drop(df_bvbr2.index[14:19])
        df_bvbr0006 = df_bvbr0006.drop(df_bvbr0006.columns[3:6], axis=1)
        df_bvbr0006.columns = ["__", "_", "Rates"]
        df_bvbr0006["Formulas"] = df_bvbr0006["__"].map(str) + df_bvbr0006["_"].map(str)  # to join Name and CAP column
        df_bvbr0006.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0006.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0006["Formulas"] = df_bvbr0006["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0006["Rates"] = df_bvbr0006["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0006["Rates"] = df_bvbr0006["Rates"].str.replace("%", "").str.strip()

        # ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0006 = pd.DataFrame({'Min': [''] * 13 + ['']})
        Max_bvbr0006 = pd.DataFrame({'Max': [''] * 13 + ['']})
        duration_bvbr0006 = Min_bvbr0006.join(Max_bvbr0006)

        df_bvbr0006.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0006.insert(0, 'Category', 'Home Loan')
        df_bvbr0006.insert(1, 'Product_ID', 'BVBR0006')
        df_bvbr0006 = df_bvbr0006.join(duration_bvbr0006)  # join newly made df with existed df
        df_bvbr0006 = df_bvbr0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BVBR0007
        df_bvbr0007 = df_bvbr2.drop(df_bvbr2.index[0:16]).drop(df_bvbr2.index[17:19])
        df_bvbr0007 = df_bvbr0007.drop(df_bvbr0007.columns[3:6], axis=1)
        df_bvbr0007.columns = ["__", "_", "Rates"]
        df_bvbr0007["Formulas"] = df_bvbr0007["__"].map(str) + df_bvbr0007["_"].map(str)  # to join Name and CAP column
        df_bvbr0007.drop('__', axis=1, inplace=True)  # To delete the column by name without having to reassign df
        df_bvbr0007.drop('_', axis=1, inplace=True)

        # ##Naming purpose
        df_bvbr0007["Formulas"] = df_bvbr0007["Formulas"].str.replace("Ã©", "e").str.strip()
        df_bvbr0007["Rates"] = df_bvbr0007["Rates"].str.replace(",", ".").str.strip()
        df_bvbr0007["Rates"] = df_bvbr0007["Rates"].str.replace("%", "").str.strip()

        ##Assigning duration: this case doesn't have any duration indicated
        Min_bvbr0007 = pd.DataFrame({'Min': [''] * 16 + ['']})
        Max_bvbr0007 = pd.DataFrame({'Max': [''] * 16 + ['']})
        duration_bvbr0007 = Min_bvbr0007.join(Max_bvbr0007)

        df_bvbr0007.insert(0, 'Provider', 'Bank Van Breda')
        df_bvbr0007.insert(0, 'Category', 'Home Loan')
        df_bvbr0007.insert(1, 'Product_ID', 'BVBR0007')
        df_bvbr0007 = df_bvbr0007.join(duration_bvbr0007)  # join newly made df with existed df
        df_bvbr0007 = df_bvbr0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global bvbr_c
        bvbr_c = pd.concat([
            pd.concat([df_bvbr0001], axis=1),
            pd.concat([df_bvbr0002], axis=1),
            pd.concat([df_bvbr0003], axis=1),
            pd.concat([df_bvbr0004], axis=1),
            pd.concat([df_bvbr0005], axis=1),
            pd.concat([df_bvbr0006], axis=1),
            pd.concat([df_bvbr0007], axis=1)])

        print(tabulate(bvbr_c, headers='keys', tablefmt='psql', showindex="never"))


    except:
        pass

def bvbr_save():
    bvbr()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    # Line below is used to concat the whole dfs and save it into a csv file
    bvbr_c.to_csv(os.path.join(path, file_name), index=False)

# #  ______  ______                # #
# # (____  \(_____ \          _    # #
# #  ____)  )_____) )__   ___| |_  # #
# # |  __  (|  ____/ _ \ /___)  _) # #
# # | |__)  ) |   | |_| |___ | |__ # #
# # |______/|_|    \___/(___/ \___)# #

def bpost():

    try:
        url_bpos0001 = 'https://www.bpostbanque.be/bpb/emprunter/credit-hypothecaire'
        page_bpos0001 = requests.get(url_bpos0001).content
        soup_bpos0001 = BeautifulSoup(page_bpos0001, "html.parser")
        pattern_bpos0001 = re.compile(r"xml version=.")
        script_bpos0001 = soup_bpos0001.find("script", text=pattern_bpos0001)
        print(script_bpos0001)
        HL_bpost = str(script_bpos0001)[174585:176860]
        print(HL_bpost)
        
    # BPOST0001
        for _ in script_bpos0001:
            formules_BPOS0001 = (re.findall(r'property label="(.*?)" name="tauxFixe"', HL_bpost)) * 6
            min_BPOS0001 = ['0', '11', '16', '19', '21', '26']
            max_BPOS0001 = ['10', '15', '18', '20', '25', '30']
            taux_BPOS0001_ = re.findall(r'<value type="string">.(.*?).<.value><.property><property label="Titre Rates annuel fixe"', HL_bpost)
            taux_BPOS0001 = [element for item in taux_BPOS0001_ for element in item.split(',')]
        BPOS0001_array = np.column_stack((min_BPOS0001, max_BPOS0001, taux_BPOS0001))
        BPOS0001_tup = tuple(map(tuple, BPOS0001_array))
        df_BPOS0001 = pd.DataFrame(list(BPOS0001_tup))
        df_BPOS0001.columns = ["Min", "Max", "Rates"]
        df_BPOS0001.insert(0, 'Provider', 'BPost')
        df_BPOS0001.insert(1, 'Product_ID', 'BPOS0001')
        df_BPOS0001.insert(2, 'Category', 'Home Loan')
        df_BPOS0001.insert(3, 'Formulas', formules_BPOS0001)

    # BPOS0002

        for _ in script_bpos0001:
            formules_BPOS0002 = (re.findall(r'nouvelle formule<.value><.property><property label="(.*?)" name="tauxVariable"', HL_bpost)) * 6
            min_BPOS0002 = ['0', '11', '16', '19', '21', '26']
            max_BPOS0002 = ['10', '15', '18', '20', '25', '30']
            taux_BPOS0002_ = re.findall(r'Rates annuel variable 5.5.5" name="tauxVariable" readonly="true" itemName="widget-simulator-morgage-custom-8840771" viewHint="text-input,admin,designModeOnly"><value type="string">(.*?)<.value>', HL_bpost) * 6
            taux_BPOS0002 = [element for item in taux_BPOS0002_ for element in item.split(',')]
        BPOS0002_array = np.column_stack((min_BPOS0002, max_BPOS0002, taux_BPOS0002))
        BPOS0002_tup = tuple(map(tuple, BPOS0002_array))
        df_BPOS0002 = pd.DataFrame(list(BPOS0002_tup))
        df_BPOS0002.columns = ["Min", "Max", "Rates"]
        df_BPOS0002.insert(0, 'Provider', 'BPost')
        df_BPOS0002.insert(1, 'Product_ID', 'BPOS0002')
        df_BPOS0002.insert(2, 'Category', 'Home Loan')
        df_BPOS0002.insert(3, 'Formulas', formules_BPOS0002)

    # BPOS0003

        for _ in script_bpos0001:
            formules_BPOS0003 = (re.findall(r'tauxVariable.*<.value><.property><property label="(.*?)" name="tauxVariable1" readonly="true"', HL_bpost)) * 6
            min_BPOS0003 = ['0', '11', '16', '19', '21', '26']
            max_BPOS0003 = ['10', '15', '18', '20', '25', '30']
            taux_BPOS0003_ = re.findall(r'Rates annuel variable 10.5.5 1" name="tauxVariable1" readonly="true" itemName="widget-simulator-morgage-custom-8840771" viewHint="text-input,admin,designModeOnly"><value type="string">(.*?)<.value', HL_bpost) * 6
            taux_BPOS0003 = [element for item in taux_BPOS0003_ for element in item.split(',')]

        BPOS0003_array = np.column_stack((min_BPOS0003, max_BPOS0003, taux_BPOS0003))
        BPOS0003_tup = tuple(map(tuple, BPOS0003_array))
        df_BPOS0003 = pd.DataFrame(list(BPOS0003_tup))
        df_BPOS0003.columns = ["Min", "Max", "Rates"]
        df_BPOS0003.insert(0, 'Provider', 'BPost')
        df_BPOS0003.insert(1, 'Product_ID', 'BPOS0003')
        df_BPOS0003.insert(2, 'Category', 'Home Loan')
        df_BPOS0003.insert(3, 'Formulas', formules_BPOS0003)

    # BPOS0004
        for _ in script_bpos0001:
            formules_BPOS0004 = (re.findall(r'tauxVariable.*<.value><.property><property label="(.*?)" name="tauxVariable2" readonly="true"', HL_bpost)) * 6
            min_BPOS0004 = ['0', '11', '16', '19', '21', '26']
            max_BPOS0004 = ['10', '15', '18', '20', '25', '30']
            taux_BPOS0004_ = re.findall(r'10.5.5 2" name="tauxVariable2" readonly="true" itemName="widget-simulator-morgage-custom-8840771" viewHint="text-input,admin,designModeOnly"><value type="string">(.*?)<.value', HL_bpost) * 6
            taux_BPOS0004 = [element for item in taux_BPOS0004_ for element in item.split(',')]

        BPOS0004_array = np.column_stack((min_BPOS0004, max_BPOS0004, taux_BPOS0004))
        BPOS0004_tup = tuple(map(tuple, BPOS0004_array))
        df_BPOS0004 = pd.DataFrame(list(BPOS0004_tup))
        df_BPOS0004.columns = ["Min", "Max", "Rates"]
        df_BPOS0004.insert(0, 'Provider', 'BPost')
        df_BPOS0004.insert(1, 'Product_ID', 'BPOS0004')
        df_BPOS0004.insert(2, 'Category', 'Home Loan')
        df_BPOS0004.insert(3, 'Formulas', formules_BPOS0004)

    # Concatenate
        global bpos_c
        bpos_c = pd.concat([
            pd.concat([df_BPOS0001], axis=1),
            pd.concat([df_BPOS0002], axis=1),
            pd.concat([df_BPOS0003], axis=1),
            pd.concat([df_BPOS0004], axis=1)])

        print(tabulate(bpos_c, headers='keys', tablefmt='psql', showindex="never"))

    except:
        pass

def bpost_save():
    bpost()
    path = os.path.abspath("History/") # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    bpos_c.to_csv(os.path.join(path, file_name), index=False)

# #  ______        _  _____              # #
# # (____  \      | |/ __(_)             # #
# #  ____)  ) ____| | |__ _ _   _  ___   # #
# # |  __  ( / _  ) |  __) | | | |/___)  # #
# # | |__)  | (/ /| | |  | | |_| |___ |  # #
# # |______/ \____)_|_|  |_|\____(___/   # #
# #                                      # #

def belfius():
    try:

    # BELF0001
        df_belf0001 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                               stream=True, area=[269.875, 12.75, 380.5, 961], pages=1, guess=False, pandas_options={'header': None})
        df_belf0001 = df_belf0001.drop(df_belf0001.index[[0, 1]])  # drop the first 2 lines
        df_belf0001.drop(df_belf0001.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0001.columns = ["Formulas", "Min", "Max", "Rates"]
        df_belf0001["Min"] = df_belf0001["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0001["Max"] = df_belf0001["Max"].str.replace(" mois", "").str.strip()
        df_belf0001["Rates"] = df_belf0001["Rates"].str.replace(",", ".").str.strip()
        df_belf0001["Rates"] = df_belf0001["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0001["Rates"] = ((df_belf0001["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%
        df_belf0001.insert(0, 'Provider', 'Belfius')
        df_belf0001.insert(1, 'Product_ID', 'BELF0001')
        df_belf0001.insert(2, 'Category', 'Home Loan')
        df_belf0001 = df_belf0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0002
        df_belf0002 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                   stream=True, spreadsheet=True, area=[555.46, 113.18, 666.39, 549.68], pages=1, guess=False, pandas_options={'header': None})

        df_belf0002 = df_belf0002.drop(df_belf0002.index[[0, 1, 2]])  # drop the first 2 lines --> USE THIS IF YOU WANNA DROP ONE BY ONE
        df_belf0002.drop(df_belf0002.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0002.drop(df_belf0002.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0002.columns = ["Formulas", "Min", "Max", "Rates"]
        df_belf0002["Min"] = df_belf0002["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0002["Max"] = df_belf0002["Max"].str.replace(" mois", "").str.strip()
        df_belf0002["Rates"] = df_belf0002["Rates"].str.replace(",", ".").str.strip()
        df_belf0002["Rates"] = df_belf0002["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0002["Rates"] = ((df_belf0002["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%
        df_belf0002.insert(0, 'Provider', 'Belfius')
        df_belf0002.insert(1, 'Product_ID', 'BELF0002')
        df_belf0002.insert(2, 'Category', 'Home Loan')
        df_belf0002 = df_belf0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0003
        df_belf0003 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                   stream=True, spreadsheet=True, area=[555.09, 113.52, 740.38, 656.1], pages=1, guess=False, pandas_options={'header': None})

        df_belf0003 = df_belf0003.drop(df_belf0003.index[0:6])  # drop top lines --> USE THIS IF YOU WANNA DROP RANGE
        df_belf0003.drop(df_belf0003.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0003.drop(df_belf0003.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0003.columns = ["Formulas", "Min", "Max", "Rates"]
        df_belf0003["Min"] = df_belf0003["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0003["Max"] = df_belf0003["Max"].str.replace(" mois", "").str.strip()
        df_belf0003["Rates"] = df_belf0003["Rates"].str.replace(",", ".").str.strip()
        df_belf0003["Rates"] = df_belf0003["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0003["Rates"] = ((df_belf0003["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%
        df_belf0003.insert(0, 'Provider', 'Belfius')
        df_belf0003.insert(1, 'Product_ID', 'BELF0003')
        df_belf0003.insert(2, 'Category', 'Home Loan')
        df_belf0003 = df_belf0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0004
        df_belf0004 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                stream=True, spreadsheet=True, area=[555.09, 113.52, 786.41, 724.65], pages=1, guess=False, pandas_options={'header': None})
        df_belf0004 = df_belf0004.drop(df_belf0004.index[0:10])  # drop top lines --> USE THIS IF YOU WANNA DROP RANGE
        df_belf0004.drop(df_belf0004.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0004.drop(df_belf0004.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0004.columns = ["Formulas", "Min", "Max", "Rates"]
        df_belf0004["Min"] = df_belf0004["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0004["Max"] = df_belf0004["Max"].str.replace(" mois", "").str.strip()
        df_belf0004["Rates"] = df_belf0004["Rates"].str.replace(",", ".").str.strip()
        df_belf0004["Rates"] = df_belf0004["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0004["Rates"] = ((df_belf0004["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%
        df_belf0004.insert(0, 'Provider', 'Belfius')
        df_belf0004.insert(1, 'Product_ID', 'BELF0004')
        df_belf0004.insert(2, 'Category', 'Home Loan')
        df_belf0004 = df_belf0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0005
        df_belf0005_1 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                 stream=True, spreadsheet=True, area=[555.09, 113.52, 886.41, 724.65], pages=1, guess=False, pandas_options={'header': None})
        df_belf0005_1 = df_belf0005_1.drop(df_belf0005_1.index[0:13])  # drop top lines --> USE THIS IF YOU WANNA DROP RANGE
        df_belf0005_1.drop(df_belf0005_1.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0005_1.columns = ["Formulas", "Min", "Max", "_TauxMens_", "Rates"]
        df_belf0005_1.drop(df_belf0005_1.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel

        df_belf0005_1["Min"] = df_belf0005_1["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0005_1["Max"] = df_belf0005_1["Max"].str.replace(" mois", "").str.strip()
        df_belf0005_1["Rates"] = df_belf0005_1["Rates"].str.replace(",", ".").str.strip()
        df_belf0005_1["Rates"] = df_belf0005_1["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0005_1["Rates"] = ((df_belf0005_1["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        # This below is for the table on the 2nd page

        df_belf0005_2 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                 pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0005_2 = df_belf0005_2.drop(df_belf0005_2.index[2:27])  # drop top lines --> USE THIS IF YOU WANNA DROP RANGE
        df_belf0005_2.drop(df_belf0005_2.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0005_2.drop(df_belf0005_2.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0005_2.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0005_2["Min"] = df_belf0005_2["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0005_2["Max"] = df_belf0005_2["Max"].str.replace(" mois", "").str.strip()
        df_belf0005_2["Rates"] = df_belf0005_2["Rates"].str.replace(",", ".").str.strip()
        df_belf0005_2["Rates"] = df_belf0005_2["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0005_2["Rates"] = ((df_belf0005_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0005 = pd.concat([df_belf0005_1, df_belf0005_2])

        df_belf0005.insert(0, 'Provider', 'Belfius')
        df_belf0005.insert(1, 'Product_ID', 'BELF0005')
        df_belf0005.insert(2, 'Category', 'Home Loan')
        df_belf0005 = df_belf0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0006
        df_belf0006 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0006 = df_belf0006.drop(df_belf0006.index[0:2])  # drop top lines --> USE THIS IF YOU WANNA DROP RANGE
        df_belf0006 = df_belf0006.drop(df_belf0006.index[3:26])
        df_belf0006.drop(df_belf0006.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0006.drop(df_belf0006.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0006.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0006["Min"] = df_belf0006["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0006["Max"] = df_belf0006["Max"].str.replace(" mois", "").str.strip()
        df_belf0006["Rates"] = df_belf0006["Rates"].str.replace(",", ".").str.strip()
        df_belf0006["Rates"] = df_belf0006["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0006["Rates"] = ((df_belf0006["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0006.insert(0, 'Provider', 'Belfius')
        df_belf0006.insert(1, 'Product_ID', 'BELF0006')
        df_belf0006.insert(2, 'Category', 'Home Loan')
        df_belf0006 = df_belf0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0007
        df_belf0007 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                                pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0007 = df_belf0007.loc[[5]]  # use this to parse one line
        df_belf0007.drop(df_belf0007.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0007.drop(df_belf0007.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0007.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0007["Min"] = df_belf0007["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0007["Max"] = df_belf0007["Max"].str.replace(" mois", "").str.strip()
        df_belf0007["Rates"] = df_belf0007["Rates"].str.replace(",", ".").str.strip()
        df_belf0007["Rates"] = df_belf0007["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0007["Rates"] = ((df_belf0007["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0007.insert(0, 'Provider', 'Belfius')
        df_belf0007.insert(1, 'Product_ID', 'BELF0007')
        df_belf0007.insert(2, 'Category', 'Home Loan')
        df_belf0007 = df_belf0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0008

        df_belf0008 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                               pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0008 = df_belf0008.loc[[6]]  # use this to parse one line
        df_belf0008.drop(df_belf0008.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0008.drop(df_belf0008.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0008.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0008["Min"] = df_belf0008["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0008["Max"] = df_belf0008["Max"].str.replace(" mois", "").str.strip()
        df_belf0008["Rates"] = df_belf0008["Rates"].str.replace(",", ".").str.strip()
        df_belf0008["Rates"] = df_belf0008["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0008["Rates"] = ((df_belf0008["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0008.insert(0, 'Provider', 'Belfius')
        df_belf0008.insert(1, 'Product_ID', 'BELF0008')
        df_belf0008.insert(2, 'Category', 'Home Loan')
        df_belf0008 = df_belf0008[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0009

        df_belf0009 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                               pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0009 = df_belf0009.loc[[7]]  # use this to parse one line
        df_belf0009.drop(df_belf0009.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0009.drop(df_belf0009.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0009.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0009["Min"] = df_belf0009["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0009["Max"] = df_belf0009["Max"].str.replace(" mois", "").str.strip()
        df_belf0009["Rates"] = df_belf0009["Rates"].str.replace(",", ".").str.strip()
        df_belf0009["Rates"] = df_belf0009["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0009["Rates"] = ((df_belf0009["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0009.insert(0, 'Provider', 'Belfius')
        df_belf0009.insert(1, 'Product_ID', 'BELF0009')
        df_belf0009.insert(2, 'Category', 'Home Loan')
        df_belf0009 = df_belf0009[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BELF0010

        df_belf0010 = read_pdf('https://www.belfius.be/imagingservlet/GetDocument?src=mifid&id=TARIFLOANFIDELITY_FR', encoding='ISO-8859-1',
                               pages=2, stream=True, spreadsheet=True, pandas_options={'header': None})
        df_belf0010 = df_belf0010.loc[[8]]  # use this to parse one line
        df_belf0010.drop(df_belf0010.columns[1:3], axis=1, inplace=True)  # drop the CAP columns
        df_belf0010.drop(df_belf0010.columns[3], axis=1, inplace=True)  # drop the column Rates Mensuel
        df_belf0010.columns = ["Formulas", "Min", "Max", "Rates"]

        df_belf0010["Min"] = df_belf0010["Min"].str.replace(" mois", "").str.strip()  # delete "Mois" in Min and Max
        df_belf0010["Max"] = df_belf0010["Max"].str.replace(" mois", "").str.strip()
        df_belf0010["Rates"] = df_belf0010["Rates"].str.replace(",", ".").str.strip()
        df_belf0010["Rates"] = df_belf0010["Rates"].str.replace(" %", "").str.strip()  # delete % so we can calculate below
        df_belf0010["Rates"] = ((df_belf0010["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        df_belf0010.insert(0, 'Provider', 'Belfius')
        df_belf0010.insert(1, 'Product_ID', 'BELF0010')
        df_belf0010.insert(2, 'Category', 'Home Loan')
        df_belf0010 = df_belf0010[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global belf_c
        belf_c = pd.concat([
            pd.concat([df_belf0001], axis=1),
            pd.concat([df_belf0002], axis=1),
            pd.concat([df_belf0003], axis=1),
            pd.concat([df_belf0004], axis=1),
            pd.concat([df_belf0005], axis=1),
            pd.concat([df_belf0006], axis=1),
            pd.concat([df_belf0007], axis=1),
            pd.concat([df_belf0008], axis=1),
            pd.concat([df_belf0009], axis=1),
            pd.concat([df_belf0010], axis=1)
        ])

        print(tabulate(belf_c, headers='keys', tablefmt='psql', showindex="never"))

    except:
        pass

def belfius_save():
    belfius()
    print(belf_c)
    #path = os.path.abspath("History/")  # saving file to the folder history
    #file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    #belf_c.to_csv(os.path.join(path, file_name), index=False)



# #  ______  ______  ______     _______               _      # #
# # (____  \|  ___ \(_____ \   (_______)         _   (_)     # #
# #  ____)  ) |   | |_____) )   _____ ___   ____| |_  _  ___ # #
# # |  __  (| |   | |  ____/   |  ___) _ \ / ___)  _)| |/___)# #
# # | |__)  ) |   | | |        | |  | |_| | |   | |__| |___ |# #
# # |______/|_|   |_|_|        |_|   \___/|_|    \___)_(___/ # #
# #                                                          # #

def bnpf():
    try:
        
    # BNPF0001
        df_bnpx0001 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=2, pandas_options={'header': None})

        df_bnpf0001 = df_bnpx0001.drop(df_bnpx0001.index[0:3])
        df_bnpf0001 = df_bnpf0001.dropna(axis='columns')
        df_bnpf0001 = df_bnpf0001.drop(df_bnpf0001.columns[1], axis=1).drop(df_bnpf0001.columns[3], axis=1)
        df_bnpf0001.columns = ["Formulas", "Rates"]
        df_bnpf0001["Rates"] = df_bnpf0001["Rates"].str.replace("%", "").str.strip()
        df_bnpf0001["Formulas"] = df_bnpf0001["Formulas"].str.replace("Ã©", "e").str.strip()
        Min_bnpf0001 = pd.DataFrame({'Min': ['', '', '', '0', '11', '14', '16', '19', '21', '26']})
        Max_bnpf0001 = pd.DataFrame({'Max': ['', '', '', '10', '13', '15', '18', '20', '25', '30']})
        duration_bnpf0001 = Min_bnpf0001.join(Max_bnpf0001)
        df_bnpf0001.insert(0, 'Provider', 'BNPF')
        df_bnpf0001.insert(1, 'Product_ID', 'BNPF0001')
        df_bnpf0001.insert(2, 'Category', 'Home Loan')
        df_bnpf0001 = df_bnpf0001.join(duration_bnpf0001)  # join newly made df with existed df
        df_bnpf0001 = df_bnpf0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0002
        df_bnpx0002 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0002 = df_bnpx0002.drop(df_bnpx0002.index[0:5]).drop(df_bnpx0002.index[10:19])
        df_bnpf0002 = df_bnpf0002.dropna(axis='columns')
        df_bnpf0002 = df_bnpf0002.drop(df_bnpf0002.columns[0], axis=1)
        df_bnpf0002.columns = ["Rates"]
        df_bnpf0002["Rates"] = df_bnpf0002["Rates"].str.replace("%", "").str.strip()
        df_bnpf0002["Formulas"] = ['1/1 +3/-3 Indice A (duree ≤ 10ans)', '1/1 +3/-3 Indice A (durée > 10ans et ≤ 15ans)', '1/1 +3/-3 Indice A (durée > 15ans et ≤ 20ans)', '1/1 +3/-3 Indice A (durée > 20ans et ≤ 25ans)', '1/1 +3/-3 Indice A (durée > 25ans et ≤ 30ans)']

        Min_bnpf0002 = pd.DataFrame({'Min': [''] * 5 + ['0', '11', '16', '21', '26']})
        Max_bnpf0002 = pd.DataFrame({'Max': [''] * 5 + ['10', '15', '20', '25', '30']})
        duration_bnpf0002 = Min_bnpf0002.join(Max_bnpf0002)

        df_bnpf0002.insert(0, 'Provider', 'BNPF')
        df_bnpf0002.insert(1, 'Product_ID', 'BNPF0002')
        df_bnpf0002.insert(2, 'Category', 'Home Loan')
        df_bnpf0002 = df_bnpf0002.join(duration_bnpf0002)  # join newly made df with existed df
        df_bnpf0002 = df_bnpf0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0003
        df_bnpf0003 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0003 = df_bnpf0003.drop(df_bnpf0003.index[0:10]).drop(df_bnpf0003.index[11:19])
        df_bnpf0003 = df_bnpf0003.dropna(axis='columns')
        df_bnpf0003 = df_bnpf0003.drop(df_bnpf0003.columns[0], axis=1)
        df_bnpf0003.columns = ["_mens_", "Rates"]
        df_bnpf0003.drop('_mens_', axis=1, inplace=True)
        df_bnpf0003["Rates"] = df_bnpf0003["Rates"].str.replace("%", "").str.strip()
        df_bnpf0003["Formulas"] = ['1/1 +3/-3 Indice A mensualite constante (duree initiale 15 ans)']

        Min_bnpf0003 = pd.DataFrame({'Min': [''] * 10 + ['15']})
        Max_bnpf0003 = pd.DataFrame({'Max': [''] * 10 + ['25']})
        duration_bnpf0003 = Min_bnpf0003.join(Max_bnpf0003)

        df_bnpf0003.insert(0, 'Provider', 'BNPF')
        df_bnpf0003.insert(1, 'Product_ID', 'BNPF0003')
        df_bnpf0003.insert(2, 'Category', 'Home Loan')
        df_bnpf0003 = df_bnpf0003.join(duration_bnpf0003)  # join newly made df with existed df
        df_bnpf0003 = df_bnpf0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0004
        df_bnpf0004 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0004 = df_bnpf0004.drop(df_bnpf0004.index[0:12]).drop(df_bnpf0004.index[13:19])
        df_bnpf0004 = df_bnpf0004.dropna(axis='columns')
        df_bnpf0004 = df_bnpf0004.drop(df_bnpf0004.columns[0], axis=1)
        df_bnpf0004.columns = ["_mens_", "Rates"]
        df_bnpf0004.drop('_mens_', axis=1, inplace=True)
        df_bnpf0004["Rates"] = df_bnpf0004["Rates"].str.replace("%", "").str.strip()
        df_bnpf0004["Formulas"] = ['1/1 +3/-3 Indice A mensualite constante (duree initiale 20 ans)']

        Min_bnpf0004 = pd.DataFrame({'Min': [''] * 12 + ['20']})
        Max_bnpf0004 = pd.DataFrame({'Max': [''] * 12 + ['25']})
        duration_bnpf0004 = Min_bnpf0004.join(Max_bnpf0004)

        df_bnpf0004.insert(0, 'Provider', 'BNPF')
        df_bnpf0004.insert(1, 'Product_ID', 'BNPF0004')
        df_bnpf0004.insert(2, 'Category', 'Home Loan')
        df_bnpf0004 = df_bnpf0004.join(duration_bnpf0004)  # join newly made df with existed df
        df_bnpf0004 = df_bnpf0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0005
        df_bnpf0005 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0005 = df_bnpf0005.drop(df_bnpf0005.index[0:14]).drop(df_bnpf0005.index[15:19])
        df_bnpf0005 = df_bnpf0005.dropna(axis='columns')
        df_bnpf0005 = df_bnpf0005.drop(df_bnpf0005.columns[0], axis=1)
        df_bnpf0005.columns = ["_mens_", "Rates"]
        df_bnpf0005.drop('_mens_', axis=1, inplace=True)
        df_bnpf0005["Rates"] = df_bnpf0005["Rates"].str.replace("%", "").str.strip()
        df_bnpf0005["Formulas"] = ['1/1 +3/-3 Indice A mensualite constante (duree initiale 25 ans)']

        Min_bnpf0005 = pd.DataFrame({'Min': [''] * 14 + ['20']})
        Max_bnpf0005 = pd.DataFrame({'Max': [''] * 14 + ['25']})
        duration_bnpf0005 = Min_bnpf0005.join(Max_bnpf0005)

        df_bnpf0005.insert(0, 'Provider', 'BNPF')
        df_bnpf0005.insert(1, 'Product_ID', 'BNPF0005')
        df_bnpf0005.insert(2, 'Category', 'Home Loan')
        df_bnpf0005 = df_bnpf0005.join(duration_bnpf0005)  # join newly made df with existed df
        df_bnpf0005 = df_bnpf0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0006
        df_bnpf0006 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0006 = df_bnpf0006.drop(df_bnpf0006.index[0:16]).drop(df_bnpf0006.index[17:19])
        df_bnpf0006 = df_bnpf0006.dropna(axis='columns')
        df_bnpf0006 = df_bnpf0006.drop(df_bnpf0006.columns[0], axis=1)
        df_bnpf0006.columns = ["_mens_", "Rates"]
        df_bnpf0006.drop('_mens_', axis=1, inplace=True)
        df_bnpf0006["Rates"] = df_bnpf0006["Rates"].str.replace("%", "").str.strip()
        df_bnpf0006["Formulas"] = ['5/5 +4/-4 indice E']

        Min_bnpf0006 = pd.DataFrame({'Min': [''] * 16 + ['10']})
        Max_bnpf0006 = pd.DataFrame({'Max': [''] * 16 + ['25']})
        duration_bnpf0006 = Min_bnpf0006.join(Max_bnpf0006)

        df_bnpf0006.insert(0, 'Provider', 'BNPF')
        df_bnpf0006.insert(1, 'Product_ID', 'BNPF0006')
        df_bnpf0006.insert(2, 'Category', 'Home Loan')
        df_bnpf0006 = df_bnpf0006.join(duration_bnpf0006)  # join newly made df with existed df
        df_bnpf0006 = df_bnpf0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0007
        df_bnpf0007 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0007 = df_bnpf0007.drop(df_bnpf0007.index[0:17]).drop(df_bnpf0007.index[18:19])
        df_bnpf0007 = df_bnpf0007.dropna(axis='columns')
        df_bnpf0007 = df_bnpf0007.drop(df_bnpf0007.columns[0], axis=1)
        df_bnpf0007.columns = ["_mens_", "Rates"]
        df_bnpf0007.drop('_mens_', axis=1, inplace=True)
        df_bnpf0007["Rates"] = df_bnpf0007["Rates"].str.replace("%", "").str.strip()
        df_bnpf0007["Formulas"] = ['10/5 +2/-5 indice E']

        Min_bnpf0007 = pd.DataFrame({'Min': [''] * 17 + ['10']})
        Max_bnpf0007 = pd.DataFrame({'Max': [''] * 17 + ['25']})
        duration_bnpf0007 = Min_bnpf0007.join(Max_bnpf0007)

        df_bnpf0007.insert(0, 'Provider', 'BNPF')
        df_bnpf0007.insert(2, 'Category', 'Home Loan')
        df_bnpf0007.insert(1, 'Product_ID', 'BNPF0007')
        df_bnpf0007 = df_bnpf0007.join(duration_bnpf0007)  # join newly made df with existed df
        df_bnpf0007 = df_bnpf0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # BNPF0008
        df_bnpf0008 = read_pdf('https://www.bnpparibasfortis.be/rsc/contrib/document/1-Website/5-Docserver/BNP/F00015F.pdf', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})

        df_bnpf0008 = df_bnpf0008.drop(df_bnpf0008.index[0:18])
        df_bnpf0008 = df_bnpf0008.dropna(axis='columns')
        df_bnpf0008 = df_bnpf0008.drop(df_bnpf0008.columns[0], axis=1)
        df_bnpf0008.columns = ["Rates"]
        df_bnpf0008["Rates"] = df_bnpf0008["Rates"].str.replace("%", "").str.strip()
        df_bnpf0008["Formulas"] = ['15/5 +2/-5 indice E  (duree ≤ 25 ans)']

        Min_bnpf0008 = pd.DataFrame({'Min': [''] * 18 + ['15']})
        Max_bnpf0008 = pd.DataFrame({'Max': [''] * 18 + ['25']})
        duration_bnpf0008 = Min_bnpf0008.join(Max_bnpf0008)

        df_bnpf0008.insert(0, 'Provider', 'BNPF')
        df_bnpf0008.insert(1, 'Product_ID', 'BNPF0008')
        df_bnpf0008.insert(2, 'Category', 'Home Loan')
        df_bnpf0008 = df_bnpf0008.join(duration_bnpf0008)  # join newly made df with existed df
        df_bnpf0008 = df_bnpf0008[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global bnpf_c
        bnpf_c = pd.concat([
            pd.concat([df_bnpf0001], axis=1),
            pd.concat([df_bnpf0002], axis=1),
            pd.concat([df_bnpf0003], axis=1),
            pd.concat([df_bnpf0004], axis=1),
            pd.concat([df_bnpf0005], axis=1),
            pd.concat([df_bnpf0006], axis=1),
            pd.concat([df_bnpf0007], axis=1),
            pd.concat([df_bnpf0008], axis=1)])

        print(tabulate(bnpf_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def bnpf_save():
    bnpf()

    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    bnpf_c.to_csv(os.path.join(path, file_name), index=False)



# #   ______ ______   ______  # #
# #  / _____|____  \ / _____) # #
# # | /      ____)  ) /       # #
# # | |     |  __  (| |       # #
# # | \_____| |__)  ) \_____  # #
# #  \______)______/ \______) # #
# #                           # #

def cbc():
    
    try:
    
    # Source
        df_cbcx_source1 = read_pdf('https://www.cbc.be/content/dam/particulieren/f-cbc/product/lenen/Wonen/woonkrediet/Carte%20des%20taux%20des%20Cr%C3%A9dits%20logement.pdf', encoding='ISO-8859-1', area=[310, 27.36, 380, 890], pages=1, pandas_options={'header': None})
        df_cbcx_source2 = read_pdf('https://www.cbc.be/content/dam/particulieren/f-cbc/product/lenen/Wonen/woonkrediet/Carte%20des%20taux%20des%20Cr%C3%A9dits%20logement.pdf', encoding='ISO-8859-1', area=[290, 1000, 360, 1175], pages=1, pandas_options={'header': None})
        df_cbcx_source1.drop(columns=[2,3,4,5,7,8,9,10], inplace=True)
        print(df_cbcx_source1)

    # CBC0001
        ## Rate for >25000
        df_cbcx0001_1 = df_cbcx_source2.copy()
        df_cbcx0001_1.columns = ['Duration', 'Rates']
        temp = df_cbcx0001_1['Duration'].str.split('<=', 1).str  # split the element within a table
        Min = temp[0]
        Max = temp[1]
        df_cbcx0001_1.insert(1,'Min',Min)
        df_cbcx0001_1.insert(2,'Max',Max)
        df_cbcx0001_1["Min"] = df_cbcx0001_1["Min"].str.replace(">", "").str.strip()
        df_cbcx0001_1["Min"] = df_cbcx0001_1["Min"].str.replace("et", "").str.strip()
        df_cbcx0001_1["Max"] = df_cbcx0001_1["Max"].str.replace("ans", "").str.strip()
        df_cbcx0001_1.insert(0, "Formulas", "Fixed rate > 25000")
        df_cbcx0001_1["Rates"] = df_cbcx0001_1["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0001_1.drop('Duration', axis=1, inplace = True)

        ## Rate for <25000
        df_cbcx0001_2 = df_cbcx_source2.copy()
        df_cbcx0001_2.columns = ['Duration', 'Rates']
        temp = df_cbcx0001_2['Duration'].str.split('<=', 1).str  # split the element within a table
        Min = temp[0]
        Max = temp[1]
        df_cbcx0001_2.insert(1,'Min',Min)
        df_cbcx0001_2.insert(2,'Max',Max)
        df_cbcx0001_2["Min"] = df_cbcx0001_2["Min"].str.replace(">", "").str.strip()
        df_cbcx0001_2["Min"] = df_cbcx0001_2["Min"].str.replace("et", "").str.strip()
        df_cbcx0001_2["Max"] = df_cbcx0001_2["Max"].str.replace("ans", "").str.strip()
        df_cbcx0001_2.insert(0, "Formulas", "Fixed rate < 25000")
        df_cbcx0001_2["Rates"] = df_cbcx0001_2["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0001_2.drop('Duration', axis=1, inplace = True)

        df_cbcx0001_2["Rates"] = ((df_cbcx0001_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        ##Concatenate rates for >25000 and <25000
        df_cbcx0001_1.columns = df_cbcx0001_2.columns
        data_cbcx0001 = pd.concat([df_cbcx0001_1, df_cbcx0001_2])

        data_cbcx0001.insert(0, 'Provider', 'CBC')
        data_cbcx0001.insert(1, 'Product_ID', 'CBC0001')
        data_cbcx0001.insert(2, 'Category', 'Home Loan')
        data_cbcx0001 = data_cbcx0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CBC0002
        ## Rate for >25000
        df_cbcx0002_1 = df_cbcx_source1.drop([6,11],axis=1)
        df_cbcx0002_1.columns = ["Max", "Rates"]
        df_cbcx0002_1.insert(0, "Formulas", "1/1/1 > 25000")
        df_cbcx0002_1["Max"] = df_cbcx0002_1["Max"].str.replace("ans", "").str.strip()
        df_cbcx0002_1["Max"] = df_cbcx0002_1["Max"].str.replace("<=", "").str.strip()
        df_cbcx0002_1["Rates"] = df_cbcx0002_1["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0002_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_cbcx0002_2 = df_cbcx_source1.drop([6,11],axis=1)
        df_cbcx0002_2.columns = ["Max", "Rates"]
        df_cbcx0002_2.insert(0, "Formulas", "1/1/1 < 25000")
        df_cbcx0002_2["Max"] = df_cbcx0002_2["Max"].str.replace("ans", "").str.strip()
        df_cbcx0002_2["Max"] = df_cbcx0002_2["Max"].str.replace("<=", "").str.strip()
        df_cbcx0002_2["Rates"] = df_cbcx0002_2["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0002_2.insert(1, 'Min', [0,11,16,21])
        df_cbcx0002_2["Rates"] = ((df_cbcx0002_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_cbcx0002 = pd.concat([df_cbcx0002_1, df_cbcx0002_2])
        data_cbcx0002.insert(0, 'Provider', 'CBC')
        data_cbcx0002.insert(1, 'Product_ID', 'CBC0002')
        data_cbcx0002.insert(2, 'Category', 'Home Loan')
        data_cbcx0002 = data_cbcx0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CBC0003
        ## Rate for >25000
        df_cbcx0003_1 = df_cbcx_source1.drop([1,11],axis=1)
        df_cbcx0003_1.columns = ["Max", "Rates"]
        df_cbcx0003_1.insert(0, "Formulas", "3/3/3 > 25000")
        df_cbcx0003_1["Max"] = df_cbcx0003_1["Max"].str.replace("ans", "").str.strip()
        df_cbcx0003_1["Max"] = df_cbcx0003_1["Max"].str.replace("<=", "").str.strip()
        df_cbcx0003_1["Rates"] = df_cbcx0003_1["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0003_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_cbcx0003_2 = df_cbcx_source1.drop([1,11],axis=1)
        df_cbcx0003_2.columns = ["Max", "Rates"]
        df_cbcx0003_2.insert(0, "Formulas", "3/3/3 < 25000")
        df_cbcx0003_2["Max"] = df_cbcx0003_2["Max"].str.replace("ans", "").str.strip()
        df_cbcx0003_2["Max"] = df_cbcx0003_2["Max"].str.replace("<=", "").str.strip()
        df_cbcx0003_2["Rates"] = df_cbcx0003_2["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0003_2.insert(1, 'Min', [0,11,16,21])
        df_cbcx0003_2["Rates"] = ((df_cbcx0003_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_cbcx0003 = pd.concat([df_cbcx0003_1, df_cbcx0003_2])
        data_cbcx0003.insert(0, 'Provider', 'CBC')
        data_cbcx0003.insert(1, 'Product_ID', 'CBC0003')
        data_cbcx0003.insert(2, 'Category', 'Home Loan')
        data_cbcx0003 = data_cbcx0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns
    
    # CBC0004
        ## Rate for >25000
        df_cbcx0004_1 = df_cbcx_source1.drop([1,6],axis=1)
        df_cbcx0004_1.columns = ["Max", "Rates"]
        df_cbcx0004_1.insert(0, "Formulas", "5/5/5 > 25000")
        df_cbcx0004_1["Max"] = df_cbcx0004_1["Max"].str.replace("ans", "").str.strip()
        df_cbcx0004_1["Max"] = df_cbcx0004_1["Max"].str.replace("<=", "").str.strip()
        df_cbcx0004_1["Rates"] = df_cbcx0004_1["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0004_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_cbcx0004_2 = df_cbcx_source1.drop([1,6],axis=1)
        df_cbcx0004_2.columns = ["Max", "Rates"]
        df_cbcx0004_2.insert(0, "Formulas", "5/5/5 < 25000")
        df_cbcx0004_2["Max"] = df_cbcx0004_2["Max"].str.replace("ans", "").str.strip()
        df_cbcx0004_2["Max"] = df_cbcx0004_2["Max"].str.replace("<=", "").str.strip()
        df_cbcx0004_2["Rates"] = df_cbcx0004_2["Rates"].str.replace(",", ".").str.strip()
        df_cbcx0004_2.insert(1, 'Min', [0,11,16,21])
        df_cbcx0004_2["Rates"] = ((df_cbcx0004_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_cbcx0004 = pd.concat([df_cbcx0004_1, df_cbcx0004_2])
        data_cbcx0004.insert(0, 'Provider', 'CBC')
        data_cbcx0004.insert(1, 'Product_ID', 'CBC0004')
        data_cbcx0004.insert(2, 'Category', 'Home Loan')
        data_cbcx0004 = data_cbcx0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global cbcx_c
        cbcx_c = pd.concat([
            pd.concat([data_cbcx0001], axis=1),
            pd.concat([data_cbcx0002], axis=1),
            pd.concat([data_cbcx0003], axis=1),
            pd.concat([data_cbcx0004], axis=1)])

        print(tabulate(cbcx_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def cbc_save():
    cbc()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    cbcx_c.to_csv(os.path.join(path, file_name), index=False)

# #   ______ ______  _     _  # #
# #  / _____|_____ \| |   | | # #
# # | /      _____) ) |__ | | # #
# # | |     |  ____/|  __)| | # #
# # | \_____| |     | |   | | # #
# #  \______)_|     |_|   |_| # #
# #                           # #


def cph():
    ##########################The lines below are required to parse directly from the web link######################

    data = requests.get("https://www.cph.be/credits/credits-prives/cph-logement/tarif-logement.html")
    soup = BeautifulSoup(data.content, "lxml")

    result = soup.findAll('a', attrs={'href': re.compile("^/images/stories/PDF/")})[0].get('href')
    base = "https://www.cph.be"
    new_pdf_cphx = base + result


    try:

    # CPHX0001
        df_cphl = read_pdf(new_pdf_cphx, encoding='ISO-8859-1', pages=1, pandas_options={'header': None})

        ##take rate of 0-2 years
        df_cphx0001_1 = df_cphl.drop(df_cphl.index[1:29])
        df_cphx0001_1.drop(df_cphx0001_1.columns[2:5], axis=1, inplace=True)
        df_cphx0001_1.columns = ["Formulas", "Rates"]
        df_cphx0001_1["Rates"] = df_cphx0001_1["Rates"].str.replace("%", "").str.strip()
        df_cphx0001_1["Rates"] = df_cphx0001_1["Rates"].str.replace(",", ".").str.strip()

        df_cphx0001_1["Rates"] = ((df_cphx0001_1["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        Min_df_cphx0001_1 = pd.DataFrame({'Min': ['0']})
        Max_df_cphx0001_1 = pd.DataFrame({'Max': ['2']})

        duration_cphx0001_1 = Min_df_cphx0001_1.join(Max_df_cphx0001_1)
        df_cphx0001_1 = df_cphx0001_1.join(duration_cphx0001_1)

        ## take rates of the rest
        df_cphx0001 = df_cphl.drop(df_cphl.index[0]).drop(df_cphl.index[8:29])
        df_cphx0001.drop(df_cphx0001.columns[2:5], axis=1, inplace=True)
        df_cphx0001.columns = ["Formulas", "Rates"]
        df_cphx0001["Rates"] = df_cphx0001["Rates"].str.replace("%", "").str.strip()
        df_cphx0001["Rates"] = df_cphx0001["Rates"].str.replace(",", ".").str.strip()

        Min_cphx0001 = pd.DataFrame({'Min': ['', '3', '4', '6', '11', '16', '21', '26']})
        Max_cphx0001 = pd.DataFrame({'Max': ['', '3', '5', '10', '15', '20', '25', '30']})

        duration_cphx0001 = Min_cphx0001.join(Max_cphx0001)
        df_cphx0001 = df_cphx0001.join(duration_cphx0001)

        # Concatenate rates for 0-2 years and rest of the years
        df_cphx0001.columns = df_cphx0001_1.columns
        data_cphx0001 = pd.concat([df_cphx0001_1, df_cphx0001])

        data_cphx0001.insert(0, 'Provider', 'CPH')
        data_cphx0001.insert(1, 'Product_ID', 'CPHX0001')
        data_cphx0001.insert(2, 'Category', 'Home Loan')
        data_cphx0001 = data_cphx0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0002
        ###take rate of 1-2 years
        df_cphx0002_1 = df_cphl.drop(df_cphl.index[0:8]).drop(df_cphl.index[9:34])
        df_cphx0002_1 = df_cphx0002_1.dropna(axis='columns')
        df_cphx0002_1.drop(df_cphx0002_1.columns[2:5], axis=1, inplace=True)
        df_cphx0002_1.columns = ["Formulas", "Rates"]
        df_cphx0002_1["Rates"] = df_cphx0002_1["Rates"].str.replace("%", "").str.strip()
        df_cphx0002_1["Rates"] = df_cphx0002_1["Rates"].str.replace(",", ".").str.strip()
        df_cphx0002_1["Formulas"] = df_cphx0002_1["Formulas"].str.replace("Ã©", "e").str.strip()

        df_cphx0002_1["Rates"] = ((df_cphx0002_1["Rates"].astype(float) / 100) + (0.5 / 100)) * 100  # multiply values by specific rate of 0.5%

        Min_cphx0002_1 = pd.DataFrame({'Min': [''] * 8 + ['1']})
        Max_cphx0002_1 = pd.DataFrame({'Max': [''] * 8 + ['2']})
        duration_cphx0002_1 = Min_cphx0002_1.join(Max_cphx0002_1)

        df_cphx0002_1 = df_cphx0002_1.join(duration_cphx0002_1)

        ###take rate of 3-30 years

        df_cphx0002 = df_cphl.drop(df_cphl.index[0:8]).drop(df_cphl.index[9:34])
        df_cphx0002 = df_cphx0002.dropna(axis='columns')
        df_cphx0002.drop(df_cphx0002.columns[2:5], axis=1, inplace=True)
        df_cphx0002.columns = ["Formulas", "Rates"]
        df_cphx0002["Rates"] = df_cphx0002["Rates"].str.replace("%", "").str.strip()
        df_cphx0002["Rates"] = df_cphx0002["Rates"].str.replace(",", ".").str.strip()
        df_cphx0002["Formulas"] = df_cphx0002["Formulas"].str.replace("Ã©", "e").str.strip()

        Min_cphx0002 = pd.DataFrame({'Min': [''] * 8 + ['3']})
        Max_cphx0002 = pd.DataFrame({'Max': [''] * 8 + ['30']})
        duration_cphx0002 = Min_cphx0002.join(Max_cphx0002)

        df_cphx0002 = df_cphx0002.join(duration_cphx0002)

        # Concatenate rates for 0-2 years and rest of the years
        df_cphx0002.columns = df_cphx0002_1.columns
        data_cphx0002 = pd.concat([df_cphx0002_1, df_cphx0002])

        data_cphx0002.insert(0, 'Provider', 'CPH')
        data_cphx0002.insert(1, 'Product_ID', 'CPHX0002')
        data_cphx0002.insert(2, 'Category', 'Home Loan')

        data_cphx0002 = data_cphx0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0003
        df_cphl = read_pdf(new_pdf_cphx, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0003 = df_cphl.drop(df_cphl.index[0:9]).drop(df_cphl.index[10:34])
        df_cphx0003 = df_cphx0003.dropna(axis='columns')
        df_cphx0003.drop(df_cphx0003.columns[2:5], axis=1, inplace=True)
        df_cphx0003.columns = ["Formulas", "Rates"]
        df_cphx0003["Rates"] = df_cphx0003["Rates"].str.replace("%", "").str.strip()
        df_cphx0003["Formulas"] = df_cphx0003["Formulas"].str.replace("Ã©", "e").str.strip()

        df_cphx0003.insert(0, 'Provider', 'CPH')
        df_cphx0003.insert(1, 'Product_ID', 'CPHX0003')
        df_cphx0003.insert(2, 'Category', 'Home Loan')
        df_cphx0003.insert(3, 'Min', '')
        df_cphx0003.insert(4, 'Max', '')

        df_cphx0003 = df_cphx0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0004
        df_cphl = read_pdf(new_pdf_cphx, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0004 = df_cphl.drop(df_cphl.index[0:10]).drop(df_cphl.index[11:34])
        df_cphx0004 = df_cphx0004.dropna(axis='columns')
        df_cphx0004.drop(df_cphx0004.columns[2:5], axis=1, inplace=True)
        df_cphx0004.columns = ["Formulas", "Rates"]
        df_cphx0004["Rates"] = df_cphx0004["Rates"].str.replace("%", "").str.strip()
        df_cphx0004["Formulas"] = df_cphx0004["Formulas"].str.replace("Ã©", "e").str.strip()

        df_cphx0004.insert(0, 'Provider', 'CPH')
        df_cphx0004.insert(1, 'Product_ID', 'CPHX0004')
        df_cphx0004.insert(2, 'Category', 'Home Loan')
        df_cphx0004.insert(3, 'Min', '')
        df_cphx0004.insert(4, 'Max', '')

        df_cphx0004 = df_cphx0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0005
        df_cphx = read_pdf('https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190301.pdf#view=fitV', encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0005 = df_cphx.drop(df_cphx.index[0:11]).drop(df_cphx.index[12:34])
        df_cphx0005 = df_cphx0005.dropna(axis='columns')
        df_cphx0005.drop(df_cphx0005.columns[2:5], axis=1, inplace=True)
        df_cphx0005.columns = ["Formulas", "Rates"]
        df_cphx0005["Rates"] = df_cphx0005["Rates"].str.replace("%", "").str.strip()
        df_cphx0005["Formulas"] = df_cphx0005["Formulas"].str.replace("Ã©", "e").str.strip()

        df_cphx0005.insert(0, 'Provider', 'CPH')
        df_cphx0005.insert(1, 'Product_ID', 'CPHX0005')
        df_cphx0005.insert(2, 'Category', 'Home Loan')
        df_cphx0005.insert(3, 'Min', '')
        df_cphx0005.insert(4, 'Max', '')

        df_cphx0005 = df_cphx0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0006
        df_cphx = read_pdf('https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190301.pdf#view=fitV', encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0006 = df_cphx.drop(df_cphx.index[0:12]).drop(df_cphx.index[13:34])
        df_cphx0006 = df_cphx0006.dropna(axis='columns')
        df_cphx0006.drop(df_cphx0006.columns[2:5], axis=1, inplace=True)
        df_cphx0006.columns = ["Formulas", "Rates"]
        df_cphx0006["Rates"] = df_cphx0006["Rates"].str.replace("%", "").str.strip()
        df_cphx0006["Formulas"] = df_cphx0006["Formulas"].str.replace("Ã©", "e").str.strip()

        df_cphx0006.insert(0, 'Provider', 'CPH')
        df_cphx0006.insert(1, 'Product_ID', 'CPHX0006')
        df_cphx0006.insert(2, 'Category', 'Home Loan')
        df_cphx0006.insert(3, 'Min', '')
        df_cphx0006.insert(4, 'Max', '')

        df_cphx0006 = df_cphx0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0007
        df_cphx = read_pdf('https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190301.pdf#view=fitV', encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0007 = df_cphx.drop(df_cphx.index[0:13]).drop(df_cphx.index[14:34])
        df_cphx0007 = df_cphx0007.dropna(axis='columns')
        df_cphx0007.drop(df_cphx0007.columns[2:5], axis=1, inplace=True)
        df_cphx0007.columns = ["Formulas", "Rates"]
        df_cphx0007["Rates"] = df_cphx0007["Rates"].str.replace("%", "").str.strip()
        df_cphx0007["Formulas"] = df_cphx0007["Formulas"].str.replace("Ã©", "e").str.strip()
        df_cphx0007.insert(0, 'Provider', 'CPH')
        df_cphx0007.insert(1, 'Product_ID', 'CPHX0007')
        df_cphx0007.insert(2, 'Category', 'Home Loan')
        df_cphx0007.insert(2, 'Min', '')
        df_cphx0007.insert(3, 'Max', '')
        df_cphx0007 = df_cphx0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CPHX0008
        df_cphx = read_pdf('https://www.cph.be/images/stories/PDF/tarif_cph_logement_20190301.pdf#view=fitV', encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_cphx0008 = df_cphx.drop(df_cphx.index[0:14]).drop(df_cphx.index[15:34])
        df_cphx0008 = df_cphx0008.dropna(axis='columns')
        df_cphx0008.drop(df_cphx0008.columns[2:5], axis=1, inplace=True)
        df_cphx0008.columns = ["Formulas", "Rates"]
        df_cphx0008["Rates"] = df_cphx0008["Rates"].str.replace("%", "").str.strip()
        df_cphx0008["Formulas"] = df_cphx0008["Formulas"].str.replace("Ã©", "e").str.strip()
        df_cphx0008.insert(0, 'Provider', 'CPH')
        df_cphx0008.insert(1, 'Product_ID', 'CPHX0008')
        df_cphx0008.insert(2, 'Category', 'Home Loan')
        df_cphx0008.insert(3, 'Min', '')
        df_cphx0008.insert(4, 'Max', '')
        df_cphx0008 = df_cphx0008[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global cphx_c
        cphx_c = pd.concat([
            pd.concat([data_cphx0001], axis=1),
            pd.concat([data_cphx0002], axis=1),
            pd.concat([df_cphx0003], axis=1),
            pd.concat([df_cphx0004], axis=1),
            pd.concat([df_cphx0005], axis=1),
            pd.concat([df_cphx0006], axis=1),
            pd.concat([df_cphx0007], axis=1),
            pd.concat([df_cphx0008], axis=1)
        ])

        print(tabulate(cphx_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def cph_save():
    cph()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    cphx_c.to_csv(os.path.join(path, file_name), index=False)

# #   ______            _              # #
# #  / _____)          | |             # #
# # | /       ____ ____| | ____ ____   # #
# # | |      / ___) _  ) |/ _  |  _ \  # #
# # | \_____| |  ( (/ /| ( ( | | | | | # #
# #  \______)_|   \____)_|\_||_|_| |_| # #
# #                                    # #

def crelan():
    ##########################The lines below are required to parse directly from the web link######################

    data = requests.get("https://www.crelan.be/fr/particuliers/produit/le-credit-logement")
    soup = BeautifulSoup(data.content, "lxml")

    result = soup.findAll('a', attrs={'href': re.compile("^/assets/")})[1].get('href')
    base = "https://www.crelan.be"
    new_pdf_crel = base + result

    try:
        
    # CREL0001
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0001 = df_crel.drop(df_crel.index[0:37]).drop(df_crel.index[44:61])
        df_crel0001 = df_crel0001.drop(df_crel0001.columns[0:2], axis=1).drop(df_crel0001.columns[4:7], axis=1)
        df_crel0001.columns = ["Formulas", "Rates"]
        df_crel0001["Rates"] = df_crel0001["Rates"].str.replace("%", "").str.strip()
        df_crel0001["Rates"] = df_crel0001["Rates"].str.replace(",", ".").str.strip()
        df_crel0001["Formulas"] = "Rates fixe de >12.500 pour " + df_crel0001["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0001 = pd.DataFrame({'Min': [''] * 37 + ['0', '11', '13', '16', '19', '21', '26']})
        Max_crel0001 = pd.DataFrame({'Max': [''] * 37 + ['10', '12', '15', '18', '20', '25', '30']})
        duration_crel0001 = Min_crel0001.join(Max_crel0001)

        df_crel0001.insert(0, 'Provider', 'Crelan')
        df_crel0001.insert(1, 'Product_ID', 'CREL0001')
        df_crel0001.insert(2, 'Category', 'Home Loan')
        df_crel0001 = df_crel0001.join(duration_crel0001)  # join newly made df with existed df
        df_crel0001 = df_crel0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0002
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0002 = df_crel.drop(df_crel.index[3:61])
        df_crel0002 = df_crel0002.drop(df_crel0002.columns[0:2], axis=1).drop(df_crel0002.columns[4:7], axis=1)
        df_crel0002.columns = ["Formulas", "Rates"]
        df_crel0002["Rates"] = df_crel0002["Rates"].str.replace("%", "").str.strip()
        df_crel0002["Rates"] = df_crel0002["Rates"].str.replace(",", ".").str.strip()
        df_crel0002["Formulas"] = "Rates 1/1/1 de >12.500 pour " + df_crel0002["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0002 = pd.DataFrame({'Min': ['0', '16', '21']})
        Max_crel0002 = pd.DataFrame({'Max': ['15', '20', '25']})
        duration_crel0002 = Min_crel0002.join(Max_crel0002)

        df_crel0002.insert(0, 'Provider', 'Crelan')
        df_crel0002.insert(1, 'Product_ID', 'CREL0002')
        df_crel0002.insert(2, 'Category', 'Home Loan')
        df_crel0002 = df_crel0002.join(duration_crel0002)  # join newly made df with existed df
        df_crel0002 = df_crel0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0003
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0003 = df_crel.drop(df_crel.index[0:3]).drop(df_crel.index[7:61])
        df_crel0003 = df_crel0003.drop(df_crel0003.columns[0:2], axis=1).drop(df_crel0003.columns[4:7], axis=1)
        df_crel0003.columns = ["Formulas", "Rates"]
        df_crel0003["Rates"] = df_crel0003["Rates"].str.replace("%", "").str.strip()
        df_crel0003["Rates"] = df_crel0003["Rates"].str.replace(",", ".").str.strip()
        df_crel0003["Formulas"] = "Rates 3/3/3 de >12.500 pour " + df_crel0003["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0003 = pd.DataFrame({'Min': [''] * 3 + ['0', '16', '21', '26']})
        Max_crel0003 = pd.DataFrame({'Max': [''] * 3 + ['15', '20', '25', '30']})
        duration_crel0003 = Min_crel0003.join(Max_crel0003)

        df_crel0003.insert(0, 'Provider', 'Crelan')
        df_crel0003.insert(1, 'Product_ID', 'CREL0003')
        df_crel0003.insert(2, 'Category', 'Home Loan')
        df_crel0003 = df_crel0003.join(duration_crel0003)  # join newly made df with existed df
        df_crel0003 = df_crel0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0004
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0004 = df_crel.drop(df_crel.index[0:14]).drop(df_crel.index[17:61])
        df_crel0004 = df_crel0004.drop(df_crel0004.columns[0:2], axis=1).drop(df_crel0004.columns[4:7], axis=1)
        df_crel0004.columns = ["Formulas", "Rates"]
        df_crel0004["Rates"] = df_crel0004["Rates"].str.replace("%", "").str.strip()
        df_crel0004["Rates"] = df_crel0004["Rates"].str.replace(",", ".").str.strip()
        df_crel0004["Formulas"] = "Rates 5/5/5 de >12.500 pour " + df_crel0004["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0004 = pd.DataFrame({'Min': [''] * 14 + ['0', '16', '21']})
        Max_crel0004 = pd.DataFrame({'Max': [''] * 14 + ['15', '20', '25']})
        duration_crel0004 = Min_crel0004.join(Max_crel0004)

        df_crel0004.insert(0, 'Provider', 'Crelan')
        df_crel0004.insert(1, 'Product_ID', 'CREL0004')
        df_crel0004.insert(2, 'Category', 'Home Loan')
        df_crel0004 = df_crel0004.join(duration_crel0004)  # join newly made df with existed df
        df_crel0004 = df_crel0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0005
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0005 = df_crel.drop(df_crel.index[0:17]).drop(df_crel.index[24:61])
        df_crel0005 = df_crel0005.drop(df_crel0005.columns[0:2], axis=1).drop(df_crel0005.columns[4:7], axis=1)
        df_crel0005.columns = ["Formulas", "Rates"]
        df_crel0005["Rates"] = df_crel0005["Rates"].str.replace("%", "").str.strip()
        df_crel0005["Rates"] = df_crel0005["Rates"].str.replace(",", ".").str.strip()
        df_crel0005["Formulas"] = "Rates 8/3/3 de >12.500 pour " + df_crel0005["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0005 = pd.DataFrame({'Min': [''] * 17 + ['0', '12', '15', '18', '21', '24', '27']})
        Max_crel0005 = pd.DataFrame({'Max': [''] * 17 + ['11', '14', '17', '20', '23', '26', '30']})
        duration_crel0005 = Min_crel0005.join(Max_crel0005)

        df_crel0005.insert(0, 'Provider', 'Crelan')
        df_crel0005.insert(1, 'Product_ID', 'CREL0005')
        df_crel0005.insert(2, 'Category', 'Home Loan')
        df_crel0005 = df_crel0005.join(duration_crel0005)  # join newly made df with existed df
        df_crel0005 = df_crel0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0006
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0006 = df_crel.drop(df_crel.index[0:24]).drop(df_crel.index[27:61])
        df_crel0006 = df_crel0006.drop(df_crel0006.columns[0:2], axis=1).drop(df_crel0006.columns[4:7], axis=1)
        df_crel0006.columns = ["Formulas", "Rates"]
        df_crel0006["Rates"] = df_crel0006["Rates"].str.replace("%", "").str.strip()
        df_crel0006["Rates"] = df_crel0006["Rates"].str.replace(",", ".").str.strip()
        df_crel0006["Formulas"] = "Rates 10/5/5 de >12.500 pour " + df_crel0006["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0006 = pd.DataFrame({'Min': [''] * 24 + ['0', '16', '21']})
        Max_crel0006 = pd.DataFrame({'Max': [''] * 24 + ['15', '20', '25']})
        duration_crel0006 = Min_crel0006.join(Max_crel0006)

        df_crel0006.insert(0, 'Provider', 'Crelan')
        df_crel0006.insert(1, 'Product_ID', 'CREL0006')
        df_crel0006.insert(2, 'Category', 'Home Loan')
        df_crel0006 = df_crel0006.join(duration_crel0006)  # join newly made df with existed df
        df_crel0006 = df_crel0006[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # CREL0007
        df_crel = read_pdf(new_pdf_crel, encoding='ISO-8859-1',
                           pages=1, pandas_options={'header': None})

        df_crel0007 = df_crel.drop(df_crel.index[0:33]).drop(df_crel.index[36:61])
        df_crel0007 = df_crel0007.drop(df_crel0007.columns[0:2], axis=1).drop(df_crel0007.columns[4:7], axis=1)
        df_crel0007.columns = ["Formulas", "Rates"]
        df_crel0007["Rates"] = df_crel0007["Rates"].str.replace("%", "").str.strip()
        df_crel0007["Rates"] = df_crel0007["Rates"].str.replace(",", ".").str.strip()
        df_crel0007["Formulas"] = "Rates 15/5/5 de >12.500 pour " + df_crel0007["Formulas"].str.replace("â¤", "≤").str.strip()

        Min_crel0007 = pd.DataFrame({'Min': [''] * 33 + ['0', '21', '26']})
        Max_crel0007 = pd.DataFrame({'Max': [''] * 33 + ['20', '25', '30']})
        duration_crel0007 = Min_crel0007.join(Max_crel0007)

        df_crel0007.insert(0, 'Provider', 'Crelan')
        df_crel0007.insert(1, 'Product_ID', 'CREL0007')
        df_crel0007.insert(2, 'Category', 'Home Loan')
        df_crel0007 = df_crel0007.join(duration_crel0007)  # join newly made df with existed df
        df_crel0007 = df_crel0007[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global crel_c
        crel_c = pd.concat([
            pd.concat([df_crel0001], axis=1),
            pd.concat([df_crel0002], axis=1),
            pd.concat([df_crel0003], axis=1),
            pd.concat([df_crel0004], axis=1),
            pd.concat([df_crel0005], axis=1),
            pd.concat([df_crel0006], axis=1),
            pd.concat([df_crel0007], axis=1)
        ])


        print(tabulate(crel_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def crelan_save():
    crelan()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    crel_c.to_csv(os.path.join(path, file_name), index=False)



# #  _______ _                  _       # #
# # (_______) |            _   (_)      # #
# #  _____  | | ____ ____ | |_  _  ___  # #
# # |  ___) | |/ _  |  _ \|  _)| |/___) # #
# # | |_____| ( ( | | | | | |__| |___ | # #
# # |_______)_|\_||_|_| |_|\___)_(___/  # #
# #                                     # #

def elantis():
    
    try:

    # Source
        df_elan_source = read_pdf('https://www.elantis.be/wp/wp-content/uploads/2019/08/tarif-cr%C3%A9dit-hypoth%C3%A9caire-.pdf', encoding='ISO-8859-1', area=[180, 68.64, 301.64, 400], pages=1, pandas_options={'header': None})
        df_elan_source = df_elan_source.drop([2,4,6,8], axis = 1)
    
    # ELAN0001
        df_elan0001 = df_elan_source.drop([3,5,7], axis=1)
        df_elan0001.columns = ["Max", "Rates"]
        df_elan0001["Max"] = df_elan0001['Max'].str.replace('ans','').str.strip()
        df_elan0001.insert(0,'Min',[8,11,16,18,21,23])
        df_elan0001["Rates"] = df_elan0001["Rates"].str.replace('%','').str.strip()
        df_elan0001["Rates"] = df_elan0001["Rates"].str.replace(',','.').str.strip()
        df_elan0001["Rates"] = ((df_elan0001["Rates"].astype(float) / 100) + (0.30 / 100)) * 100
        df_elan0001.insert(0, 'Provider', 'Elantis')
        df_elan0001.insert(1, 'Product_ID', 'ELAN0001')
        df_elan0001.insert(2, 'Category', 'Home Loan')
        df_elan0001.insert(3, 'Formulas', 'Fixed rate')
        df_elan0001 = df_elan0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ELAN0002
        df_elan0002 = df_elan_source.drop([1,3,5], axis=1)
        df_elan0002.columns = ["Max", "Rates"]
        df_elan0002["Max"] = df_elan0002['Max'].str.replace('ans','').str.strip()
        df_elan0002["Rates"] = df_elan0002["Rates"].str.replace('%','').str.strip()
        df_elan0002["Rates"] = df_elan0002["Rates"].str.replace(',','.').str.strip()
        df_elan0002 = df_elan0002[df_elan0002.Rates != '-']
        df_elan0002["Rates"] = ((df_elan0002["Rates"].astype(float) / 100) + (0.30 / 100)) * 100
        df_elan0002.insert(0,'Min',[8,11,16,21])
        df_elan0002.insert(0, 'Provider', 'Elantis')
        df_elan0002.insert(1, 'Product_ID', 'ELAN0002')
        df_elan0002.insert(2, 'Category', 'Home Loan')
        df_elan0002.insert(3, 'Formulas', '3/3/3 CAP2')
        df_elan0002 = df_elan0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ELAN0003
        df_elan0003 = df_elan_source.drop([1,3,7], axis=1)
        df_elan0003.columns = ["Max", "Rates"]
        df_elan0003["Max"] = df_elan0003['Max'].str.replace('ans','').str.strip()
        df_elan0003["Rates"] = df_elan0003["Rates"].str.replace('%','').str.strip()
        df_elan0003["Rates"] = df_elan0003["Rates"].str.replace(',','.').str.strip()
        df_elan0003 = df_elan0003[df_elan0003.Rates != '-']
        df_elan0003["Rates"] = ((df_elan0003["Rates"].astype(float) / 100) + (0.30 / 100)) * 100
        df_elan0003.insert(0,'Min',[8,11,16,21])
        df_elan0003.insert(0, 'Provider', 'Elantis')
        df_elan0003.insert(1, 'Product_ID', 'ELAN0003')
        df_elan0003.insert(2, 'Category', 'Home Loan')
        df_elan0003.insert(3, 'Formulas', '5/5/5 CAP2')
        df_elan0003 = df_elan0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ELAN0004
        df_elan0004 = df_elan_source.drop([1,5,7], axis=1)
        df_elan0004.columns = ["Max", "Rates"]
        df_elan0004["Max"] = df_elan0004['Max'].str.replace('ans','').str.strip()
        df_elan0004["Rates"] = df_elan0004["Rates"].str.replace('%','').str.strip()
        df_elan0004["Rates"] = df_elan0004["Rates"].str.replace(',','.').str.strip()
        df_elan0004 = df_elan0004[df_elan0004.Rates != '-']
        df_elan0004["Rates"] = ((df_elan0004["Rates"].astype(float) / 100) + (0.30 / 100)) * 100
        df_elan0004.insert(0,'Min',[10,16,21])
        df_elan0004.insert(0, 'Provider', 'Elantis')
        df_elan0004.insert(1, 'Product_ID', 'ELAN0004')
        df_elan0004.insert(2, 'Category', 'Home Loan')
        df_elan0004.insert(3, 'Formulas', '10/5/5 CAP2')
        df_elan0004 = df_elan0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global elan_c
        elan_c = pd.concat([
            pd.concat([df_elan0001], axis=1),
            pd.concat([df_elan0002], axis=1),
            pd.concat([df_elan0003], axis=1),
            pd.concat([df_elan0004], axis=1)
        ])
        print(tabulate(elan_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def elan_save():
    elantis()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    elan_c.to_csv(os.path.join(path, file_name), index=False)

# #  _______       _                  _        # #
# # (_______)     | |                | |       # #
# #  _____ ____ _ | | ____  ____ ____| | ____  # #
# # |  ___) _  ) || |/ _  )/ ___) _  | |/ _  ) # #
# # | |  ( (/ ( (_| ( (/ /| |  ( ( | | ( (/ /  # #
# # |_|   \____)____|\____)_|   \_||_|_|\____) # #
# #                                            # #

def federale():

    try:
        
    # FEDE0001
        df_fede_source = read_pdf('https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_4', encoding='ISO-8859-1',
                                  pages=1, pandas_options={'header': None})

        ## Taking rates for >25000
        df_fede0001 = df_fede_source.drop(df_fede_source.index[0:3]).drop(df_fede_source.index[6:22])
        df_fede0001 = df_fede0001.drop(df_fede0001.columns[2:24], axis=1)
        df_fede0001.columns = ["Formulas", "Rates"]
        df_fede0001["Formulas"] = df_fede0001["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0001["Rates"] = df_fede0001["Rates"].str.replace(",", ".").str.strip()
        df_fede0001["Formulas"] = "Rates fixe >25000 de " + df_fede0001["Formulas"].astype(str)  # add prefix to str value in df

        ## Taking rates for <25000
        df_fede0001_2 = df_fede_source.drop(df_fede_source.index[0:3]).drop(df_fede_source.index[6:22])
        df_fede0001_2 = df_fede0001_2.drop(df_fede0001_2.columns[2:24], axis=1)
        df_fede0001_2.columns = ["Formulas", "Rates"]
        df_fede0001_2["Formulas"] = df_fede0001_2["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0001_2["Rates"] = df_fede0001_2["Rates"].str.replace(",", ".").str.strip()
        df_fede0001_2["Formulas"] = "Rates fixe <25000 de " + df_fede0001_2["Formulas"].astype(str)  # add prefix to str value in df

        df_fede0001_2["Rates"] = ((df_fede0001_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        df_fede0001.columns = df_fede0001_2.columns
        data_fede0001 = pd.concat([df_fede0001, df_fede0001_2])

        Min_fede0001 = pd.DataFrame({'Min': [''] * 3 + ['5', '11', '16'] * 2})
        Max_fede0001 = pd.DataFrame({'Max': [''] * 3 + ['10', '15', '20'] * 2})
        duration_fede0001 = Min_fede0001.join(Max_fede0001)

        data_fede0001.insert(0, 'Provider', 'Federale')
        data_fede0001.insert(1, 'Product_ID', 'FEDE0001')
        data_fede0001.insert(2, 'Category', 'Home Loan')
        data_fede0001 = data_fede0001.join(duration_fede0001)  # join newly made df with existed df
        data_fede0001 = data_fede0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # FEDE0002
        df_fede_source = read_pdf('https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_4', encoding='ISO-8859-1',
                                  pages=1, pandas_options={'header': None})

        ## Taking rates for >25000
        df_fede0002 = df_fede_source.drop(df_fede_source.index[0:9]).drop(df_fede_source.index[10:22])
        df_fede0002 = df_fede0002.drop(df_fede0002.columns[2:24], axis=1)
        df_fede0002.columns = ["Formulas", "Rates"]
        df_fede0002["Formulas"] = df_fede0002["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0002["Rates"] = df_fede0002["Rates"].str.replace(",", ".").str.strip()
        df_fede0002["Formulas"] = "Rates >25000 15/5 +2-2 de " + df_fede0002["Formulas"].astype(str)  # add prefix to str value in df

        ## Taking rates for <25000
        df_fede0002_2 = df_fede_source.drop(df_fede_source.index[0:9]).drop(df_fede_source.index[10:22])
        df_fede0002_2 = df_fede0002_2.drop(df_fede0002_2.columns[2:24], axis=1)
        df_fede0002_2.columns = ["Formulas", "Rates"]
        df_fede0002_2["Formulas"] = df_fede0002_2["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0002_2["Rates"] = df_fede0002_2["Rates"].str.replace(",", ".").str.strip()
        df_fede0002_2["Formulas"] = "Rates < 25000 15/5 +2-2 de " + df_fede0002_2["Formulas"].astype(str)  # add prefix to str value in df

        df_fede0002_2["Rates"] = ((df_fede0002_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        df_fede0002.columns = df_fede0002_2.columns
        data_fede0002 = pd.concat([df_fede0002, df_fede0002_2])

        Min_fede0002 = pd.DataFrame({'Min': [''] * 9 + ['15'] * 2})
        Max_fede0002 = pd.DataFrame({'Max': [''] * 9 + ['30'] * 2})
        duration_fede0002 = Min_fede0002.join(Max_fede0002)

        data_fede0002.insert(0, 'Provider', 'Federale')
        data_fede0002.insert(1, 'Product_ID', 'FEDE0002')
        data_fede0002.insert(2, 'Category', 'Home Loan')
        data_fede0002 = data_fede0002.join(duration_fede0002)  # join newly made df with existed df
        data_fede0002 = data_fede0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # FEDE0003
        df_fede_source = read_pdf('https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_4', encoding='ISO-8859-1',
                                  pages=1, pandas_options={'header': None})

        # Taking rates for >25000
        df_fede0003 = df_fede_source.drop(df_fede_source.index[0:13]).drop(df_fede_source.index[14:22])
        df_fede0003 = df_fede0003.drop(df_fede0003.columns[2:24], axis=1)
        df_fede0003.columns = ["Formulas", "Rates"]
        df_fede0003["Formulas"] = df_fede0003["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0003["Rates"] = df_fede0003["Rates"].str.replace(",", ".").str.strip()
        df_fede0003["Formulas"] = "Rates >25000 10/5 +2-2 de " + df_fede0003["Formulas"].astype(str)  # add prefix to str value in df

        ## Taking rates for <25000
        df_fede0003_2 = df_fede_source.drop(df_fede_source.index[0:13]).drop(df_fede_source.index[14:22])
        df_fede0003_2 = df_fede0003_2.drop(df_fede0003_2.columns[2:24], axis=1)
        df_fede0003_2.columns = ["Formulas", "Rates"]
        df_fede0003_2["Formulas"] = df_fede0003_2["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0003_2["Rates"] = df_fede0003_2["Rates"].str.replace(",", ".").str.strip()
        df_fede0003_2["Formulas"] = "Rates < 25000 10/5 +2-2 de " + df_fede0003_2["Formulas"].astype(str)  # add prefix to str value in df

        df_fede0003_2["Rates"] = ((df_fede0003_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        df_fede0003.columns = df_fede0003_2.columns
        data_fede0003 = pd.concat([df_fede0003, df_fede0003_2])

        Min_fede0003 = pd.DataFrame({'Min': [''] * 13 + ['10'] * 2})
        Max_fede0003 = pd.DataFrame({'Max': [''] * 13 + ['30'] * 2})
        duration_fede0003 = Min_fede0003.join(Max_fede0003)

        data_fede0003.insert(0, 'Provider', 'Federale')
        data_fede0003.insert(1, 'Product_ID', 'FEDE0003')
        data_fede0003.insert(2, 'Category', 'Home Loan')
        data_fede0003 = data_fede0003.join(duration_fede0003)  # join newly made df with existed df
        data_fede0003 = data_fede0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # FEDE0004
        df_fede_source = read_pdf('https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_4', encoding='ISO-8859-1',
                                  pages=1, pandas_options={'header': None})

        # Taking rates for >25000
        df_fede0004 = df_fede_source.drop(df_fede_source.index[0:17]).drop(df_fede_source.index[18:22])
        df_fede0004 = df_fede0004.drop(df_fede0004.columns[2:24], axis=1)
        df_fede0004.columns = ["Formulas", "Rates"]
        df_fede0004["Formulas"] = df_fede0004["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0004["Rates"] = df_fede0004["Rates"].str.replace(",", ".").str.strip()
        df_fede0004["Formulas"] = "Rates >25000 5/5 +2-2 de " + df_fede0004["Formulas"].astype(str)  # add prefix to str value in df

        ## Taking rates for <25000
        df_fede0004_2 = df_fede_source.drop(df_fede_source.index[0:17]).drop(df_fede_source.index[18:22])
        df_fede0004_2 = df_fede0004_2.drop(df_fede0004_2.columns[2:24], axis=1)
        df_fede0004_2.columns = ["Formulas", "Rates"]
        df_fede0004_2["Formulas"] = df_fede0004_2["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0004_2["Rates"] = df_fede0004_2["Rates"].str.replace(",", ".").str.strip()
        df_fede0004_2["Formulas"] = "Rates < 25000 5/5 +2-2 de " + df_fede0004_2["Formulas"].astype(str)  # add prefix to str value in df

        df_fede0004_2["Rates"] = ((df_fede0004_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        df_fede0004.columns = df_fede0004_2.columns
        data_fede0004 = pd.concat([df_fede0004, df_fede0004_2])

        Min_fede0004 = pd.DataFrame({'Min': [''] * 17 + ['5'] * 2})
        Max_fede0004 = pd.DataFrame({'Max': [''] * 17 + ['30'] * 2})
        duration_fede0004 = Min_fede0004.join(Max_fede0004)

        data_fede0004.insert(0, 'Provider', 'Federale')
        data_fede0004.insert(1, 'Product_ID', 'FEDE0004')
        data_fede0004.insert(2, 'Category', 'Home Loan')
        data_fede0004 = data_fede0004.join(duration_fede0004)  # join newly made df with existed df
        data_fede0004 = data_fede0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns
 
    # FEDE0005
        df_fede_source = read_pdf('https://www.federale.be/docs/default-source/default-document-library/particulieren-particuliers/tarif-ch-30-01-2019.pdf?sfvrsn=9f4b78d7_4', encoding='ISO-8859-1',
                                  pages=1, pandas_options={'header': None})

        # Taking rates for >25000
        df_fede0005 = df_fede_source.drop(df_fede_source.index[0:21])
        df_fede0005 = df_fede0005.drop(df_fede0005.columns[2:24], axis=1)
        df_fede0005.columns = ["Formulas", "Rates"]
        df_fede0005["Formulas"] = df_fede0005["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0005["Rates"] = df_fede0005["Rates"].str.replace(",", ".").str.strip()
        df_fede0005["Formulas"] = "Rates >25000 1/1 +3-3 de " + df_fede0005["Formulas"].astype(str)  # add prefix to str value in df

        ## Taking rates for <25000
        df_fede0005_2 = df_fede_source.drop(df_fede_source.index[0:21])
        df_fede0005_2 = df_fede0005_2.drop(df_fede0005_2.columns[2:24], axis=1)
        df_fede0005_2.columns = ["Formulas", "Rates"]
        df_fede0005_2["Formulas"] = df_fede0005_2["Formulas"].str.replace(" â¤", "≤").str.strip()
        df_fede0005_2["Rates"] = df_fede0005_2["Rates"].str.replace(",", ".").str.strip()
        df_fede0005_2["Formulas"] = "Rates < 25000 1/1 +3-3 de " + df_fede0005_2["Formulas"].astype(str)  # add prefix to str value in df

        df_fede0005_2["Rates"] = ((df_fede0005_2["Rates"].astype(float) / 100) + (0.5 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        df_fede0005.columns = df_fede0005_2.columns
        data_fede0005 = pd.concat([df_fede0005, df_fede0005_2])

        Min_fede0005 = pd.DataFrame({'Min': [''] * 21 + ['5'] * 2})
        Max_fede0005 = pd.DataFrame({'Max': [''] * 21 + ['30'] * 2})
        duration_fede0005 = Min_fede0005.join(Max_fede0005)

        data_fede0005.insert(0, 'Provider', 'Federale')
        data_fede0005.insert(1, 'Product_ID', 'FEDE0005')
        data_fede0005.insert(2, 'Category', 'Home Loan')
        data_fede0005 = data_fede0005.join(duration_fede0005)  # join newly made df with existed df
        data_fede0005 = data_fede0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global fede_c
        fede_c = pd.concat([
            pd.concat([data_fede0001], axis=1),
            pd.concat([data_fede0002], axis=1),
            pd.concat([data_fede0003], axis=1),
            pd.concat([data_fede0004], axis=1),
            pd.concat([data_fede0005], axis=1)
        ])

        print(tabulate(fede_c, headers='keys', tablefmt='psql', showindex="never"))
   
    except:
        pass

def federale_save():
    federale()

    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    fede_c.to_csv(os.path.join(path, file_name), index=False)


# #  _     _       _ _       _                 _      # #
# # | |   | |     | | |     | |               | |     # #
# # | |__ | | ____| | | ___ | | _   ____ ____ | |  _  # #
# # |  __)| |/ _  ) | |/ _ \| || \ / _  |  _ \| | / ) # #
# # | |   | ( (/ /| | | |_| | |_) | ( | | | | | |< (  # #
# # |_|   |_|\____)_|_|\___/|____/ \_||_|_| |_|_| \_) # #
# #                                                   # #

def hellobank():

    try:
        
    # HBNK0001
        df_hbnk0001 = read_pdf('https://www.hellobank.be/docs/default-source/Products/h10061/fr-a.pdf', encoding='ISO-8859-1', area=[297.36, 66.96, 454.32, 540], pages=1, pandas_options={'header': None})

        df_hbnk0001 = df_hbnk0001.drop([2,3], axis=1)  # Dropping all the unintended columns
        df_hbnk0001.columns = ["Max",'Rates']
        df_hbnk0001["Max"] = df_hbnk0001["Max"].str.replace('ans fixe', '').str.strip()  # split the element within a table
        df_hbnk0001.insert(0,"Min", df_hbnk0001['Max'])
        df_hbnk0001["Rates"] = df_hbnk0001["Rates"].str.replace("%", "").str.strip()
        df_hbnk0001["Rates"] = df_hbnk0001["Rates"].str.replace(",", ".").str.strip()

        df_hbnk0001.insert(0, 'Provider', 'Hello Bank')
        df_hbnk0001.insert(1, 'Product_ID', 'HBNK0001')
        df_hbnk0001.insert(2, 'Category', 'Home Loan')
        df_hbnk0001.insert(3, 'Formulas', 'Fixed rate')
        df_hbnk0001 = df_hbnk0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns
        
    # Concatenate
        global hbnk_c
        hbnk_c = df_hbnk0001
        print(tabulate(df_hbnk0001, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def hellobank_save():
    hellobank()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    hbnk_c.to_csv(os.path.join(path, file_name), index=False)

# #  _____ ______   ______  # #
# # (_____)  ___ \ / _____) # #
# #    _  | |   | | /  ___  # #
# #   | | | |   | | | (___) # #
# #  _| |_| |   | | \____/| # #
# # (_____)_|   |_|\_____/  # #
# #                         # #

def ing():

    try:
        df_ing = read_pdf('https://www.ing.be/static/legacy/SiteCollectionDocuments/Bareme_CH_FR.pdf', encoding='ISO-8859-1', pages=1, area=[123.28, 16.25, 502.15, 827.29], pandas_options={'header': None})

    # ING0001
        df_ingx0001 = df_ing.drop(df_ing.index[0:3]).drop(df_ing.index[9:38])
        df_ingx0001 = df_ingx0001.drop(df_ingx0001.columns[1:7], axis=1).drop(df_ingx0001.columns[8:16], axis=1)
        df_ingx0001.columns = ["Formulas", "Rates"]
        df_ingx0001["Rates"] = df_ingx0001["Rates"].str.replace(" %", "").str.strip()
        df_ingx0001["Rates"] = df_ingx0001["Rates"].str.replace(",", ".").str.strip()

        Min_ingx0001 = pd.DataFrame({'Min': [''] * 3 + ['0', '6', '11', '16', '21', '25']})
        Max_ingx0001 = pd.DataFrame({'Max': [''] * 3 + ['5', '10', '15', '20', '25', '30']})
        duration_ingx0001 = Min_ingx0001.join(Max_ingx0001)

        df_ingx0001.insert(0, 'Provider', 'ING')
        df_ingx0001.insert(1, 'Product_ID', 'INGX0001')
        df_ingx0001.insert(2, 'Category', 'Home Loan')
        df_ingx0001 = df_ingx0001.join(duration_ingx0001)  # join newly made df with existed df
        df_ingx0001 = df_ingx0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ING0002

        df_ingx0002 = df_ing.drop(df_ing.index[0:11]).drop(df_ing.index[17:38])
        df_ingx0002 = df_ingx0002.drop(df_ingx0002.columns[0:7], axis=1).drop(df_ingx0002.columns[8:16], axis=1)
        df_ingx0002.columns = ["Rates"]
        df_ingx0002["Rates"] = df_ingx0002["Rates"].str.replace(" %", "").str.strip()
        df_ingx0002["Rates"] = df_ingx0002["Rates"].str.replace(",", ".").str.strip()

        Min_ingx0002 = pd.DataFrame({'Min': [''] * 11 + ['0', '6', '11', '16', '21', '25']})
        Max_ingx0002 = pd.DataFrame({'Max': [''] * 11 + ['5', '10', '15', '20', '25', '30']})
        duration_ingx0002 = Min_ingx0002.join(Max_ingx0002)

        df_ingx0002.insert(0, 'Provider', 'ING')
        df_ingx0002.insert(1, 'Product_ID', 'INGX0002')
        df_ingx0002.insert(2, 'Category', 'Home Loan')
        df_ingx0002.insert(3, 'Formulas', 'Formule 1+1+1 (+3,00%/--%)')
        df_ingx0002 = df_ingx0002.join(duration_ingx0002)  # join newly made df with existed df
        df_ingx0002 = df_ingx0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ING0003

        df_ingx0003 = df_ing.drop(df_ing.index[0:18]).drop(df_ing.index[23:38])
        df_ingx0003 = df_ingx0003.drop(df_ingx0003.columns[0:7], axis=1).drop(df_ingx0003.columns[8:16], axis=1)
        df_ingx0003.columns = ["Rates"]
        df_ingx0003["Rates"] = df_ingx0003["Rates"].str.replace(" %", "").str.strip()
        df_ingx0003["Rates"] = df_ingx0003["Rates"].str.replace(",", ".").str.strip()

        Min_ingx0003 = pd.DataFrame({'Min': [''] * 18 + ['0', '11', '16', '21', '25']})
        Max_ingx0003 = pd.DataFrame({'Max': [''] * 18 + ['10', '15', '20', '25', '30']})
        duration_ingx0003 = Min_ingx0003.join(Max_ingx0003)

        df_ingx0003.insert(0, 'Provider', 'ING')
        df_ingx0003.insert(1, 'Product_ID', 'INGX0003')
        df_ingx0003.insert(2, 'Category', 'Home Loan')
        df_ingx0003.insert(3, 'Formulas', 'Formule 5+5+5 (+5,00%/-5,00%)')
        df_ingx0003 = df_ingx0003.join(duration_ingx0003)  # join newly made df with existed df
        df_ingx0003 = df_ingx0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ING0004

        df_ingx0004 = df_ing.drop(df_ing.index[0:24]).drop(df_ing.index[28:38])
        df_ingx0004 = df_ingx0004.drop(df_ingx0004.columns[0:7], axis=1).drop(df_ingx0004.columns[8:16], axis=1)
        df_ingx0004.columns = ["Rates"]
        df_ingx0004["Rates"] = df_ingx0004["Rates"].str.replace(" %", "").str.strip()
        df_ingx0004["Rates"] = df_ingx0004["Rates"].str.replace(",", ".").str.strip()

        Min_ingx0004 = pd.DataFrame({'Min': [''] * 24 + ['0', '16', '21', '25']})
        Max_ingx0004 = pd.DataFrame({'Max': [''] * 24 + ['15', '20', '25', '30']})
        duration_ingx0004 = Min_ingx0004.join(Max_ingx0004)

        df_ingx0004.insert(0, 'Provider', 'ING')
        df_ingx0004.insert(1, 'Product_ID', 'INGX0004')
        df_ingx0004.insert(2, 'Category', 'Home Loan')
        df_ingx0004.insert(3, 'Formulas', 'Formule 10+5+5 (+5,00%/-5,00%)')
        df_ingx0004 = df_ingx0004.join(duration_ingx0004)  # join newly made df with existed df
        df_ingx0004 = df_ingx0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # ING0005

        df_ingx0005 = df_ing.drop(df_ing.index[0:29]).drop(df_ing.index[33:38])
        df_ingx0005 = df_ingx0005.drop(df_ingx0005.columns[0:7], axis=1).drop(df_ingx0005.columns[8:16], axis=1)
        df_ingx0005.columns = ["Rates"]
        df_ingx0005["Rates"] = df_ingx0005["Rates"].str.replace(" %", "").str.strip()
        df_ingx0005["Rates"] = df_ingx0005["Rates"].str.replace(",", ".").str.strip()

        Min_ingx0005 = pd.DataFrame({'Min': [''] * 29 + ['0', '16', '21', '25']})
        Max_ingx0005 = pd.DataFrame({'Max': [''] * 29 + ['15', '20', '25', '30']})
        duration_ingx0005 = Min_ingx0005.join(Max_ingx0005)

        df_ingx0005.insert(0, 'Provider', 'ING')
        df_ingx0005.insert(1, 'Product_ID', 'INGX0005')
        df_ingx0005.insert(2, 'Category', 'Home Loan')
        df_ingx0005.insert(2, 'Formulas', 'Formule 10+5+5 (+2,00%/--%)')
        df_ingx0005 = df_ingx0005.join(duration_ingx0005)  # join newly made df with existed df
        df_ingx0005 = df_ingx0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global ingx_c
        ingx_c = pd.concat([
            pd.concat([df_ingx0001], axis=1),
            pd.concat([df_ingx0002], axis=1),
            pd.concat([df_ingx0003], axis=1),
            pd.concat([df_ingx0004], axis=1),
            pd.concat([df_ingx0005], axis=1)
        ])

        print(tabulate(ingx_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def ing_save():
    ing()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    ingx_c.to_csv(os.path.join(path, file_name), index=False)

# #  _    _ ______   ______  # #
# # | |  / |____  \ / _____) # #
# # | | / / ____)  ) /       # #
# # | |< < |  __  (| |       # #
# # | | \ \| |__)  ) \_____  # #
# # |_|  \_)______/ \______) # #
# #                          # #

def kbc():

    try:
    
    # Sources
        df_kbcx_source1 = read_pdf('https://multimediafiles.kbcgroup.eu/ng/published/KBC/PDF/WONEN/kbc-woningkrediet-tarievenkaart.pdf', encoding='ISO-8859-1',
                                      area=[235.44, 27.36, 293.04, 814.32], pages=1, pandas_options={'header': None})
        df_kbcx_source1 = df_kbcx_source1.drop([2,3,4,7,8,9,12,13,14],axis = 1)
        df_kbcx_source2 = read_pdf('https://multimediafiles.kbcgroup.eu/ng/published/KBC/PDF/WONEN/kbc-woningkrediet-tarievenkaart.pdf', encoding='ISO-8859-1',
                                      area=[205.92, 840.24, 277.92, 1128.24], pages=1, pandas_options={'header': None})

    # KBC0001
        ## Rate for >25000
        df_kbcx0001_1 = df_kbcx_source1.drop([5,6,10,11],axis=1)
        df_kbcx0001_1.columns = ["Max", "Rates"]
        df_kbcx0001_1.insert(0, "Formulas", "1/1/1 > 25000")
        df_kbcx0001_1["Max"] = df_kbcx0001_1["Max"].str.replace("j", "").str.strip()
        df_kbcx0001_1["Max"] = df_kbcx0001_1["Max"].str.replace("<=", "").str.strip()
        df_kbcx0001_1["Rates"] = df_kbcx0001_1["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0001_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_kbcx0001_2 = df_kbcx_source1.drop([5,6,10,11],axis=1)
        df_kbcx0001_2.columns = ["Max", "Rates"]
        df_kbcx0001_2.insert(0, "Formulas", "1/1/1 < 25000")
        df_kbcx0001_2["Max"] = df_kbcx0001_2["Max"].str.replace("j", "").str.strip()
        df_kbcx0001_2["Max"] = df_kbcx0001_2["Max"].str.replace("<=", "").str.strip()
        df_kbcx0001_2["Rates"] = df_kbcx0001_2["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0001_2.insert(1, 'Min', [0,11,16,21])
        df_kbcx0001_2["Rates"] = ((df_kbcx0001_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_kbcx0001 = pd.concat([df_kbcx0001_1, df_kbcx0001_2])
        data_kbcx0001.insert(0, 'Provider', 'KBC')
        data_kbcx0001.insert(1, 'Product_ID', 'KBC0001')
        data_kbcx0001.insert(2, 'Category', 'Home Loan')
        data_kbcx0001 = data_kbcx0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # KBC0002
        ## Rate for >25000
        df_kbcx0002_1 = df_kbcx_source1.drop([0,1,10,11],axis=1)
        df_kbcx0002_1.columns = ["Max", "Rates"]
        df_kbcx0002_1.insert(0, "Formulas", "3/3/3 > 25000")
        df_kbcx0002_1["Max"] = df_kbcx0002_1["Max"].str.replace("j", "").str.strip()
        df_kbcx0002_1["Max"] = df_kbcx0002_1["Max"].str.replace("<=", "").str.strip()
        df_kbcx0002_1["Rates"] = df_kbcx0002_1["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0002_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_kbcx0002_2 = df_kbcx_source1.drop([0,1,10,11],axis=1)
        df_kbcx0002_2.columns = ["Max", "Rates"]
        df_kbcx0002_2.insert(0, "Formulas", "3/3/3 < 25000")
        df_kbcx0002_2["Max"] = df_kbcx0002_2["Max"].str.replace("j", "").str.strip()
        df_kbcx0002_2["Max"] = df_kbcx0002_2["Max"].str.replace("<=", "").str.strip()
        df_kbcx0002_2["Rates"] = df_kbcx0002_2["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0002_2.insert(1, 'Min', [0,11,16,21])
        df_kbcx0002_2["Rates"] = ((df_kbcx0002_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_kbcx0002 = pd.concat([df_kbcx0002_1, df_kbcx0002_2])
        data_kbcx0002.insert(0, 'Provider', 'KBC')
        data_kbcx0002.insert(1, 'Product_ID', 'KBC0002')
        data_kbcx0002.insert(2, 'Category', 'Home Loan')
        data_kbcx0002 = data_kbcx0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # KBC0003
        ## Rate for >25000
        df_kbcx0003_1 = df_kbcx_source1.drop([0,1,5,6],axis=1)
        df_kbcx0003_1.columns = ["Max", "Rates"]
        df_kbcx0003_1.insert(0, "Formulas", "5/5/5 > 25000")
        df_kbcx0003_1["Max"] = df_kbcx0003_1["Max"].str.replace("j", "").str.strip()
        df_kbcx0003_1["Max"] = df_kbcx0003_1["Max"].str.replace("<=", "").str.strip()
        df_kbcx0003_1["Rates"] = df_kbcx0003_1["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0003_1.insert(1, 'Min', [0,11,16,21])

        ## Rate for <25000
        df_kbcx0003_2 = df_kbcx_source1.drop([0,1,5,6],axis=1)
        df_kbcx0003_2.columns = ["Max", "Rates"]
        df_kbcx0003_2.insert(0, "Formulas", "5/5/5 < 25000")
        df_kbcx0003_2["Max"] = df_kbcx0003_2["Max"].str.replace("j", "").str.strip()
        df_kbcx0003_2["Max"] = df_kbcx0003_2["Max"].str.replace("<=", "").str.strip()
        df_kbcx0003_2["Rates"] = df_kbcx0003_2["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0003_2.insert(1, 'Min', [0,11,16,21])
        df_kbcx0003_2["Rates"] = ((df_kbcx0003_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        # Concatenate rates for >25000 and <25000
        data_kbcx0003 = pd.concat([df_kbcx0003_1, df_kbcx0003_2])
        data_kbcx0003.insert(0, 'Provider', 'KBC')
        data_kbcx0003.insert(1, 'Product_ID', 'KBC0003')
        data_kbcx0003.insert(2, 'Category', 'Home Loan')
        data_kbcx0003 = data_kbcx0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns
 
    # KBC0004
        ## Rate for >25000
        df_kbcx0004_1 = df_kbcx_source2.drop([2,3,4], axis = 1)
        df_kbcx0004_1.columns = ['Duration', 'Rates']
        temp = df_kbcx0004_1['Duration'].str.split('<=', 1).str  # split the element within a table
        Min = temp[0]
        Max = temp[1]
        df_kbcx0004_1.insert(1,'Min',Min)
        df_kbcx0004_1.insert(2,'Max',Max)
        df_kbcx0004_1["Min"] = df_kbcx0004_1["Min"].str.replace(">", "").str.strip()
        df_kbcx0004_1["Min"] = df_kbcx0004_1["Min"].str.replace("en", "").str.strip()
        df_kbcx0004_1["Max"] = df_kbcx0004_1["Max"].str.replace("jaar", "").str.strip()
        df_kbcx0004_1.insert(0, "Formulas", "Fixed rate > 25000")
        df_kbcx0004_1["Rates"] = df_kbcx0004_1["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0004_1.drop('Duration', axis=1, inplace = True)

        ## Rate for <25000
        df_kbcx0004_2 = df_kbcx_source2.drop([2,3,4], axis = 1)
        df_kbcx0004_2.columns = ['Duration', 'Rates']
        temp = df_kbcx0004_2['Duration'].str.split('<=', 1).str  # split the element within a table
        Min = temp[0]
        Max = temp[1]
        df_kbcx0004_2.insert(1,'Min',Min)
        df_kbcx0004_2.insert(2,'Max',Max)
        df_kbcx0004_2["Min"] = df_kbcx0004_2["Min"].str.replace(">", "").str.strip()
        df_kbcx0004_2["Min"] = df_kbcx0004_2["Min"].str.replace("en", "").str.strip()
        df_kbcx0004_2["Max"] = df_kbcx0004_2["Max"].str.replace("jaar", "").str.strip()
        df_kbcx0004_2.insert(0, "Formulas", "Fixed rate < 25000")
        df_kbcx0004_2["Rates"] = df_kbcx0004_2["Rates"].str.replace(",", ".").str.strip()
        df_kbcx0004_2.drop('Duration', axis=1, inplace = True)

        df_kbcx0004_2["Rates"] = ((df_kbcx0004_2["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        ##Concatenate rates for >25000 and <25000
        df_kbcx0004_1.columns = df_kbcx0004_2.columns
        data_kbcx0004 = pd.concat([df_kbcx0004_1, df_kbcx0004_2])

        data_kbcx0004.insert(0, 'Provider', 'KBC')
        data_kbcx0004.insert(1, 'Product_ID', 'KBC0004')
        data_kbcx0004.insert(2, 'Category', 'Home Loan')
        data_kbcx0004 = data_kbcx0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global kbcx_c
        kbcx_c = pd.concat([
            pd.concat([data_kbcx0001], axis=1),
            pd.concat([data_kbcx0002], axis=1),
            pd.concat([data_kbcx0003], axis=1),
            pd.concat([data_kbcx0004], axis=1)
        ])

        print(tabulate(kbcx_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def kbc_save():
    kbc()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    kbcx_c.to_csv(os.path.join(path, file_name), index=False)

# #  _    _                                _        # #
# # | |  / )           _                  | |       # #
# # | | / / ____ _   _| |_   ____ ____  _ | | ____  # #
# # | |< < / _  ) | | |  _) / ___) _  |/ || |/ _  ) # #
# # | | \ ( (/ /| |_| | |__| |  ( ( | ( (_| ( (/ /  # #
# # |_|  \_)____)\__  |\___)_|   \_||_|\____|\____) # #
# #             (____/                              # #

def keytrade():

    try:

    # KEYT0001
        df_keyt0001 = read_pdf('https://www.keytradebank.be/node/backend/v1/keyhome/tariffsheet?language=fr', encoding='ISO-8859-1',
                               pages=1, pandas_options={'header': None})
        df_keyt0001 = df_keyt0001.drop(df_keyt0001.index[0:5])
        df_keyt0001 = df_keyt0001.drop(df_keyt0001.columns[1:3], axis=1).drop(df_keyt0001.columns[4], axis=1)
        df_keyt0001.columns = ["Formulas", "_Taux_"]
        df_keyt0001["_Maandelijks_"], df_keyt0001["Rates"] = df_keyt0001["_Taux_"].str.split('% ', 1).str  # split the element within a table
        df_keyt0001.drop('_Maandelijks_', axis=1, inplace=True)
        df_keyt0001.drop('_Taux_', axis=1, inplace=True)
        df_keyt0001["Rates"] = df_keyt0001["Rates"].str.replace("%", "").str.strip()
        df_keyt0001["Rates"] = df_keyt0001["Rates"].str.replace(",", ".").str.strip()

        Min_keyt0001 = pd.DataFrame({'Min': [''] * 5 + ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']})
        Max_keyt0001 = pd.DataFrame({'Max': [''] * 5 + ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']})
        duration_keyt0001 = Min_keyt0001.join(Max_keyt0001)

        df_keyt0001.insert(0, 'Provider', 'Keytrade')
        df_keyt0001.insert(1, 'Product_ID', 'KEYT0001')
        df_keyt0001.insert(2, 'Category', 'Home Loan')
        df_keyt0001 = df_keyt0001.join(duration_keyt0001)  # join newly made df with existed df
        df_keyt0001 = df_keyt0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    #Concatenate
        global keyt_c
        keyt_c = df_keyt0001

        print(tabulate(keyt_c, headers='keys', tablefmt='psql', showindex="never"))
        # df_keyt0001.to_csv(os.path.join(path, "today_results.csv"))
    
    except:
        pass

def keytrade_save():
    keytrade()
    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'
    keyt_c.to_csv(os.path.join(path, file_name), index=False)


# #  ______                    _                   _               # #
# # |  ___ \                  | |                 | |              # #
# # | |   | | ____  ____  ____| |____   ____  ____| |  _  ____ ___ # #
# # | |   | |/ _  |/ _  |/ _  ) |    \ / _  |/ ___) | / )/ ___)___)# #
# # | |   | ( ( | ( ( | ( (/ /| | | | ( ( | ( (___| |< (| |  |___ |# #
# # |_|   |_|\_||_|\_|| |\____)_|_|_|_|\_||_|\____)_| \_)_|  (___/ # #
# #               (_____|                                          # #

def nage():

    try:
        url_nege = 'https://www.nagelmackers.be/src/Frontend/Files/userfiles/files/Liste_des_tarifs_credits_logements.pdf'
        response_nege = requests.get(url_nege)

    # NAGE0001
        with io.BytesIO(response_nege.content) as open_pdf_file:
            read_pdf_nege = PyPDF2.PdfFileReader(open_pdf_file)
            page_nege = read_pdf_nege.getPage(0)
            page_content_nege = page_nege.extractText()
            page_content_nege = page_content_nege.encode('utf-8')

        html = page_content_nege.decode('ISO-8859-1') #decode because our regex is a string, but html is bytes
        line = re.sub('.xc3.', '', html)
        line_2 = re.sub('.xa9.', '', line)

        for _ in line_2:
            taux_nage0001 = re.findall(r'10 ans(.*?)1.2', line_2)
            taux_nage0001_1_fix = [i.split('%', 1)[0] for i in taux_nage0001]
            taux_nage0001_2 = [i.split('%', 1)[1] for i in taux_nage0001]
            taux_nage0001_2b = [i.split('%', 1)[1] for i in taux_nage0001_2]
            taux_nage0001_2b_fix = [i.split('%', 1)[0] for i in taux_nage0001_2b]
            taux_nage0001_3 = [i.split('%', 1)[1] for i in taux_nage0001_2b]
            taux_nage0001_3b = [i.split('ans', 1)[1] for i in taux_nage0001_3]
            taux_nage0001_3b_fix = [i.split('%', 1)[0] for i in taux_nage0001_3b]
            taux_nage0001_4 = [i.split('%', 1)[1] for i in taux_nage0001_3b]
            taux_nage0001_4_fix = [s.strip('%') for s in taux_nage0001_4]  # removing '%' sign
        taux_nage0001 = taux_nage0001_1_fix + taux_nage0001_2b_fix + taux_nage0001_3b_fix + taux_nage0001_4_fix
        taux_nage0001 = pd.DataFrame({'Rates': taux_nage0001})  # convert list into panda df
        formules_nage0001 = pd.DataFrame({'Formulas': ['Rates fixe de 10ans', 'Rates fixe de 15ans', 'Rates fixe de 20ans', 'Rates fixe de 25ans']})
        Min_nage0001 = pd.DataFrame({'Min': ['0', '11', '16', '21']})
        Max_nage0001 = pd.DataFrame({'Max': ['10', '15', '20', '25']})
        duration_nage0001 = Min_nage0001.join(Max_nage0001)

        df_nage0001 = taux_nage0001.join(formules_nage0001).join(duration_nage0001)
        df_nage0001["Rates"] = df_nage0001["Rates"].str.replace(",", ".").str.strip()
        df_nage0001["Rates"] = ((df_nage0001["Rates"].astype(float) / 100) + (0.30 / 100)) * 100

        df_nage0001.insert(0, 'Provider', 'Nagelmackers')
        df_nage0001.insert(1, 'Product_ID', 'NA0001')
        df_nage0001.insert(2, 'Category', 'Home Loan')
        df_nage0001 = df_nage0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # NAGE0002

        with io.BytesIO(response_nege.content) as open_pdf_file:
            read_pdf_nege = PyPDF2.PdfFileReader(open_pdf_file)
            #num_pages_nege = read_pdf_nege.getNumPages()
            page_nege = read_pdf_nege.getPage(0)
            page_content_nege = page_nege.extractText()
            page_content_nege = page_content_nege.encode('utf-8')

        html = page_content_nege.decode('ISO-8859-1') #decode because our regex is a string, but html is bytes
        line = re.sub('.xc3.', '', html)
        line_2 = re.sub('.xa9.', '', line)

        for _ in line_2:
            #bank_nage = ['Nagelmackers']
            taux_nage0002 = re.findall(r'.2.(.*?)1.3.', line_2)
            taux_nage0002_1 = [i.split('%', 1)[0] for i in taux_nage0002]
        taux_nage0002 = pd.DataFrame({'Rates':taux_nage0002_1})

        formules_nage0002 = pd.DataFrame({'Formulas': ['3/3/3 Cap +5/-5']})
        Min_nage0002 = pd.DataFrame({'Min': ['']})
        Max_nage0002 = pd.DataFrame({'Max': ['']})
        duration_nage0002 = Min_nage0002.join(Max_nage0002)

        df_nage0002 = taux_nage0002.join(formules_nage0002).join(duration_nage0002)
        df_nage0002["Rates"] = df_nage0002["Rates"].str.replace(",", ".").str.strip()
        df_nage0002["Rates"] = ((df_nage0002["Rates"].astype(float) / 100) + (0.30 / 100)) * 100

        df_nage0002.insert(0, 'Provider', 'Nagelmackers')
        df_nage0002.insert(1, 'Product_ID', 'NA0002')
        df_nage0002.insert(2, 'Category', 'Home Loan')
        df_nage0002 = df_nage0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # NAGE0003

        with io.BytesIO(response_nege.content) as open_pdf_file:
            read_pdf_nege = PyPDF2.PdfFileReader(open_pdf_file)
            #num_pages_nege = read_pdf_nege.getNumPages()
            page_nege = read_pdf_nege.getPage(0)
            page_content_nege = page_nege.extractText()
            page_content_nege = page_content_nege.encode('utf-8')

        html = page_content_nege.decode('ISO-8859-1') #decode because our regex is a string, but html is bytes
        line = re.sub('.xc3.', '', html)
        line_2 = re.sub('.xa9.', '', line)

        for _ in line_2:
            #bank_nage = ['Nagelmackers']
            taux_nage0003 = re.findall(r'.2.(.*?)1.3.', line_2)
            taux_nage0003_1 = [i.split('(2)', 1)[1] for i in taux_nage0003]
            taux_nage0003_1_fix = [i.split('(2)', 1)[0] for i in taux_nage0003_1]
            taux_nage0003_1_fix = [s.strip('%') for s in taux_nage0003_1_fix]  # removing '%' sign
        taux_nage0003 = pd.DataFrame({'Rates': taux_nage0003_1_fix})

        formules_nage0003 = pd.DataFrame({'Formulas': ['5/5/5 Cap +5/-5']})
        Min_nage0003 = pd.DataFrame({'Min': ['']})
        Max_nage0003 = pd.DataFrame({'Max': ['']})
        duration_nage0003 = Min_nage0003.join(Max_nage0003)

        df_nage0003 = taux_nage0003.join(formules_nage0003).join(duration_nage0003)
        df_nage0003["Rates"] = df_nage0003["Rates"].str.replace(",", ".").str.strip()
        df_nage0003["Rates"] = ((df_nage0003["Rates"].astype(float) / 100) + (0.30 / 100)) * 100

        df_nage0003.insert(0, 'Provider', 'Nagelmackers')
        df_nage0003.insert(1, 'Product_ID', 'NA0003')
        df_nage0003.insert(2, 'Category', 'Home Loan')
        df_nage0003 = df_nage0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # NAGE0004
    # not able to find the right taux value for NAGE0004 ---- constant based is applied

        with io.BytesIO(response_nege.content) as open_pdf_file:
            read_pdf_nege = PyPDF2.PdfFileReader(open_pdf_file)
            #num_pages_nege = read_pdf_nege.getNumPages()
            page_nege = read_pdf_nege.getPage(0)
            page_content_nege = page_nege.extractText()
            page_content_nege = page_content_nege.encode('utf-8')

        html = page_content_nege.decode('ISO-8859-1') #decode because our regex is a string, but html is bytes
        line = re.sub('.xc3.', '', html)
        line_2 = re.sub('.xa9.', '', line)

        taux_nage0004 = pd.DataFrame({'Rates': ['2,79']})
        formules_nage0004 = pd.DataFrame({'Formulas': ['10/5/5 Cap +5/-5']})
        Min_nage0004 = pd.DataFrame({'Min': ['']})
        Max_nage0004 = pd.DataFrame({'Max': ['']})
        duration_nage0004 = Min_nage0004.join(Max_nage0004)

        df_nage0004 = taux_nage0004.join(formules_nage0004).join(duration_nage0004)
        df_nage0004["Rates"] = df_nage0004["Rates"].str.replace(",", ".").str.strip()
        df_nage0004["Rates"] = ((df_nage0004["Rates"].astype(float) / 100) + (0.30 / 100)) * 100

        df_nage0004.insert(0, 'Provider', 'Nagelmackers')
        df_nage0004.insert(1, 'Product_ID', 'NA0004')
        df_nage0004.insert(2, 'Category', 'Home Loan')
        df_nage0004 = df_nage0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # NAGE0005

        with io.BytesIO(response_nege.content) as open_pdf_file:
            read_pdf_nege = PyPDF2.PdfFileReader(open_pdf_file)
            #num_pages_nege = read_pdf_nege.getNumPages()
            page_nege = read_pdf_nege.getPage(0)
            page_content_nege = page_nege.extractText()
            page_content_nege = page_content_nege.encode('utf-8')

        html = page_content_nege.decode('ISO-8859-1')  # decode because our regex is a string, but html is bytes
        line = re.sub('.xc3.', '', html)
        line_2 = re.sub('.xa9.', '', line)

        for _ in line_2:
            #bank_nage = ['Nagelmackers']
            taux_nage0005 = re.findall(r'.2.(.*?)1.3.', line_2)
            taux_nage0005_1 = [i.split('(2)', 1)[1] for i in taux_nage0005]
            taux_nage0005_1 = [i.split('(2)', 1)[1] for i in taux_nage0005_1]
            taux_nage0005_1 = [i.split('(2)', 1)[1] for i in taux_nage0005_1]
            taux_nage0005_1_fix = [s.strip('%') for s in taux_nage0005_1]  # removing '%' sign
        taux_nage0005 = pd.DataFrame({'Rates': taux_nage0005_1_fix})

        formules_nage0005 = pd.DataFrame({'Formulas': ['20/5 Cap +5/-5']})
        Min_nage0005 = pd.DataFrame({'Min': ['']})
        Max_nage0005 = pd.DataFrame({'Max': ['']})
        duration_nage0005 = Min_nage0005.join(Max_nage0005)

        df_nage0005 = taux_nage0005.join(formules_nage0005).join(duration_nage0005)
        df_nage0005["Rates"] = df_nage0005["Rates"].str.replace(",", ".").str.strip()
        df_nage0005["Rates"] = ((df_nage0005["Rates"].astype(float) / 100) + (0.30 / 100)) * 100

        df_nage0005.insert(0, 'Provider', 'Nagelmackers')
        df_nage0005.insert(1, 'Product_ID', 'NA0005')
        df_nage0005.insert(2, 'Category', 'Home Loan')
        df_nage0005 = df_nage0005[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]

    # Concatenate
        global nage_c
        nage_c = pd.concat([
            pd.concat([df_nage0001], axis=1),
            pd.concat([df_nage0002], axis=1),
            pd.concat([df_nage0003], axis=1),
            pd.concat([df_nage0004], axis=1),
            pd.concat([df_nage0005], axis=1)
        ])

        print(tabulate(nage_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def nage_save():
    nage()

    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    nage_c.to_csv(os.path.join(path, file_name), index=False)


# #             _           _             # #
# #  _         (_)         | |            # #
# # | |_   ____ _  ___   _ | | ___   ___  # #
# # |  _) / ___) |/ _ \ / || |/ _ \ /___) # #
# # | |__| |   | | |_| ( (_| | |_| |___ | # #
# #  \___)_|   |_|\___/ \____|\___/(___/  # #
# #                                       # #


def trio():

    try:

    # Source 1
        df_trio_source1 = read_pdf('https://www.triodos.be/downloads/downloads-fr/tarifs-et-conditions/liste-tarifs-credit-hypothecaire.pdf', encoding='ISO-8859-1',
                                  stream=False, spreadsheet=True, area=[376.56, 40.32, 457, 532.8], pages=1, pandas_options={'header': None})
        df_trio_source1=df_trio_source1.drop([2,3,4,5,7],axis=1)
        df_trio_source1.columns = ['Formulas','Duration','Rates']
        temp = df_trio_source1["Duration"].str.split("\r", n = 1, expand = True)
        df_trio_source1.insert(1,'Min',temp[0])
        df_trio_source1.insert(2,'Max',temp[1])
        df_trio_source1["Min"] = df_trio_source1["Min"].str.extract(pat = '([0-9]+)')
        df_trio_source1["Max"] = df_trio_source1["Max"].str.extract(pat = '([0-9][0-9])')
        df_trio_source1 = df_trio_source1.drop(['Duration'],axis=1)

    # TRIO0001
        ## Rate of >75000
        df_trio00011 = df_trio_source1.drop([1,2],axis=0)
        df_trio00011['Formulas']='5+5 > 75,000'
        df_trio00011["Rates"] = df_trio00011["Rates"].str.replace("%", "").str.strip()
        df_trio00011["Rates"] = df_trio00011["Rates"].str.replace(",", ".").str.strip()
        df_trio00011["Rates"] = ((df_trio00011["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        ## Rate of <75000
        df_trio00012 = df_trio_source1.drop([1,2],axis=0)
        df_trio00012['Formulas']='5+5 < 75,000'
        df_trio00012["Rates"] = df_trio00012["Rates"].str.replace("%", "").str.strip()
        df_trio00012["Rates"] = df_trio00012["Rates"].str.replace(",", ".").str.strip()
        df_trio00012["Rates"] = ((df_trio00012["Rates"].astype(float) / 100) + (0.25 / 100) + (0.75 / 100)) * 100

        ##Concatenate rates for >75000 and <75000
        data_trio0001 = pd.concat([df_trio00011, df_trio00012])
        data_trio0001.insert(0, 'Provider', 'Triodos')
        data_trio0001.insert(1, 'Product_ID', 'TRIO0001')
        data_trio0001.insert(2, 'Category', 'Home Loan')
        data_trio0001 = data_trio0001[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # TRIO0002
        ## Rate of >75000
        df_trio00021 = df_trio_source1.drop([0,2],axis=0)
        df_trio00021['Formulas']='13+5 > 75,000'
        df_trio00021["Rates"] = df_trio00021["Rates"].str.replace("%", "").str.strip()
        df_trio00021["Rates"] = df_trio00021["Rates"].str.replace(",", ".").str.strip()
        df_trio00021["Rates"] = ((df_trio00021["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        ## Rate of <75000
        df_trio00022 = df_trio_source1.drop([0,2],axis=0)
        df_trio00022['Formulas']='13+5 < 75,000'
        df_trio00022["Rates"] = df_trio00022["Rates"].str.replace("%", "").str.strip()
        df_trio00022["Rates"] = df_trio00022["Rates"].str.replace(",", ".").str.strip()
        df_trio00022["Rates"] = ((df_trio00022["Rates"].astype(float) / 100) + (0.25 / 100) + (0.75 / 100)) * 100

        ##Concatenate rates for >75000 and <75000
        data_trio0002 = pd.concat([df_trio00021, df_trio00022])
        data_trio0002.insert(0, 'Provider', 'Triodos')
        data_trio0002.insert(1, 'Product_ID', 'TRIO0002')
        data_trio0002.insert(2, 'Category', 'Home Loan')
        data_trio0002 = data_trio0002[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # TRIO0003

        ## Rate of >75000
        df_trio00031 = df_trio_source1.drop([0,1],axis=0)
        df_trio00031['Formulas']='16+5 > 75,000'
        df_trio00031["Rates"] = df_trio00031["Rates"].str.replace("%", "").str.strip()
        df_trio00031["Rates"] = df_trio00031["Rates"].str.replace(",", ".").str.strip()
        df_trio00031["Rates"] = ((df_trio00031["Rates"].astype(float) / 100) + (0.25 / 100)) * 100

        ## Rate of <75000
        df_trio00032 = df_trio_source1.drop([0,1],axis=0)
        df_trio00032['Formulas']='16+5 < 75,000'
        df_trio00032["Rates"] = df_trio00032["Rates"].str.replace("%", "").str.strip()
        df_trio00032["Rates"] = df_trio00032["Rates"].str.replace(",", ".").str.strip()
        df_trio00032["Rates"] = ((df_trio00032["Rates"].astype(float) / 100) + (0.25 / 100) + (0.75 / 100)) * 100

        ##Concatenate rates for >75000 and <75000
        data_trio0003 = pd.concat([df_trio00031, df_trio00032])
        data_trio0003.insert(0, 'Provider', 'Triodos')
        data_trio0003.insert(1, 'Product_ID', 'TRIO0003')
        data_trio0003.insert(2, 'Category', 'Home Loan')
        data_trio0003 = data_trio0003[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Source 2
        df_trio_source2 = read_pdf('https://www.triodos.be/downloads/downloads-fr/tarifs-et-conditions/liste-tarifs-credit-hypothecaire.pdf', encoding='ISO-8859-1',
                                      stream=False, spreadsheet=True, area=[610, 40.32, 629, 530], pages=1, pandas_options={'header': None})
        df_trio_source2=df_trio_source2.drop([1,2,3,4,5,7],axis=1)
        df_trio_source2.columns = ['Duration','Rates']
        df_trio_source2.insert(1,'Min','10')
        df_trio_source2.insert(2,'Max','10')
        df_trio_source2 = df_trio_source2.drop(['Duration'],axis=1)

    # TRIO0004
        ## Rate of >75000
        df_trio00041 = df_trio_source2.copy()
        df_trio00041["Rates"] = df_trio00041["Rates"].str.replace("%", "").str.strip()
        df_trio00041["Rates"] = df_trio00041["Rates"].str.replace(",", ".").str.strip()
        df_trio00041["Rates"] = ((df_trio00041["Rates"].astype(float) / 100) + (0.25 / 100)) * 100
        df_trio00041.insert(0, 'Formulas', '> 75000 10 fixed')

        # Rate of <75000
        df_trio00042 = df_trio_source2.copy()
        df_trio00042["Rates"] = df_trio00042["Rates"].str.replace("%", "").str.strip()
        df_trio00042["Rates"] = df_trio00042["Rates"].str.replace(",", ".").str.strip()
        df_trio00042["Rates"] = ((df_trio00042["Rates"].astype(float) / 100) + (0.25 / 100) + (0.75 / 100)) * 100
        df_trio00042.insert(0, 'Formulas', '< 75000 10 fixed')

        ##Concatenate rates for >75000 and <75000
        data_trio0004 = pd.concat([df_trio00041, df_trio00042])
        data_trio0004.insert(0, 'Provider', 'Triodos')
        data_trio0004.insert(1, 'Product_ID', 'TRIO0004')
        data_trio0004.insert(2, 'Category', 'Home Loan')
        data_trio0004 = data_trio0004[['Provider', 'Product_ID', 'Category', 'Formulas', 'Min', 'Max', 'Rates']]  # Change order of columns

    # Concatenate
        global trio_c
        trio_c = pd.concat([
            pd.concat([data_trio0001], axis=1),
            pd.concat([data_trio0002], axis=1),
            pd.concat([data_trio0003], axis=1),
            pd.concat([data_trio0004], axis=1)])

        print(tabulate(trio_c, headers='keys', tablefmt='psql', showindex="never"))
    
    except:
        pass

def trio_save():
    trio()

    path = os.path.abspath("History/")  # saving file to the folder history
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    # Line below is used to concat the whole dfs and save it into a csv file

    trio_c.to_csv(os.path.join(path, file_name), index=False)



def all():
    try:
        argenta()
    except:
        pass
    try:
        bvbr()
    except:
        pass
    try:
        bpost()
    except:
        pass
    try:
        belfius()
    except:
        pass
    try:
        cbc()
    except:
        pass
    try:
        crelan()
    except:
        pass
    try:
        elantis()
    except:
        pass
    try:
        federale()
    except:
        pass
    try:
        hellobank()
    except:
        pass
    try:
        ing()
    except:
        pass
    try:
        kbc()
    except:
        pass
    try:
        keytrade()
    except:
        pass
    try:
        nage()
    except:
        pass
    try:
        trio()
    except:
        pass

    all_c = pd.concat([
        pd.concat([arge_c], axis=1),
        pd.concat([bvbr_c], axis=1),
        #pd.concat([bpos_c], axis=1),
        pd.concat([belf_c], axis=1),
        pd.concat([cbcx_c], axis=1),
        pd.concat([crel_c], axis=1),
        pd.concat([elan_c], axis=1),
        pd.concat([fede_c], axis=1),
        pd.concat([hbnk_c], axis=1),
        pd.concat([ingx_c], axis=1),
        pd.concat([kbcx_c], axis=1),
        pd.concat([keyt_c], axis=1),
        pd.concat([nage_c], axis=1),
        pd.concat([trio_c], axis=1)
    ])

    print(tabulate(all_c, headers='keys', tablefmt='psql', showindex="never"))

    path = os.path.abspath("History/")
    file_name = str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M")) + '.csv'

    all_c.to_csv(os.path.join(path, file_name), index=False)


if __name__ == '__main__':
    bpost()