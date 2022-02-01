
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

import time


import uuid



try:

    from .Driver_Controller import Driver_Controller

except:

    from Driver_Controller import Driver_Controller
    



driver_controller=Driver_Controller()







def use_driver(tnum):
   
  
    req_id = uuid.uuid1().hex

    selecting=True
    while selecting:

        driver_index,driver=driver_controller.select_driver(req_id)

        if driver_controller.check_driver_use(driver_index,req_id):
            selecting=False



    # print('driver selected')

    url=f'https://www.jtexpress.ph/index/query/gzquery.html?bills={tnum}'
    driver.get(url)
    
    time.sleep(1)



    try:



        el = driver.find_element(By.CLASS_NAME, "bill_state_list")




    except:
        print('No bill_state_list Found')
 
        driver_controller.release_driver(driver_index,req_id)
    
        raise Exception

    innerHtml=el.get_attribute('innerHTML')

    soup = BeautifulSoup(innerHtml, 'html.parser')    
        


 
    driver_controller.release_driver(driver_index,req_id)

    

    try:
        status_histories=extract_status_history(soup)
        print(f'{req_id} Driver {driver_index} Got Response')
        return {'tnum':tnum,'status_histories':status_histories}
    
    except:
        print(f'{req_id} Driver {driver_index} Got NO Response')
        raise Exception


def extract_status_history(soup):

    histories_div=soup.find_all(class_="bill_state_item")

    if len(histories_div) <=0:
        print('histories_div length zero')
        raise Exception


    status_histories=[]

    for div in histories_div:

        try:
            bill_state_day=div.find(class_="bill_state_day").text

            # print(bill_state_day.text)
        except:
            bill_state_day=''



        bill_state_text=div.find(class_="bill_state_text")
        # print(bill_state_text)

        states=bill_state_text.find_all("p")
        # print(states)


        try:
            location=states[0].text
        except:
            location=''

        try:
            city=states[1].text
        except:
            city=''

    
        try:

            city=city.partition("：")[2]

        except:
            print('cant partition city')


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
    


    return_obj=use_driver(tnum)

    return return_obj


