from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json




file = open('pjn.json','r')
info = json.load(file)

kljucevi = []

for i in info:
    cpv = i['CPVExtended']
    # if '33140000' in cpv:
    kljucevi.append(i['Id'])
        # print(i['Id'])
        # if i['EstimatedValue']!='null':
        #     print(i['EstimatedValue'])

browser = webdriver.Firefox()
url = 'https://jnportal.ujn.gov.rs/'

for (w,i) in enumerate(kljucevi):
    # browser.find_element_by_css_selector('body').send_keys(Keys.COMMAND + 't') 
    # browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    next_window = browser.window_handles[w]
    browser.switch_to.window(next_window)
    browser.get(url + 'tender-eo/' + str(i))
    elem = browser.find_element_by_css_selector('#documentControl_uiMainContentPH_uiMainContentPH_uiDocumentControl > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2)')
    elem.click()
    if w!=len(kljucevi)-1:
        browser.execute_script('''window.open("http://bings.com","_blank");''')
    