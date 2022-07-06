import requests

class Airport():
    def __init__(self):
        self.path_file_employee = "src/empleados.txt"
        self.readFile()

    def readFile(self):
        try:
            file_employee = open(self.path_file_employee, "r", encoding="UTF-8")
            self.data_file = file_employee.readlines()
            file_employee.close()
        except:
            print("ERROR: No se pudo acceder al archivo")
        else:
            return self.fileToJson()

    def fileToJson(self):
        try:
            airport_id = self.getIdAirport()
            for airport in self.data_file:
                airport = airport.strip("\n").split(", ")
                # Airport Data
                airport_name = airport[4]
                # Country Id
                country = airport[2][0:3:1].upper()
                # Json
                id_country = {"id_country": self.getIdCountry(country)}
                self.airport_json = {"id_airport": airport_id, "name": airport_name, "country": id_country}
                self.postAirport()
                airport_id += 1
        except:
            print("Error: No se puede llenar la tabla Airport, intente llenando la tabla Country primero")
    
    def postAirport(self):
        api_url = "http://localhost:8080/Airport/createAirport"
        response = requests.post(api_url, json=self.airport_json)
        response.json()
        print("Airport-Insert: ", response.status_code)
    
    def getIdAirport(self):
        api_url = "http://localhost:8080/Airport/getAirport"
        response = requests.get(api_url)
        try: 
            id = response.json()[0]["id_airport"]
        except:
            id = 1
        finally:
            return int(id)
    
    def getIdCountry(self, code):
        api_url = "http://localhost:8080/Country/getCountry"
        response = requests.get(api_url)
        for data in response.json():
            if data["code"] == code:
                id = data["id_country"]
                return id
