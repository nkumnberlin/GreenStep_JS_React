# -*- coding: utf-8 -*-

import requests
import json
from .airportfinder import airportfinder
from .flightdistcalc import flightdistcalc
from ..APIrequests.APIrequest import APIrequest

class planflightroute:

    def planflight(self, arr_lng, arr_lat, dest_lng, dest_lat):
        jsonload = json.load(open("api/gs_python/flight/largeairportDB.json"))
        afinder = airportfinder()
        #planfroute = planflightroute()
        #origin_iata, origin_city, origin_airport_lat, origin_airport_lng \
        origin_airport = afinder.find_next_airport(arr_lat, arr_lng, jsonload)
        #dest_iata, dest_city, dest_airport_lat, dest_airport_lng \
        dest_airport = afinder.find_next_airport(dest_lat, dest_lng, jsonload)
        #print ((origin_airport["iata"]+"\t"+ dest_airport["iata"]))
        flight_possible = self.check_planned_route(origin_airport["iata"], dest_airport["iata"])
        #print (flight_possible)
        if flight_possible == True:
            return self.getValues(origin_airport, dest_airport)
        #tbd: else ist mit Fehlern behaftet - erledigt ?
        # - mgl Anpassung des Algorithmus, dass er weniger Anfragen durchführen muss
        else:
            airports = afinder.find_city_airport(origin_airport["city"], jsonload)
            #print (flight_possible)
            #checkt ob der Startflughafen zu variieren ist
            for airport in airports:
                flight_possible = self.check_planned_route(airport["iata"], dest_airport["iata"])
                if flight_possible:
                    print (flight_possible)
                    return self.getValues(airport, dest_airport)
                    break
            #print (flight_possible)
            if flight_possible == False:
                airports = afinder.find_city_airport(dest_airport["city"], jsonload)
                for airport in airports:
                    flight_possible = self.check_planned_route(origin_airport["iata"], airport["iata"])
                    if flight_possible:
                        print (flight_possible)
                        return self.getValues(airport, dest_airport)
                        break
            #print (flight_possible)
            if flight_possible == False:
                print ("Nothing found")
                return 0, 0, 0, 0, 0, 0

    def check_planned_route(self, iata_origin, iata_dest):
        flight_route_response = requests.get(
            "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/DE/EUR/de-DE/" +
            iata_origin + "/" + iata_dest + "/2019-10-01?inboundpartialdate=2019-10-10",
            headers={
                "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "1de2f44c33msh037f72b19990e75p17ddc4jsn11356a6a1be8"
            }
        )
        # print (flight_route_response.raw_body)  # wenn "QuoteId":1,  im JSON-Response vorhanden dann: verfügbaren Routen
        json_decode_flightroute = json.loads(flight_route_response.text)
        #print (json_decode_flightroute)
        #tbd: if-Block wirft FEHLER wenn keine Routen vorhanden sind - erledigt
        try:
            #print (json_decode_flightroute["Quotes"][0]["QuoteId"])
            if json_decode_flightroute["Quotes"][0]["QuoteId"] != 0:
                return True
            else:
                return False
        except KeyError:
            return False

    def getValues(self, origin_airport, dest_airport):
        flight_dist = flightdistcalc().distanceInKmBetweenEarthCoordinates(origin_airport["lat"], origin_airport["lng"],
                                                                         dest_airport["lat"], dest_airport["lng"])
        takeoff_time= 30 #min
        flight_time = (flight_dist/800+takeoff_time)*60 #time is always in seconds
        arrival_transit_dist, arrival_transit_time = APIrequest().callGoogleDirectionsAPI(
            str(origin_airport["lat"]) + " " + str(origin_airport["lng"]), origin_airport["iata"] + " airport",
            "transit")
        departure_transit_dist, departure_transit_time = APIrequest().callGoogleDirectionsAPI(
            str(dest_airport["lat"]) + " " + str(dest_airport["lng"]), dest_airport["iata"] + " airport",
            "transit")
        return departure_transit_dist, arrival_transit_dist, flight_dist, departure_transit_time, arrival_transit_time, flight_time


            #tbd: if 0,0,0,0,0,0 is returned, flight planning didn't was succesfull

    # def find_other_airport(self):
    #     #     airports = airportfinder.find_city_airport(origin_airport["city"])
    #     #     for airport in airports:
    #     #         flight_possible = planflightroute.check_planned_route(airport["iata"], dest_airport["iata"])
    #     #         if flight_possible:
    #     #             return planflightroute.getValues(airport, dest_airport)
    #     #             break