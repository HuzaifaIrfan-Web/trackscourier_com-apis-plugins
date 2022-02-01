
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

    url=f'https://www.jtexpress.my/tracking/{tnum}'
    driver.get(url)
    
    time.sleep(1)
    driver.execute_script("captcha.options.onSuccess()")
    time.sleep(2)





    try:
        # print('waiting')
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='accordion']")))
        
    

        el = driver.find_element(By.CLASS_NAME, "accordion")

        innerHtml=el.get_attribute('innerHTML')

        soup = BeautifulSoup(innerHtml, 'html.parser')





    except:
        print('No data Found')
 
        driver_controller.release_driver(driver_index,req_id)
    
        raise Exception
        

 
    driver_controller.release_driver(driver_index,req_id)

    response=extract_tracking_details(soup,tnum)


    try:
        
        print(f'{req_id} Driver {driver_index} Got Response')
        return response
    
    except:
        print(f'{req_id} Driver {driver_index} Got NO Response')
        raise Exception




def extract_status_history(soup):
    body=soup.find(class_="accordion-body")
    status_history=[]
    for parent in body.findChildren(recursive=False):
        children=parent.findChildren(recursive=False)
        dated_status_obj={}
        for n, child in enumerate(children):
            if (n % 2) == 0:
                #even dates
                date=child.text.strip()
    #             print(date)
                dated_status_obj={'date':date}
                
            else:
                #odd time statuses and locations
                history = child.find_all(class_="row")
                statuses=[]
                for a_status in history:

                    time=a_status.find(class_="fw-b mt-3").text.strip()
                    status=a_status.find("b").text.strip()
                    location=a_status.find(class_="fw-light").text.strip()
    #                 print(f'{time} {status} {location}')
                    
                    status_obj={'time':time,'status':status,'location':location}
                    statuses.append(status_obj)
                    
                dated_status_obj['statuses']=statuses
                status_history.append(dated_status_obj)
                
    # print(status_history)
    return status_history
                


def extract_tracking_details(soup,tnum):

    alert=soup.find(class_="alert")
    if alert:
        print('Sorry, information not found Alert Shown')
        raise Exception


    direction=soup.find(class_="col-12 text-start").text.strip().split()
    # print(direction)
    try:
        origin=direction[0]
    except:
        origin=None

    try:
        destination=direction[1]
    except:
        destination=None
        
    status=soup.find(class_="text-center mx-auto mb-3 fw-light h3").text.strip()

    status_history=extract_status_history(soup)

    tracking_details={'tnum':tnum,'origin':origin,'destination':destination,'status':status,'status_history':status_history}



    return tracking_details




def return_details(tnum):
    


    return_obj=use_driver(tnum)

    return return_obj



