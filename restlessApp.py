from flask import Flask
import tripsCSP


app = Flask(__name__)

@app.route("/getRecommendation")
def computeTrips():
    return "YO"

@app.route("/updateUserPref")
def updateAlgo():
    return "YOYo"

@app.route("/findTrips", methods=["POST"])
def findTripsRoute():
    return tripsCSP.findTrips();

if __name__ == "__main__":
    app.run(host='0.0.0.0')
