from flask import render_template,redirect ,url_for,request, jsonify
from . import main
from flask_login import login_required
from ..requests import base_url
from .forms import CommentForm

import json
from urllib import request

# Views
@main.route('/', methods=['GET','POST'])
@login_required
def index():
    with request.urlopen(base_url) as url:
        data1 = json.loads(url.read().decode())
    
    with request.urlopen(base_url) as url:
        data2 = json.loads(url.read().decode())
    
    with request.urlopen(base_url) as url:
        data3 = json.loads(url.read().decode())
    
    with request.urlopen(base_url) as url:
        data4 = json.loads(url.read().decode())
    
    with request.urlopen(base_url) as url:
        data5 = json.loads(url.read().decode())
    
    data= [data1,data2,data3,data4,data5]

    comments= CommentForm()
        

    return render_template('index.html', data=data, comments=comments)


    