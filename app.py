

import json
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)


from jtexpress_ph_scraper_api.selenium_scraper import return_details as ph_return_details

from jtexpress_my_scraper_api.scraper import return_details as my_return_details
 
 
app = Flask(__name__)



@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')



@app.route('/track/jtexpress_my_scraper_api',methods = ['GET'])
def tracking_my():

    # tnum=int(tnum_str)

    try:

        tnum = int(request.args.get('tnum'))
        print(f'jtexpress my tnum: {tnum}')

    except:
        
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422


    if not tnum:
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    if (len(str(tnum)) > 16) or (len(str(tnum)) < 8):
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    tracking_details=my_return_details(tnum)

    if tracking_details ==False:
        return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

    return jsonify(tracking_details), 200











@app.route('/track/jtexpress_ph_scraper_api',methods = ['GET'])
def tracking_ph():

    # tnum=int(tnum_str)

    try:

        tnum = int(request.args.get('tnum'))
        print(f'jtexpress ph tnum: {tnum}')

    except:
        
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422


    if not tnum:
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    if (len(str(tnum)) > 16) or (len(str(tnum)) < 8):
        return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    tracking_details=ph_return_details(tnum)

    try:
        if tracking_details['status_histories'] ==False:
            return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

    except:
        return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

    return jsonify(tracking_details), 200




if __name__ == '__main__':
	app.run(debug=True)