
from bs4 import BeautifulSoup



import os


import uuid


try:

    from .driver_controller import *
except:
  
    from driver_controller import *





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
        print('histories_div length zero')
        return False


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
    


    soup=use_driver(tnum)

    if soup == False:
        return False

    # print('got soup')

    status_histories=extract_status_history(soup)
    return_obj={'tnum':tnum,'status_histories':status_histories}



    return return_obj


