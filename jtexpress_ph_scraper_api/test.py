import grequests
import datetime

import json
urls = [
]

url='http://127.0.0.1:5000/tracking/620000295758173'

start= datetime.datetime.now().timestamp()

for i in range(0,100):

    urls.append(url)

rs = (grequests.get(u) for u in urls)

responses = grequests.map(rs)

for res in responses:
    # print(res.content)
    d = json.loads(res.content)
    print(d.keys())
    

end= datetime.datetime.now().timestamp()

print(f'Time Taken [s] {end-start}')

