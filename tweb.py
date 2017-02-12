from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def home():
    str="Hello World"    
    return render_template("home.html")
   
@app.route('/sicklakaj')
def sicklakaj():
    try:
        import os
        SITE_ROOT=os.path.realpath(os.path.dirname(__file__))
        path=os.path.join(SITE_ROOT, "traflabkey.txt")
        f=open(path, "r")
        import json
        API_KEY=json.loads(f.readline())
    except:
        print("Error reading file")
        return("FATAL ERROR")
    finally:
        f.close()
    SITE_ID_SICKLAKAJ="1550"
    url="http://api.sl.se/api2/realtimedeparturesV4.{0}?key={1}&siteid={2}&timewindow={3}".format("json", API_KEY, SITE_ID_SICKLAKAJ, "30")
    results=get_trams(url)
    destinations=[]
    for key in results.keys():
        destinations.append(str(key))

    times=[]
    for value in results.values():
        times.append(str(value))
#    a=[str(u'alfa-1'), str(u'alfa-2')]
#    b=["beta-1", "beta-2"]
    return render_template("sicklakaj.html", destinations=destinations, times=times)
#    return render_template("s.html", a=a, b=b)   


def get_full_response(url):
    #Returns a dict from the JSON provided by the Trafiklab API, given a compliant REST call
    import requests
    response=requests.get(url)
    return response.json()

def get_trams(url):
    #Returns a dict of tram destinations (keys) and departure times (values, as displayed on boards)
    j=get_full_response(url)
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
    app.run(debug=True, threaded=True)
    
