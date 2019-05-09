

class Airline:

    def __init__(name, twoDigitCode,threeDigitCode,country):
        self.name = name
        self.twoDigitCode = twoDigitCode
        self.threeDigitCode = threeDigitCode

class Airport:

    def __init__(name, city, country, IATA3, latitute, longitude):
        self.name = name
        self.city = city
        self.country = country
        self.IATA3 = IATA3
        self.latitude = latitude
        self.longitude = longitude

class Route:

    def __init__(airline, origin, destination):
        self.airline = ariline
        self.origin = origin
        self.destination = destination
    
        
