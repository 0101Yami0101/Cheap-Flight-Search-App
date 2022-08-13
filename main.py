import requests
from flight_search import *
from data_manager import DataManager
from flight_data import FlightData


#sheety
SHEETY_API = "https://api.sheety.co/e032b37477a3897f988da0947a1d6e24/flights/sheet1"
SHEETY_AUTH = "Basic eWFtaTpTaG93cGFzc3dvcmRAMQ"
headerSHEETY = {
    "Authorization" : SHEETY_AUTH
}

#request available data
response = requests.get(url= SHEETY_API, headers = headerSHEETY)
data = response.json()

sheet_data = data['sheet1']

for i in range (len(sheet_data)):
    if sheet_data[i]['iataCode'] == "":
        #fill IATA codes if empty
        city_name = sheet_data[i]["city"]
        AUTH = "vvzVCWj49PjTGMDzbk7Ywamw3G0o_bTp"
        flight_API = "https://tequila-api.kiwi.com/locations/query"
        parameters = {
                    "term": city_name,
                    "location_types": "airport"
                }
        header = {"apikey" : AUTH}

        #Search for IATA code
        search = FlightSearch()
        IATA_code = search.search_flight_code(flight_API= flight_API, parameters= parameters, header= header)
        print(IATA_code)
        
        #After getting IATA code, fill relevent spaces in the sheet
        row_ID = sheet_data[i]["id"]
        PUT_API = f"https://api.sheety.co/e032b37477a3897f988da0947a1d6e24/flights/sheet1/{row_ID}"
        update_data = {
            "sheet1":{
                "iataCode" : IATA_code
            }
        }

        DataManager(data_to_update= update_data, API= PUT_API, header_file= headerSHEETY)


    def search():
        #search for cheapest flights #dummy departure location -  GAU
        max_price = sheet_data[i]["lowestPrice"]
        destination_IATA = sheet_data[i]["iataCode"]

        search_cheap_flights = FlightData()
        search_cheap_flights.get_cheapest_flights(destinationIATA= destination_IATA, maximumPrice= max_price)


    search()
        







    
        

