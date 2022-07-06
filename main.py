
from controllers.airport import Airport
from controllers.country import Country
from controllers.employee import Employee

class Main():
    def __init__(self):
        self.postCountry()
        self.postAirport()
        self.postEmployee()

    def postEmployee(self):
        Employee()

    def postCountry(self):
        Country()

    def postAirport(self):
        Airport()

Main()
