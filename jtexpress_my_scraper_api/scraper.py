
from bs4 import BeautifulSoup

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def use_driver(tnum):
    url=f'https://www.jtexpress.my/tracking/{tnum}'
    r = requests.get(url, verify=False)
    innerHtml= r.text
    soup = BeautifulSoup(innerHtml, 'html.parser')
    return soup


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
        print('Sorry, information not found')
        return False


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

    soup=use_driver(tnum)

    if soup == False:
        return False

    # print('got soup')
    tracking_details=extract_tracking_details(soup,tnum)

    return tracking_details


