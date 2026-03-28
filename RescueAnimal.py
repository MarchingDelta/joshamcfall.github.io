class RescueAnimal:
    name = ""
    animal_type = ""
    gender = ""
    age = 0
    weight = 0.0
    acquisition_date = ""
    acquisition_country = ""
    training_status = ""
    reserved = False
    in_service_country = ""

    def __init__(self, name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        self.name = name
        self.animal_type = animal_type
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country

#   getters
    def get_name(self):
        return self.name
    
    def get_animal_type(self):
        return self.animal_type
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def get_weight(self):
        return self.weight
    
    def get_acquisition_date(self):
        return self.acquisition_date
    
    def get_acquisition_country(self):
        return self.acquisition_country
    
    def get_training_status(self):
        return self.training_status
    
    def get_reserved(self):
        return self.reserved
    
    def get_in_service_country(self):
        return self.in_service_country
    
#   setters
    def set_name(self, name):
        while name == "" or name == None:
            print("Name cannot be empty. Please enter a valid name.")
            name = input("Enter the animal's name: ")
        self.name = name
    
    def set_animal_type(self, animal_type):
        while animal_type == "" or animal_type == None:
            print("Animal type cannot be empty. Please enter a valid animal type.")
            animal_type = input("Enter the animal's type: ")
        self.animal_type = animal_type
    
    def set_gender(self, gender):
        while gender == "" or gender == None:
            print("Gender cannot be empty. Please enter a valid gender.")
            gender = input("Enter the animal's gender: ")
        self.gender = gender
    
    def set_age(self, age):
        while age <= 0 or age == None:
            print("Age cannot be negative or 0. Please enter a valid age.")
            age = int(input("Enter the animal's age: "))
        self.age = age
    
    def set_weight(self, weight):
        while weight <= 0 or weight == None:
            print("Weight cannot be negative or 0. Please enter a valid weight.")
            weight = float(input("Enter the animal's weight: "))
        self.weight = weight
    
    def set_acquisition_date(self, acquisition_date):
        while acquisition_date == "" or acquisition_date == None:
            print("Acquisition date cannot be empty. Please enter a valid acquisition date.")
            acquisition_date = input("Enter the animal's acquisition date: ")
        self.acquisition_date = acquisition_date
    
    def set_acquisition_country(self, acquisition_country):
        while acquisition_country == "" or acquisition_country == None:
            print("Acquisition country cannot be empty. Please enter a valid acquisition country.")
            acquisition_country = input("Enter the animal's acquisition country: ")
        self.acquisition_country = acquisition_country
    
    def set_training_status(self, training_status):
        while training_status == "" or training_status == None:
            print("Training status cannot be empty. Please enter a valid training status.")
            training_status = input("Enter the animal's training status: ")
        self.training_status = training_status
    
    def set_reserved(self, reserved):
        while isinstance(reserved, bool) == False:
            print("Reserved must be a boolean value. Please enter True or False.")
            reserved_input = input("Is the animal reserved? (True/False): ")
            if reserved_input.lower() == "true":
                reserved = True
            elif reserved_input.lower() == "false":
                reserved = False
            else:
                print("Invalid input. Please enter True or False.")
        self.reserved = reserved
    
    def set_in_service_country(self, in_service_country):
        while in_service_country == "" or in_service_country == None:
            print("In service country cannot be empty. Please enter a valid in service country.")
            in_service_country = input("Enter the animal's in service country: ")
        self.in_service_country = in_service_country

    

    