import requests
import time as t

from selenium import webdriver #acceses website

values={'username':'user', 
        'password':'pass'}#username and password for site

webAddress='http://gmail.com' #website

filepathway='/home/pi/SlackData/Data/'
BaudRate=115200

driver=webdriver.Chromium() #browser
driver.implicitly_wait(10) #wait for browser to open
driver.get(webAddress) #go to website
print driver.content

req=requests.post(webAddress,data=values) #log in
print r.content

## logged into site now

date=t.localtime(t.time())
outputDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
outputDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
filename='%s.csv'%outputDate

while True:
    date=t.localtime(t.time())
    checkDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
    checkDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
    clock='%H:%M:%S'%(date[3],date[4],date[5])
    filename2='%s.csv'%checkDate
    barcode=raw_input('code?')
    print barcode
    text_box=driver.find_element_by_css_selector('#input')
    text_box.send_keys(barcode)
    driver.find_element_by_css_selector('#submit').click()
    print 'Writing to File'
    if checkDate != outputDate:
        filename=filename2
        outputDate=checkDate
        outputDate2=checkDate2
    
    if not(path.isfile(filepathway+filename)):
        f = open(filepathway+filename, "w")
        f.write("date(mm_dd_yyyy),time(HH:MM:SS),Barcode\n")
        f.write("%s,%s,%s,\n" % (outputDate2,clock,barcode))      
        f.close()
    else:
        f = open(filepathway+filename, 'a') 
        f.write("%s,%s,%s,\n" % (outputDate2,clock,barcode))
        f.close()
    
