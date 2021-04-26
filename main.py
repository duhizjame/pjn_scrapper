from functions import set_browser_pref, login, get_json_list, enter_data, delete_doc, get_doc
import datetime
from selenium import webdriver
import selenium
import openpyxl
import sqlite3
import mapbox
from selenium.webdriver.common.keys import Keys
import os
import json
import time
import copy
import pymongo
import logging
from openpyxl.styles import PatternFill, Fill, Color
from openpyxl.styles import colors

def main():
    # dl_path = 'konkursne'
    username = input('Enter username:')
    password = input('Enter password:')
    days = input("Enter number of days to search: ")
    curr_date = datetime.date.today()
    profile = set_browser_pref()
    browser = webdriver.Firefox(firefox_profile=profile,executable_path='selenium-drivers/geckodriver')
    try:
        login(username,password,browser)
        time_d = datetime.timedelta(days=int(days))
        target_date = curr_date - time_d
        print(target_date)
        data = get_json_list(browser, target_date)
        enter_data(browser,data)
        browser.close()
    except:
        browser.close()

if __name__ == "__main__":
    main()
