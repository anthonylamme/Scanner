import mechanize
import time as t
from os import path
import win32com.client

webaddress='http://admin.erincondren.com' #site
BarcodeAddress='http://admin.erincondren.com/admin/order_status/barcode_status_update/10000247'#barcode site
##test='http://admin.erincondren.com/admin/userprofile'
###target='userForm'

formLog='loginForm' #Login Form Name
#formBar='print_label_form' #Barcode Form Name
formBar='barcode_update_form'
BaudRate=115200 #baudRate of scanner
filepathway='/home/pi/SlackData/Data/'
key_to_the_kingdom='Keys.txt'
Susername='ecd'
Spassword='admin2020'
keyway=open(filepathway+key_to_the_kingdom,'r')
username=keyway.readline().rstrip().strip(' ').strip()#username
passcode=keyway.readline().rstrip().strip(' ').strip()#password
date=t.localtime(t.time())
outputDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
outputDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
filename='%s.csv'%outputDate
shell = win32com.client.Dispatch("WScript.Shell")
while True:
    try:
        while True:
            date=t.localtime(t.time())
            print 'start %d:%d:%d'%(date[3],date[4],date[5])
            agent=mechanize.Browser()#Browser
            agent.set_handle_robots(False)#ignore Bot Rules
            agent.addheaders=[('User-agent','Firefox')] #method of browsing
            agent.open(webaddress) #go to address
            shell.SendKeys(Susername)#username
            shell.SendKeys('{TAB}')#Tab
            shell.SendKeys(Spassword)#password
            shell.SendKeys('{ENTER}')#Enter
            
            agent.select_form(name=formLog) 
            agent['username']=username
            agent['password']=passcode
            result=agent.submit()
            date=t.localtime(t.time())
            print 'website %d:%d:%d'%(date[3],date[4],date[5])
            #go to website
            agent.open(BarcodeAddress)
            agent.select_form(name=formBar)
            date=t.localtime(t.time())
            print 'ready %d:%d:%d'%(date[3],date[4],date[5])
            barcode=raw_input('') #Pi gets Barcode
            agent.select_form(name=formBar)
            agent['barcode']=barcode
            result=agent.submit()
            date=t.localtime(t.time())
            print '%d:%d:%d'%(date[3],date[4],date[5])
    except:
        t.sleep(1)
        continue
    '''
    date=t.localtime(t.time())
    checkDate='%d_%d_%d'%(date[1],date[2],(date[0]%100))
    checkDate2='%d/%d/%d'%(date[1],date[2],(date[0]%100))
    clock='%d:%d:%d'%(date[3],date[4],date[5])
    filename2='%s.csv'%checkDate
    
    #print 'Writing to File'
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
'''
