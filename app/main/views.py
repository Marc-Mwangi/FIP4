from flask import render_template,redirect ,url_for,request, jsonify
from . import main
from flask_login import current_user, login_required
from ..requests import base_url
from .forms import CommentForm, QuoteForm,QuoteCommentForm
from ..models import Quote, User
from .. import db
import json
from urllib import request

# Views
@main.route('/', methods=['GET','POST'])
@login_required
def index():
    form= QuoteForm()
    quoteComment= QuoteCommentForm()
    user= current_user.id
    if form.validate_on_submit():
        userQuote= Quote(quote= form.quote.data,user_id=user)
        
        db.session.add(userQuote)
        db.session.commit()
    
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
    post= Quote.query.all()
    #length = len(post)
    #p= list(filter(None,post))
    


    
    for i in range(0,len(data)):
        com_id= data[i]['id']
        com= comments.comment.data
        mess={com_id: com}
        coms.append(mess)
                

    return render_template('index.html', data=data, comments=comments, coms=coms, form=form,post=post)


    