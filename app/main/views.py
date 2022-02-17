from flask import render_template,redirect ,url_for,request, jsonify
from . import main
from flask_login import login_required
from ..requests import base_url
from .forms import CommentForm, QuoteForm
from ..models import Quote

import json
from urllib import request

# Views
@main.route('/', methods=['GET','POST'])
@login_required
def index():
    form= QuoteForm()
    
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
    coms=[]
    for i in range(0,len(data)):
        com_id= data[i]['id']
        com= comments.comment.data
        mess={com_id: com}
        coms.append(mess)
                

    return render_template('index.html', data=data, comments=comments, coms=coms)


    