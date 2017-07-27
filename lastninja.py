from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/ninja/<name>')
def show_user_profile(name):
   if name==None:
      return render_template("ninjaturtle.html",ninja=None,file=["leonardo.jpg","michelangelo.jpg","notapril.jpg","raphael.jpg"])
   ninja,filename = switchNinja(name)
   return render_template("ninjaturtle.html", ninja=ninja,file=filename)
@app.route('/ninja')
def show_all():
      return render_template("ninjaturtle.html",ninja=None,file=["leonardo.jpg","michelangelo.jpg","donatello.jpg","raphael.jpg"])
@app.route('/')
def index():
      return render_template("default.html")

def switchNinja(x):
   return {
      "donatello": ("Donatello","donatello.jpg"),
      "leonardo": ("Leonardo","leonardo.jpg"),
      "michelangelo": ("Michelangelo","michelangelo.jpg"),
      "raphael": ("Raphael","raphael.jpg"),
   }.get(x,("Not April","notapril.jpg"))

app.run(debug=True,host='0.0.0.0', port=9000)
