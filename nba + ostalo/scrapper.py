from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
import datetime
import time
import copy
import pymongo
import logging
import gridfs


def get_doc(browser,id,name):
    url = 'https://jnportal.ujn.gov.rs/tender-eo/' + str(id)
    browser.get(url)
    time.sleep(3)
    elem = browser.find_element_by_css_selector('html body.skin-blue.sidebar-mini form#form1 div.wrapper div#uiContentWrapper.content-wrapper section#uiContent.content div#uiMainContentPH_uiTenderWrapper.notsubtracted div#documentControl_uiMainContentPH_uiMainContentPH_uiDocumentControl.dx-accordion.dx-widget.dx-visibility-change-handler.dx-collection div.dx-accordion-wrapper div.dx-item.dx-accordion-item.dx-item-selected.dx-accordion-item-opened div.dx-item-content.dx-accordion-item-title a')
    elem.click()
    time.sleep(1)
    if(len(name)>100):
        namex = str(name)[:100]
    else:
        namex = str(name)
    try:
        os.rename("Konkursna dokumentacija za ponuđača.zip", namex + ".zip")
    except Exception as e:
        print("ovde greska")
        print(e)
    place = browser.find_element_by_id("uiMainContentPH_uiMainContentPH_ucBasicDetails_uiNuts")
    mesto = str(place.text)
    word = mesto.split(',')
    return word[1].strip()



curr_date = datetime.date.today()
username = input("Enter db username: ")
password = input("Enter db password: ")

client = pymongo.MongoClient("mongodb+srv://"+ username + ":" + password + "@cluster0.dstyf.mongodb.net/test?retryWrites=true&w=majority",27017)
db = client.bonafides
nabavke = db.nabavke
konkursne = db.konkursne
fs = gridfs.GridFSBucket(db)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.dir",'/home/duhizjame/Desktop/python')
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf,application/zip")
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.helperApps.neverAsk.openFile","text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf,application/zip")
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.openFile", "")
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.closeWhenDone", True)
profile.set_preference("pdfjs.disabled", True)

url = 'https://jnportal.ujn.gov.rs/'
browser = webdriver.Firefox(firefox_profile=profile)
browser.get(url + 'prijava')
username = browser.find_element_by_id('uiUsername')
username.send_keys('amilosevic')
pass_field = browser.find_element_by_id('uiPassword')
password = input('Unesite password:')
pass_field.send_keys(password)

log_button = browser.find_element_by_id('uiLogin')
log_button.click()

dani = input("unesite broj dana: ")

timed = datetime.timedelta(days=int(dani))
curr_date = curr_date - timed

# params = f'oglasi-svi?initFilter=["PublishDate",">=","{curr_date}"]'
# browser = webdriver.Firefox(firefox_profile=profile)
# url = 'https://jnportal.ujn.gov.rs/'
# browser.get(url + params)
# json_dl = browser.find_element_by_css_selector('html body.skin-blue.sidebar-mini form#form1 div.wrapper div#uiContentWrapper.content-wrapper section#uiContent.content div#searchGridContainer.dx-widget.searchGridContainer.dx-visibility-change-handler div.dx-datagrid.dx-gridbase-container div.dx-datagrid-header-panel div.dx-toolbar.dx-widget.dx-visibility-change-handler.dx-collection div.dx-toolbar-items-container div.dx-toolbar-after div.dx-item.dx-toolbar-item.dx-toolbar-button div.dx-item-content.dx-toolbar-item-content div.dx-button.dx-button-normal.dx-button-mode-contained.dx-widget.dx-button-has-icon div.dx-button-content i.dx-icon.fa.fa-file-o') 
# curr_time = datetime.datetime.now()
# json_dl.click()
# times = str(curr_time.year) + '-' + str(curr_time.month-1) + '-' + str(curr_time.day) + '-' + str(curr_time.hour) + '-' + str(curr_time.minute) + '-' + str(curr_time.second)
# times2 = str(curr_time.year) + '-' + str(curr_time.month-1) + '-' + str(curr_time.day) + '-' + str(curr_time.hour) + '-' + str(curr_time.minute) + '-' + str(curr_time.second+1)
# filename = 'Огласи о јавној набавци_' + times + '.json'
# filename2 = 'Огласи о јавној набавци_' + times2 + '.json'

params = f'postupci-svi?initFilter=["NoticePublishDate",">=","{curr_date}"]'
browser.get(url + params)
json_dl = browser.find_element_by_css_selector('html body.skin-blue.sidebar-mini form#form1 div.wrapper div#uiContentWrapper.content-wrapper section#uiContent.content div#searchGridContainer.dx-widget.searchGridContainer.dx-visibility-change-handler div.dx-datagrid.dx-gridbase-container div.dx-datagrid-header-panel div.dx-toolbar.dx-widget.dx-visibility-change-handler.dx-collection div.dx-toolbar-items-container div.dx-toolbar-after div.dx-item.dx-toolbar-item.dx-toolbar-button div.dx-item-content.dx-toolbar-item-content div.dx-button.dx-button-normal.dx-button-mode-contained.dx-widget.dx-button-has-icon div.dx-button-content i.dx-icon.fa.fa-file-o') 
curr_time = datetime.datetime.now()
json_dl.click()
times = str(curr_time.year) + '-' + str(curr_time.month-1) + '-' + str(curr_time.day) + '-' + str(curr_time.hour) + '-' + str(curr_time.minute) + '-' + str(curr_time.second)
times2 = str(curr_time.year) + '-' + str(curr_time.month-1) + '-' + str(curr_time.day) + '-' + str(curr_time.hour) + '-' + str(curr_time.minute) + '-' + str(curr_time.second+1)
filename = 'Поступци јавних набавки_' + times + '.json'
filename2 = 'Поступци јавних набавки_' + times2 + '.json'

time.sleep(1)

try:
    f = open(filename,'r')
except:
    f = open(filename2,'r')
data = json.load(f)
try:
    os.remove(filename)
except:
    os.remove(filename2)


# mesta = open('mesta.json','r')
# mjson = json.load(mesta)

for i in data:
    id = i['Id']
    name = i['Name']
    value = i['EstimatedValue']
    tip = i['TypeContract']
    procId = i['ProcedureType']
    cpv = i['CPVExtended'][:8]
    rok = i['SubmissionDeadline']
    if rok is not None:
        rok = i['SubmissionDeadline'][:10]
    narucilac = i['BusinessEntityName']
    planId = i['PlanItemId']
    mKod = i['Nuts']
    # for m in mjson:
    #     if m['Code'] == mKod:
    #         mesto = m['Region']
    if tip == "Добра":
        continue
    nabavka = {
        "name" : name,
        "value" : value,
        "type" : tip,
        "procedure" : procId,
        "cpv" : cpv,
        "deadline" : rok,
        "narucilac" : narucilac,
        "planId" : planId,
        # "region" : mesto,
        "id" : id
    }
    try:
        mesto = get_doc(browser,id,name)
        nabavka.update({'mesto':mesto})
        f = open(str(name)+".zip",'rb')
        content = f.read()
        fs.upload_from_stream_with_id(id,name,content)
        nabavke.insert_one(nabavka)
    except Exception as e:
        print(e)
    



    




