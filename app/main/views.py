from flask import render_template,redirect ,url_for,request, jsonify
from . import main
from flask_login import login_required
from ..requests import base_url

import json
from urllib import request

# Views
@main.route('/', methods=['GET','POST'])
@login_required
def index():
    with request.urlopen(base_url) as url:
        data = json.loads(url.read().decode())


    
    


    

    
    
    
    
    return render_template('index.html', quote=data)


    