import requests

class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self, data_to_update, API, header_file):
        self.data = data_to_update
        self.api = API
        self.header = header_file
        self.update_data()
       
        

    def update_data(self):
        try:
            requests.put(url= self.api, json= self.data, headers= self.header)
        except:
            print("IATA Code already available")

        