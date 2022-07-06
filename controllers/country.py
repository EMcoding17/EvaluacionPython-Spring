import requests

class Country():
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
        country_id = self.getId()
        for country in self.data_file:
            country = country.strip("\n").split(", ")
            # CountryData
            country_code = country[2][0:3:1].upper()
            country_name = country[2]
            # Json
            self.country_json = {"id_country": country_id,"code": country_code, "name": country_name}
            self.postCountry()
            country_id += 1
    
    def postCountry(self):
        api_url = "http://localhost:8080/Country/createCountry"
        response = requests.post(api_url, json=self.country_json)
        response.json()
        print("Country-Insert: ", response.status_code)

    def getId(self):
        api_url = "http://localhost:8080/Country/getCountry"
        response = requests.get(api_url)
        try: 
            id = response.json()[0]["id_country"]
        except:
            id = 1
        finally:
            return int(id)
