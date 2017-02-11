from flask import Flask
from flask import render_template

app=Flask(__name__)

#try:
#    f=open("traflabkey.txt", "r")
#    import json
#    API_KEY=json.loads(self.f.readline())
#except:
#    print("Error reading file")
#    return("FATAL ERROR")
#finally:
#    f.close()
SITE_ID_SICKLAKAJ="1550"
url="http://api.sl.se/api2/realtimedeparturesV4.{0}?key={1}&siteid={2}&timewindow={3}".format("json", self.API_KEY, self.SITE_ID_SICKLAKAJ, "30")


@app.route("/")
def home():
    str="Hello World"    
    return render_template("home.html")
   
@app.route('/test')
def testpage():
#    return "Test page"
#    import Traflab
#    t=Traflab()
    str="Test page"
    return render_template('test.html', str=str)
#    return str(get_trams)

def get_full_response(url):
    #Returns a dict from the JSON provided by the Trafiklab API, given a compliant REST call
    import requests
    response=requests.get(url)
    return response.json()

def get_trams(url):
    #Returns a dict of tram destinations (keys) and departure times (values, as displayed on boards)
    j=self.get_full_response(url)
    trams=dict()    
    for departure in j["ResponseData"]["Trams"]:
        trams[departure["Destination"]]=departure["DisplayTime"]
    return trams

def get_buses(url):
    #Returns a dics of bus destinations (keys) and departure times (values, as displayed on boards)
    j=get_full_response(url)
    buses=dict()
    for departure in j["ResponseData"]["Buses"]:
        buses[departure["Destination"]]=departure["DisplayTime"]
    return buses

#start sequence
if __name__=="__main__":
    app.run(debug=True)
    
