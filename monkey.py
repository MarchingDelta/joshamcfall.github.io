import RescueAnimal

class Monkey(RescueAnimal):
    species = ""
    tail_length = 0.0
    height = 0.0
    body_length = 0.0

    def __init__(self, name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, species, tail_length, height, body_length):
        super().__init__(name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        self.species = species
        self.tail_length = tail_length
        self.height = height
        self.body_length = body_length

    def __str__(self):
        return f"Name: {self.name}\nAnimal Type: {self.animal_type}\nGender: {self.gender}\nAge: {self.age}\nWeight: {self.weight}\nAcquisition Date: {self.acquisition_date}\nAcquisition Country: {self.acquisition_country}\nTraining Status: {self.training_status}\nReserved: {self.reserved}\nIn Service Country: {self.in_service_country}\nSpecies: {self.species}\nTail Length: {self.tail_length}\nHeight: {self.height}\nBody Length: {self.body_length}"

#   getters
    def get_body_length(self):
        return self.body_length

    def get_species(self):
        return self.species

    def get_tail_length(self):
        return self.tail_length

    def get_height(self):
        return self.height

    def set_species(self, species):
        while species == "" or species == None:
            print("Species cannot be empty. Please enter a valid species.")
            species = input("Enter the monkey's species: ")
        self.species = species
        

#   setters
    def set_tail_length(self, tail_length):
        while tail_length <= 0 or tail_length == None:
            print("Tail length cannot be negative or 0. Please enter a valid tail length.")
            tail_length = float(input("Enter the monkey's tail length: "))
        self.tail_length = tail_length

    def set_height(self, height):
        while height <= 0 or height == None:
            print("Height cannot be negative or 0. Please enter a valid height.")
            height = float(input("Enter the monkey's height: "))
        self.height = height

    def set_body_length(self, body_length):
        while body_length <= 0 or body_length == None:
            print("Body length cannot be negative or 0. Please enter a valid body length.")
            body_length = float(input("Enter the monkey's body length: "))
        self.body_length = body_length
