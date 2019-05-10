from flask import Flask
from flask import request,jsonify
from Model import Airline,Airport,Route
from GraphUtils import Graph
import pandas as pd

app = Flask(__name__)

graph = Graph()
dfRoutes = pd.read_csv('../data/routes.csv')
dfAirports = pd.read_csv('../data/airports.csv')
dfAirlines = pd.read_csv('../data/airlines.csv')


def formatPath(pathList):
    returnString = ""
    for segment in formatPathList(pathList):
        returnString += getSegmentString(segment)
    return returnString
    
def getSegmentString(segment):
    airline = getAirline(segment)
    airportOri = getAirport(segment[0])
    airportDest = getAirport(segment[1])
    return "<h1>From "+airportOri+" to "+airportDest+" via "+airline+"</h1>"

def getAirline(segment):
    airlineCode = ""
    for index, row in dfRoutes.iterrows():
        if row[1] == segment[0] and row[2] == segment[1]:
            airlineCode = row[0]
    for index, row in dfAirlines.iterrows():
        if airlineCode == row[1]:
            return row[0]
    return airlineCode

def getAirport(airportCode):
    for index, row in dfAirports.iterrows():
        if airportCode == row[3]:
            return row[0]
    
    return airportCode
    
def formatPathList(pathList):
    returnList = []
    for x,path in enumerate(pathList):
        if x+1<len(pathList):
            returnList.append([pathList[x],pathList[x+1]])
    return returnList
        

@app.route('/route/shortest/pretty')
def shortestPretty():
    try:
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        return formatPath(graph.dijsktra(origin,destination))
    except Exception as e:
        return str(e)

@app.route('/route/shortest/')
def shortest():
    try:
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        return jsonify(formatPathList(graph.dijsktra(origin,destination)))
    except Exception as e:
        return str(e)


if __name__ == '__main__': 
    for index, row in dfRoutes.iterrows():
        graph.add_edge(row[1],row[2])
    app.run(debug=True,port=5001)
    