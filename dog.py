
import RescueAnimal


class Dog(RescueAnimal):
    breed = ""
    
    def __init__(self, name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, breed):
        super().__init__(name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        self.breed = breed

    #database query should pull data 
    def __str__(self):
        return f"Name: {self.name}\nAnimal Type: {self.animal_type}\nGender: {self.gender}\nAge: {self.age}\nWeight: {self.weight}\nAcquisition Date: {self.acquisition_date}\nAcquisition Country: {self.acquisition_country}\nTraining Status: {self.training_status}\nReserved: {self.reserved}\nIn Service Country: {self.in_service_country}\nBreed: {self.breed}"

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        while breed == "" or breed == None:
            print("Breed cannot be empty. Please enter a valid breed.")
            breed = input("Enter the dog's breed: ")
        self.breed = breed