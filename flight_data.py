import requests
import datetime
from notification_manager import NotificationManager

API = "https://tequila-api.kiwi.com/v2/search"
AUTH_KEY = "vvzVCWj49PjTGMDzbk7Ywamw3G0o_bTp"
header = {"apikey": AUTH_KEY}

#dates
date = datetime.datetime.now()
tomorrow = (date + datetime.timedelta(1)).strftime("%d/%m/%Y")
six_months = (date + datetime.timedelta(180)).strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def get_cheapest_flights(self, destinationIATA, maximumPrice):
        
        try:
            self.search_params = {
                "fly_from": "GAU",
                "fly_to": destinationIATA,
                "date_from": tomorrow,
                "date_to": six_months,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "curr": "INR",
                "one_for_city": 1,
                "max_stopovers": 0,
                "flight_type": "round"}

        

            resp = requests.get(url=API, params= self.search_params, headers= header)
            data = resp.json()
            data_slice = data["data"] #list


            for i in range (len(data_slice)):
                if data_slice[i]["price"] < maximumPrice:
                    flight_price = data_slice[i]['price']
                    print(f"TO {destinationIATA}: Cheapest Flight is at - {flight_price}")

                    city_from = data_slice[i]["cityFrom"]
                    dep_IATA = data_slice[i]["flyFrom"]
                    city_to = data_slice[i]["cityTo"]
                    arr_IATA = data_slice[i]["flyTo"]
                    outbound_date = data_slice[i]['route'][0]['local_departure'][0:10]
                    inbound_date = data_slice[i]['route'][1]['local_departure'][0:10]
                    

                    #Send notification
                    notify = NotificationManager()
                    notify.send_notification(price= flight_price, from_Loc= city_from, from_IATA=dep_IATA, to_Loc= city_to, to_IATA= arr_IATA, outbound_date= outbound_date, inbound_date= inbound_date )

        except:
            print(f"No direct Flights Available to {destinationIATA}")
                

               



