import requests

class Language():

    def readFile(self):
        try:
            file_employee = open("src/empleados.txt", "r", encoding="UTF-8")
            self.data_file = file_employee.readlines()
            file_employee.close()
        except:
            print("ERROR: No se pudo acceder al archivo")
        else:
            return self.fileToJson()

    def fileToJson(self):
        self.languages = []
        language_id = self.getId()
        for language in self.data_file:
            language = language.strip("\n").split(", ")
            # Language Data
            language_code = language[3][0:3:1].upper()
            language_name = language[3]
            # Json
            language_json = {"id_language":language_id, "code": language_code, "name": language_name}
            self.languages.append(language_json)
            language_id += 1
        return self.languages

    def getId(self):
        api_url = "http://localhost:8080/Country/getCountry"
        response = requests.get(api_url)
        try: 
            id = response.json()[0]["id_language"]
        except:
            id = 1
        finally:
            return int(id)
