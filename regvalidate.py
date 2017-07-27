from flask import Flask, render_template, request, redirect, session,flash
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'^[A-z]+$')
PASS_REGEX= re.compile(r'^(([0-9]{1})|([A-Z]{1})|([a-z]{1})){8,20}$')
app = Flask(__name__)
app.secret_key = 'nobodyknows'
@app.route('/')
def  index():
   return render_template('regform.html')

@app.route('/validate',methods=['POST'])
def validate():
   if ( len(request.form.get('fname')) < 1 ) or (len(request.form.get('lname')) < 1) \
    or       (len(request.form.get('pword')) < 1 ) or (len(request.form.get('confirm')) < 1) or \
      (len(request.form.get('email')) < 1 ) :
      flash("One or more of the required fields are empty!","Error") # just pass a string to the flash function
   elif not EMAIL_REGEX.match(request.form.get('email')) :
      flash("Invalid Email Address!","Error") # just pass a string to the flash function
   elif not NAME_REGEX.match(request.form.get('lname')+request.form.get('fname')) :
      flash("Invalid Name!") # just pass a string to the flash function
   elif not ( len (request.form.get('pword')) >=9 ):
      flash("Passworld should be more than 8 characters!","Error")
   elif not ( PASS_REGEX.match(request.form.get('pword'))) :
      flash("Passworld must have at least 1 lower letter, 1 upper letter and 1 digit!","Error")
   elif not request.form.get('pword') == request.form.get('confirm'):
      flash("Passwords do not match!","Error")
   else:
      flash("Registration info submitted!","Success")
   return render_template('submitted.html')

app.run(debug=True,host='0.0.0.0', port=9000)
