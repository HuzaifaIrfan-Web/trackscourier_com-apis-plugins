

import json
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

from settings import use_selenium

if use_selenium:
    from selenium_scraper import return_details
else:
    from scraper import return_details
 
 




app = Flask(__name__)



# @app.route('/docs',methods = ['GET'])
# def index():
#     return render_template('index.html')



@app.route('/track/jtexpress_my_scraper_api',methods = ['GET'])
def tracking():

    # tnum=int(tnum_str)

    try:

        tnum = int(request.args.get('tnum'))
        print(f'tnum: {tnum}')

    except:
        
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422


    if not tnum:
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    if (len(str(tnum)) > 16) or (len(str(tnum)) < 8):
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    tracking_details=return_details(tnum)

    if tracking_details ==False:
        return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

    return jsonify(tracking_details), 200

if __name__ == '__main__':
	app.run(debug=True)