

# import json
# from flask import Flask, render_template, request, jsonify, redirect





# try:
#     from .selenium_scraper import return_details
# except:
#     from selenium_scraper import return_details




# app = Flask(__name__)



# # @app.route('/docs',methods = ['GET'])
# # def index():
# #     return render_template('index.html')



# @app.route('/track/jtexpress_ph_scraper_api',methods = ['GET'])
# def jtexpress_ph_track():

#     # tnum=int(tnum_str)

#     try:

#         tnum = int(request.args.get('tnum'))
#         print(f'jtexpress_ph tnum: {tnum}')

#     except:
        
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422


#     if not tnum:
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



#     if (len(str(tnum)) > 16) or (len(str(tnum)) < 8):
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



#     tracking_details=return_details(tnum)

#     try:
#         if tracking_details['status_histories'] ==False:
#             return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

#     except:
#         return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

#     return jsonify(tracking_details), 200

# if __name__ == '__main__':
# 	app.run(debug=True)


from typing import Optional

from fastapi import FastAPI, HTTPException

import uvicorn as uvicorn
from uvicorn.workers import UvicornWorker

try:
    from .selenium_scraper import return_details
except:
    from selenium_scraper import return_details
 

class MyUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "log_config": "logging.yaml",
    }


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/track/jtexpress_ph_scraper_api")
def track_query(tnum: Optional[str] = None):



    if not tnum:
        raise HTTPException(status_code=404, detail="No tnum")




    if (len(str(tnum)) > 16) or (len(str(tnum)) < 8):
        raise HTTPException(status_code=404, detail="Length error")



    
    

    try:
        tracking_details=return_details(tnum)


    except:
        raise HTTPException(status_code=404, detail="Not Found")

    return tracking_details



if __name__ == '__main__':
      uvicorn.run(app, port=5000)