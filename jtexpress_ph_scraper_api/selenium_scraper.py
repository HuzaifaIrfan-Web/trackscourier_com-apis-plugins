
from bs4 import BeautifulSoup
import datetime

import uuid


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_opt = Options()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--no-sandbox')
chrome_opt.add_argument('--disable-dev-sh--usage')

chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
chrome_opt.experimental_options["prefs"] = chrome_prefs




drivers=[]

for i in range(0,1):

    print(datetime.datetime.now(), end=' ')

    print(f'Setting Up Chrome Selenium Driver {i}')


    driver = webdriver.Chrome(options=chrome_opt)
    drivers.append({'use':None,'driver':driver,'epoch':0})

    print(datetime.datetime.now(), end=' ')

    print(f'Started Chrome Selenium Driver {i}')






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



    try:


        # el = driver.find_element_by_class_name('bill_state_list')

        el = driver.find_element(By.CLASS_NAME, "bill_state_list")

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


