import requests

from controllers.language import Language

class Employee():
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
        employee_id = self.getId()
        for employee in self.data_file:
            employee = employee.strip("\n").split(", ")
            employee_surname = employee[1]
            employee_firstname = employee[0]
            code_language = employee[3][0:3:1].upper()
            language_data = self.getIdLanguage(code_language)
            name_airport = employee[4]
            id_airport = self.getIdAirport(name_airport)
            self.employee_json = {"id_employee": employee_id, "surname": employee_surname, "firstname": employee_firstname, "language": language_data, "airport": id_airport}
            self.postEmployee()
            employee_id += 1

    def getIdLanguage(self, code):
        list_lenguages = Language().readFile()
        for language in list_lenguages:
            if language["code"] == code:
                id = [{"id_language" : language["id_language"], "code": language["code"], "name": language["name"]}]
                return id

    def getIdAirport(self, name):
        api_url = "http://localhost:8080/Airport/getAirport"
        response = requests.get(api_url)
        for data in response.json():
            if data["name"] == name:
                id = {"id_airport" : data["id_airport"]}
                return id
    
    def postEmployee(self):
        api_url = "http://localhost:8080/apiv1/clientes/add"
        response = requests.post(api_url, json=self.employee_json)
        response.json()
        print("Employee-Insert: ",response.status_code)

    def getId(self):
        api_url = "http://localhost:8080/Employee/getEmployee"
        response = requests.get(api_url)
        try: 
            id = response.json()[0]["id_country"]
        except:
            id = 1
        finally:
            return int(id)
