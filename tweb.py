from flask import Flask
from flask import render_template
from Traflab import Traflab

app=Flask(__name__)
#t=Traflab()

@app.route("/")
def home():
    str="Hello World"    
    return render_template("home.html")
   
@app.route('/test')
def testpage():
#    return "Test page"
    str="Test page"
    return render_template('test.html', str=str)

if __name__=="__main__":
    app.run(debug=True)
    
