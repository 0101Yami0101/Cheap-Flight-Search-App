import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def search_flight_code(self,flight_API, parameters, header):
        res = requests.get(url= flight_API, params= parameters, headers= header)
        data = res.json()
        return data["locations"][0]["code"]

    





