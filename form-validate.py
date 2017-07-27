from flask import Flask, render_template, request, redirect, session,flash
import random
import datetime
from datetime import date
app = Flask(__name__)
app.secret_key = 'nobodyknows'
@app.route('/')
def  index():
   return render_template('forms.html')

@app.route('/validate',methods=['POST'])
def validate():
   if len(request.form['name']) < 1:
      flash("Name cannot be empty!") # just pass a string to the flash function
   if len(request.form['comment']) < 1:
      flash("Comment cannot be empty!") # just pass a string to the flash function
   elif len(request.form.get('comment')) > 120 :
      flash("Comment is too long")
   return render_template('submitted.html',name=request.form.get('name'),location=request.form.get('loc'),lang=request.form.get('lang'),comment=request.form.get('comment'))

app.run(debug=True,host='0.0.0.0', port=9000)
