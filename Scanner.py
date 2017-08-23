import requests
import time as t
from os import path
from selenium import webdriver #acceses website

values={'username':'alamme', 
        'password':'1234'}#username and password for site
print 'address'
webAddress='http://admin.erincondren.com/' #website

filepathway='/home/pi/SlackData/Data/'
BaudRate=115200
print 'driver'
driver=webdriver.Firefox() #browser
print 'website'
driver.get(webAddress) #go to website
print 'request'
req=requests.post(webAddress,data=values) #log in
print req.content

## logged into site now

date=t.localtime(t.time())
outputDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
outputDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
filename='%s.csv'%outputDate

while True:
    barcode=raw_input('code?')
    date=t.localtime(t.time())
    checkDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
    checkDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
    clock='%d:%d:%d'%(date[3],date[4],date[5])
    filename2='%s.csv'%checkDate
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
    
