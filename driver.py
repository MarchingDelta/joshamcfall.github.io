from collections import defaultdict
import datetime
import os
import sqlite3
import subprocess
import sys
import Monkey, Dog # type: ignore

# Global cache for animal data using search_id as the key and access count as the value
animal_cache = defaultdict(int)  

#   connects to db and returns database and cursor objects
def connect_to_database():
    try:
        database = sqlite3.connect('RescueAnimals.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    cursor = database.cursor()
    return database, cursor

#   creates tables in db if they don't already exist
def create_tables():
    database, cursor = connect_to_database()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Dogs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        search_id INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        weight FLOAT NOT NULL,
                        acquisition_date TEXT NOT NULL,
                        acquisition_country TEXT NOT NULL,
                        training_status BOOLEAN NOT NULL,
                        reserved BOOLEAN NOT NULL,
                        in_service_country TEXT NOT NULL,
                        breed TEXT NOT NULL
                        
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Monkeys (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        search_id INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        weight FLOAT NOT NULL,
                        acquisition_date TEXT NOT NULL,
                        acquisition_country TEXT NOT NULL,
                        training_status BOOLEAN NOT NULL,
                        reserved BOOLEAN NOT NULL,
                        in_service_country TEXT NOT NULL,
                        species TEXT NOT NULL,
                        tail_length FLOAT NOT NULL,
                        height FLOAT NOT NULL,
                        body_length FLOAT NOT NULL
                    )''')
    database.commit()
    database.close()

def cache_data(search_id):
    while len(animal_cache) >= 100:  # Limit cache size to 100 entries
        # Remove the least recently accessed item
        least_recent = min(animal_cache, key=animal_cache.get)
        del animal_cache[least_recent]
    animal_cache[search_id] += 1  # Cache the search ID, increment search count


def search_animal():
    search_id = int(input("Enter the animal's search ID: "))
    database, cursor = connect_to_database()

    #check cache first before querying db
    if animal_cache.get(search_id):
        #gets most recent data from db in case of updates since last search
        cursor.execute("SELECT * FROM Dogs, Monkeys WHERE search_id = ?", (search_id,))
        results = cursor.fetchone()
        #in case something goes wrong 
        if results is None:
            print("No animal found with that search ID.")
            database.close()
            return
              
        print(f"Name: {results[1]},\nAcquisition Date: {results[5]}, \nTraining Status: {results[7]}, \nReserved: {results[8]}, \nBreed/Species: {results[10]}")
        database.close()
        cache_data(search_id)  # Update cache access count
        return

    #query database if not found in cache
    cursor.execute("SELECT * FROM Dogs, Monkeys WHERE search_id = ?", (search_id,))
    results = cursor.fetchone()

    #in case something goes wrong 
    if results is None:
        print("No animal found with that search ID.")
        database.close()
        return
    
    print(f"Name: {results[1]},\nAcquisition Date: {results[5]}, \nTraining Status: {results[7]}, \nReserved: {results[8]}, \nBreed/Species: {results[10]}")
    cache_data(search_id)
    database.close()

#   prints menu options 
def print_menu():
    print("\t\t\tRescue Animal Management System")
    print('---------------------------------------------')
    print("[1] Manually add a Dog")
    print("[2] Manually add a Monkey")
    print("[3] Display all Dogs")
    print("[4] Display all Monkeys")
    print("[5] Display all animals that aren't reserved")
    print("[6] Search for an animal")
    print("[7] Remove an animal")
    print("[q] Exit")
    print('---------------------------------------------')
    print(f"Total Dogs: {count_dogs()}")
    print(f"Reserved Dogs: {count_reserved_dogs()}")
    print(f"Total Monkeys: {count_monkeys()}")
    print(f"Reserved Monkeys: {count_reserved_monkeys()}")

#   counts number of reserved dogs in db
def count_reserved_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Dogs WHERE reserved = 1")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   counts number of reserved monkeys in db
def count_reserved_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Monkeys WHERE reserved = 1")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   prints all monkeys in db
def print_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Monkeys")
    monkeys = cursor.fetchall()
    if not monkeys:
        print("No monkeys found in the database.")
        database.close()
        return 
    for monkey in monkeys:
        print(f"ID: {monkey[0]},\nName: {monkey[1]},\nGender: {monkey[2]},\nAge: {monkey[3]},\nWeight: {monkey[4]},\nAcquisition Date: {monkey[5]},\nAcquisition Country: {monkey[6]},\nTraining Status: {monkey[7]},\nReserved: {monkey[8]},\nIn Service Country: {monkey[9]},\nSpecies: {monkey[10]},\nTail Length: {monkey[11]},\nHeight: {monkey[12]},\nBody Length: {monkey[13]}")  
    database.close()

#   prints all dogs in db
def print_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Dogs")
    dogs = cursor.fetchall()
    if not dogs:
        print("No dogs found in the database.")
        database.close()
        return
    for dog in dogs:
        print(f"ID: {dog[0]},\nName: {dog[1]},\nGender: {dog[2]},\nAge: {dog[3]},\nWeight: {dog[4]},\nAcquisition Date: {dog[5]},\nAcquisition Country: {dog[6]},\nTraining Status: {dog[7]},\nReserved: {dog[8]},\nIn Service Country: {dog[9]},\nBreed: {dog[10]}")  
    database.close()

#  prints all unreserved animals in db
def print_unreserved_animals():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Dogs WHERE reserved = 0")
    unreserved_dogs = cursor.fetchall()
    if not unreserved_dogs:
        print("No unreserved dogs found in the database.")
    for dog in unreserved_dogs:
        print(f"ID: {dog[0]},\nName: {dog[1]},\nGender: {dog[2]},\nAge: {dog[3]},\nWeight: {dog[4]},\nAcquisition Date: {dog[5]},\nAcquisition Country: {dog[6]},\nTraining Status: {dog[7]},\nReserved: {dog[8]},\nIn Service Country: {dog[9]},\nBreed: {dog[10]}")
    cursor.execute("SELECT * FROM Monkeys WHERE reserved = 0")
    unreserved_monkeys = cursor.fetchall()
    if not unreserved_monkeys:
        print("No unreserved monkeys found in the database.")
    for monkey in unreserved_monkeys:
        print(f"ID: {monkey[0]},\nName: {monkey[1]},\nGender: {monkey[2]},\nAge: {monkey[3]},\nWeight: {monkey[4]},\nAcquisition Date: {monkey[5]},\nAcquisition Country: {monkey[6]},\nTraining Status: {monkey[7]},\nReserved: {monkey[8]},\nIn Service Country: {monkey[9]},\nSpecies: {monkey[10]},\nTail Length: {monkey[11]},\nHeight: {monkey[12]},\nBody Length: {monkey[13]}")
    database.close()

#   adds dog to db
def add_dog():
    dog = Dog("", "", "", 0, 0.0, "", "", False, False, "", "") #empty dog object to use setters for validation
    name = input("Enter the dog's name: ")
    dog.set_name(name)
    gender = input("Enter the dog's gender: ")
    dog.set_gender(gender)
    age = int(input("Enter the dog's age: "))
    dog.set_age(age)
    weight = float(input("Enter the dog's weight: "))
    dog.set_weight(weight)
    acquisition_date = input("Enter the dog's acquisition date: ")
    dog.set_acquisition_date(acquisition_date)
    acquisition_country = input("Enter the dog's acquisition country: ")
    dog.set_acquisition_country(acquisition_country)
    training_status = bool(input("Enter the dog's training status (True/False): "))
    dog.set_training_status(training_status)
    reserved = bool(input("Enter the dog's reserved status (True/False): "))
    dog.set_reserved(reserved)
    in_service_country = input("Enter the dog's in-service country: ")
    dog.set_in_service_country(in_service_country)
    breed = input("Enter the dog's breed: ")
    dog.set_breed(breed)
    database, cursor = connect_to_database()

    search_id = abs(hash(datetime.now().strftime("%Y%m%d%H%M%S"))) 
    if search_id > 99999999: #limits search_id to 8 digits to prevent possible overflow issues in db
        search_id = search_id % 100000000
    
    cursor.execute("INSERT INTO Dogs (search_id, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, breed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (search_id, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, breed))
    database.commit()

#   adds monkey to db 
def add_monkey():
    #empyt monkey object to use setters for validation
    monkey = Monkey.Monkey("", "", "", 0, 0.0, "", "", False, False, "", "", 0.0, 0.0, 0.0) 

    name = input("Enter the monkey's name: ")
    monkey.set_name(name)
    gender = input("Enter the monkey's gender: ")
    monkey.set_gender(gender)
    age = int(input("Enter the monkey's age: "))
    monkey.set_age(age)
    weight = float(input("Enter the monkey's weight: "))
    monkey.set_weight(weight)
    acquisition_date = input("Enter the monkey's acquisition date: ")
    monkey.set_acquisition_date(acquisition_date)
    acquisition_country = input("Enter the monkey's acquisition country: ")
    monkey.set_acquisition_country(acquisition_country)
    training_status = bool(input("Enter the monkey's training status (True/False): "))
    monkey.set_training_status(training_status)
    reserved = bool(input("Enter the monkey's reserved status (True/False): "))
    monkey.set_reserved(reserved)
    in_service_country = input("Enter the monkey's in-service country: ")
    monkey.set_in_service_country(in_service_country)
    species = input("Enter the monkey's species: ")
    monkey.set_species(species)
    tail_length = float(input("Enter the monkey's tail length: "))
    monkey.set_tail_length(tail_length)
    height = float(input("Enter the monkey's height: "))
    monkey.set_height(height)
    body_length = float(input("Enter the monkey's body length: "))
    monkey.set_body_length(body_length)
    database, cursor = connect_to_database()
    search_id = abs(hash(datetime.now().strftime("%Y%m%d%H%M%S"))) 
    if search_id > 99999999:
        search_id = search_id % 100000000
    
    cursor.execute("INSERT INTO Monkeys (search_id, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, species, tail_length, height, body_length) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (search_id, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, species, tail_length, height, body_length))
    database.commit()

#   removes animal from db based on search_id
def remove_animal():
    search_id = int(input("Enter the animal's search ID to remove: "))
    database, cursor = connect_to_database()
    if search_id in animal_cache:
        del animal_cache[search_id]  # Remove from cache if it exists
    #no need for a check since the delete query will do nothing if the search_id doesn't exist 
    cursor.execute("DELETE FROM Dogs WHERE search_id = ?", (search_id,))
    cursor.execute("DELETE FROM Monkeys WHERE search_id = ?", (search_id,))
    database.commit()
    database.close()
    print(f"Animal with search ID {search_id} has been removed from the database.")

#   clears screen regardless of os
def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

#   counts number of dogs in db
def count_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Dogs")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   counts number of monkeys in db
def count_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Monkeys")
    count = cursor.fetchone()[0]
    database.close()
    return count

def main():
    connect_to_database()
    print("Connected to the database successfully.")
    create_tables()
    print("Tables created successfully.")
    #input("debug point")
    clear_screen()
    print_menu()

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_dog()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '2':
            add_monkey()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '3':
            print_dogs()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '4':
            print_monkeys()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '5':
            print_unreserved_animals()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '6':
            search_animal()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '7': #untested 
            remove_animal()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            print("Press any key to continue...")
            input()
            clear_screen()
            print_menu()


main()
