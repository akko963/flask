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
   worksite = request.form.get('vault')  # can directly look-up with request.form['vault']
   # but this raises error if not found
   # .get will never raise error, it will return None if not found
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

'''
I noticed the following in this script:
javascript security issues in dealing with data storage and request, inherently 
letting client compute things is not the most secured. 
1) letting client set boundaries: there is a chance that the client would just 
access/edit the boundaries and submit it to server.
2) altering the identity/place/id without validity
In this script I also learned:
session is dictionary-based.
3)to check a key existence in dictionary: "if key in dictionary"
4) switch doesn't exist in python. A good alternative is dictionary.
5) a default for dictionary (when not found) is tagging a {}.get(var,defaultvalue)
6) some inputs can be hidden and yet submitted along with other input items from 
the form at submit
7) "name" attributes in html tags (especially form's) are used for server communication.
server checks for parts of the form thru the 'name'. example: request.form.get('name')

Some tips:
kept forgetting that designing a page should be top-down. Using classes and ids are 
good practice. probably better than using generic tags: p/h2 etc. This will save
headaches and up the dev times.

#previously learned
request.
request.form.get('name of inputs from form')

reference:
datetime
import datetime
datetime.datetime.today()
datetime.datetime.today().strftime()
   where %Y,%m,%d year,month,day and %H %M %s 24h min seconds. %I 12h.  %p ampm
when in doubt, add braces for ternary/any condition.
auto-scrolling not yet working
'''