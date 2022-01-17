

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
        print(f'jtexpress_my Setting Up Firefox Selenium Driver {i}')
        driver = webdriver.Firefox(options=firefox_opt)
    else:
        print(f'jtexpress_my Setting Up Chrome Selenium Driver {i}')
        driver = webdriver.Chrome(options=chrome_opt)


    # driver.get(url)


    drivers.append({'use':None,'driver':driver,'epoch':0})

    print(datetime.datetime.now(), end=' ')

    if use_firefox:

        print(f'jtexpress_my Started Firefox Selenium Driver {i}')
    
    else:

        print(f'jtexpress_my Started Chrome Selenium Driver {i}')









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
