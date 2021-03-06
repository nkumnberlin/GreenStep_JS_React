# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:38:13 2019

@author: tristanwachtel
"""
#pyCharm
from ..APIrequests.APIrequest import APIrequest, get_time
from ..transit.crawl_transit_steps import crawl_steps
import json
#react - not tested in react
# from ..APIrequests.APIrequest import APIrequest
# from transit.crawl_trainsit_steps import crawl_steps

class transit_route_cords:
    emission_transit = 0.04

    def __init__(self, origin_lng, origin_lat, dest_lng, dest_lat):
        # Laegnengrad W/E
        self.origin_lng = origin_lng
        # Breitengrad N/S
        self.origin_lat = origin_lat
        self.dest_lng = dest_lng
        self.dest_lat = dest_lat

    def run_transit_planning(self):
        transit_dist, transit_time, json_response= APIrequest().callGoogleDirectionsAPI(str(str(self.origin_lat) + " " + str(self.origin_lng)), str(str(self.dest_lat) + " " + str(self.dest_lng)), "transit", "&departure_time=" + str(get_time().get_next_noon()))
        transit_emission_result = transit_dist / 1000 * self.emission_transit
        return json.dumps({"transit": {"dist": transit_dist, "time": transit_time, "emission": transit_emission_result, "travel_mode": "TRANSIT",  "steps": crawl_steps().get_steps(json_response, str(str(self.origin_lat) + " " + str(self.origin_lng)), str(str(self.dest_lat) + " " + str(self.dest_lng)))}})

class transit_route_address:
    emission_transit = 0.04
    def __init__(self, origin, dest):
        self.origin = origin
        self.dest = dest

    def run_transit_planning(self):
        transit_dist, transit_time , json_response = APIrequest().callGoogleDirectionsAPI(self.origin, self.dest, "transit", "&departure_time=" + str(get_time().get_next_noon()))
        transit_emission_result = transit_dist / 1000 * self.emission_transit
        return {"transit": {"dist": transit_dist, "time": transit_time, "emission": transit_emission_result, "travel_mode": "TRANSIT", "steps": crawl_steps().get_steps(json_response, self.origin, self.dest)}}
#print(transit_route_cords(12.2783002853, 53.9182014465, 12.1815795, 53.1470739).run_transit_planning())
