from flask import Flask, render_template, request, redirect, session
import random
import datetime
from datetime import date
app = Flask(__name__)
app.secret_key = 'nobodyknows'
@app.route('/')
def  index():
#  session['answer'] = random.randint(1,100)
#  random.randint(1,100)   
   print
   if not ('earned' in session and 'log' in session):
      session['earned']=0
      session['log']=[]
      print(session['earned'])
   return render_template("ninjafarm.html")

@app.route('/process_money',methods=['POST'])
def process_money():
   worksite = request.form.get('vault')
   (lower,upper) = switchMoney(worksite)  # fancy switch drop-in replacement
   gain = random.randint(lower,upper)
   session['earned']+= gain
   if worksite== "reset":
      session.pop('log')
      session.pop('earned')
   elif worksite== "casino":
      session['log'].append("Entered a casino and "+ ("earned " if gain >=0 else "lost ") +str(gain) +" golds..."+
         ("Yay! " if gain >=0 else "Ouch .. ")+" ("+datetime.datetime.now().strftime("%Y/%m/%d %H:%M %p")+")")
   else:
      session['log'].append("Earned "+ str(gain) +" golds from the "+worksite+"! ("+datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")+")")
   print('earning',worksite,lower,upper)
   return redirect('/')

def switchMoney(x):
   return {
      'farm' : (10,20),
      'cave' : (5,10),
      'house' : (2,5),
      'casino' : (-50,50)
   }.get(x,(0,5))
app.run(debug=True,host='0.0.0.0', port=9000)
