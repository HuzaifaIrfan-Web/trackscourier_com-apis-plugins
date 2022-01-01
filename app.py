

import json
from flask import Flask, render_template, request, jsonify, redirect





 
app = Flask(__name__)



@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')


from jtexpress_ph_scraper_api.app import jtexpress_ph_track

from jtexpress_my_scraper_api.app import jtexpress_my_track


app.add_url_rule('/track/jtexpress_ph_scraper_api', 'jtexpress_ph_track', jtexpress_ph_track)

app.add_url_rule('/track/jtexpress_my_scraper_api', 'jtexpress_pmy_track', jtexpress_my_track)
 


if __name__ == '__main__':
	app.run(debug=True)