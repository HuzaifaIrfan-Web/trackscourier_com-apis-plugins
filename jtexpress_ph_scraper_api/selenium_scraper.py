
from bs4 import BeautifulSoup



import os


import uuid

import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options as FirefoxOptions







try:

    from .settings import use_firefox,num_of_drivers
except:
  
    from settings import use_firefox,num_of_drivers






import datetime


drivers=[]


firefox_opt = FirefoxOptions()
firefox_opt.add_argument("--headless")
firefox_opt.set_preference('permissions.default.stylesheet', 2)
firefox_opt.set_preference('permissions.default.image', 2)
firefox_opt.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')


from selenium.webdriver.chrome.options import Options
chrome_opt = Options()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--no-sandbox')
chrome_opt.add_argument('--disable-dev-sh--usage')

# url='https://www.madhurcouriers.in/CNoteTracking'
for i in range(0,num_of_drivers):

    print(datetime.datetime.now(), end=' ')



    if use_firefox:
        print(f'jtexpress_ph Setting Up Firefox Selenium Driver {i}')
        driver = webdriver.Firefox(options=firefox_opt)
    else:
        print(f'jtexpress_ph Setting Up Chrome Selenium Driver {i}')
        driver = webdriver.Chrome(options=chrome_opt)


    # driver.get(url)


    drivers.append({'use':None,'driver':driver,'epoch':0})

    print(datetime.datetime.now(), end=' ')

    if use_firefox:

        print(f'jtexpress_ph Started Firefox Selenium Driver {i}')
    
    else:

        print(f'jtexpress_ph Started Chrome Selenium Driver {i}')







def select_driver(id):

    selecting=True

    while selecting:

        for i,driver_obj in enumerate(drivers):
            
            if driver_obj['use'] ==None:

                driver_obj['use']=id
                epoch=int(datetime.datetime.now().timestamp())
                # print(epoch)
                driver_obj['epoch']=epoch
                driver=driver_obj['driver']


                index=i


                selecting=False
                break
            else:
                epoch=int(datetime.datetime.now().timestamp())
                # print(epoch)
                if (epoch > driver_obj['epoch'] +10):
                    print('Driver Use TimeOut')
                    driver_obj['use'] =None
                


    return index, driver


def use_driver(tnum):
   
  
    id = uuid.uuid1().hex

    selecting=True
    while selecting:

        index,driver=select_driver(id)

        if drivers[index]['use']==id:
            selecting=False

    # print('driver selected')

    url=f'https://www.jtexpress.ph/index/query/gzquery.html?bills={tnum}'
    driver.get(url)
    
    time.sleep(1)



    try:


        # el = driver.find_element_by_class_name('bill_state_list')

        el = driver.find_element(By.CLASS_NAME, "bill_state_list")

        els = driver.find_element(By.CLASS_NAME, "bill_state_item")



    except:
        print('No data Found')
        drivers[index]['use'] =None
        return False

    innerHtml=el.get_attribute('innerHTML')

    soup = BeautifulSoup(innerHtml, 'html.parser')    
        


    drivers[index]['use'] =None

    return soup



def extract_status_history(soup):

    histories_div=soup.find_all(class_="bill_state_item")

    if len(histories_div) <=0:
        print('histories_div length zero')
        return False


    status_histories=[]

    for div in histories_div:
        bill_state_day=div.find(class_="bill_state_day").text
        # print(bill_state_day.text)

        bill_state_text=div.find(class_="bill_state_text")
        # print(bill_state_text)

        states=bill_state_text.find_all("p")
        # print(states)

        location=states[0].text

        city=states[1].text

        try:

            city=city.partition("：")[2]

        except:
            print('cant partition')


        detail=states[2].text.replace(",Due to the implementation of community quarantine which limits transportation and mobility, delivery schedules may get affected.Thank you for your patience and understanding.", "")
        
        # re.sub(r'[^\w]', ' ', s)

        # 【


        try:
            status=states[3].text

        except:
            status=""

        status_history={'datetime':bill_state_day,'location':location,'city':city,'detail':detail,'status':status}

        status_histories.append(status_history)
                

    



    return status_histories
                



def return_details(tnum):
    


    soup=use_driver(tnum)

    if soup == False:
        return False

    # print('got soup')

    status_histories=extract_status_history(soup)
    return_obj={'tnum':tnum,'status_histories':status_histories}



    return return_obj


