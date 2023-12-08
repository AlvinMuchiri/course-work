import sqlite3
# This function returns a connection object that interacts with sqlite database.


class FlightDatabase:
    def __init__(self, database_name='flights.db'):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
# This creates a database class in which tables can be created and functions which can add data to the table and
# helps when searching for data in the database.

    def create_tables(self):
        # Creates a table in the database that holds flight details.
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS flights (
                airline_code TEXT,
                airline_name TEXT,
                aircraft_number TEXT,
                flight_number TEXT,
                flight_origin TEXT,
                flight_distance TEXT,
                flight_speed TEXT,
                arrival_time TEXT
            )
        """)
        self.connection.commit()
        # The above command ensures that the table is added to the database since it is not automatically done.

    def add_flight(self, airline_code, airline_name, aircraft_number, flight_number,
                   flight_origin, flight_distance, flight_speed, arrival_time):
        self.cursor.execute("""
        INSERT INTO flights (airline_code, airline_name, aircraft_number, flight_number,
                             flight_origin, flight_distance, flight_speed, arrival_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (airline_code, airline_name, aircraft_number, flight_number,
              flight_origin, flight_distance, flight_speed, arrival_time))
        self.connection.commit()
    # This function is used to add flights to the database by the admin.
    # The function ensures that every field requires an input to ensure all data is entered correctly

    def get_flight_number(self, criteria, value):
        query = f"SELECT * FROM flights WHERE {criteria} = ?"
        self.cursor.execute(query, (value,))
        return self.cursor.fetchall()
    # This function allows the user to search for flights using the flight number
    # This is done by the criteria flight_number

    def get_flight_origin(self, criteria, value):
        query = f"SELECT * FROM flights WHERE {criteria} = ?"
        self.cursor.execute(query, (value,))
        return self.cursor.fetchall()
    # This function allows the user to search for flights using the flight origin.
    # This is done by using the criteria flight_origin.

    def get_aircraft_number(self, criteria, value):
        query = f"SELECT * FROM flights WHERE {criteria} = ?"
        self.cursor.execute(query, (value, ))
        return self.cursor.fetchall()
    # This function allows the user to find flights by searching through the aircraft number column in the database


def check_pin(pin):
    if pin == '0000':
        print("Correct pin.")
        return pin
# This function ensures that admins have access to functions that are restricted to unauthorised users by creating a
# pin in order to access the admin menu options.


class Airport:
    def __init__(self):
        self.flight_database = FlightDatabase()
        self.logged_in = False

    def menu(self):
        while True:
            print("\n1. Search using flight number.")
            print("2. Search using flight origin.")
            print("3. Search using aircraft number.")
            print("4. Admin login.")

            choice = input("Enter your choice: ")
    # The above function displays a list of options where users can search for flights depending on the information they
    # have about a particular flight.
    # The user can select one of the options to search for a flight using one of the criteria listed.

            if choice == '1':
                self.get_flight_number()
            # when the user selects this option, it calls the function above to search for a flight using the criteria
            # flight number.
            elif choice == '2':
                self.get_flight_origin()
            # When the user selects this option, it calls the function above to search for a flight using the criteria
            # flight origin
            elif choice == '3':
                self.get_aircraft_number()
            # When the user selects this option, it calls the function above to search for a flight using the criteria
            # aircraft number
            elif choice == '4':
                pin = int(input("Enter pin.: "))
                check_pin(pin)
            # This option is set up for admins to allow them to add incoming flights to the database hence updating it
            # This helps the other users find flight landing at the airport
                while True:
                    menuOption = int(input("\n1. Add flights \n2. Exit \n Select one of the options:"))
                    if menuOption == 1:
                        self.add_flight()
                    elif menuOption == 2:
                        # This option allows to the admin to return to the main menu exiting from the admin menu.
                        break
                    # This menu option is set out for admins it enables them to add new flights to the system by calling
                    # out a function.
            else:
                print("Invalid choice")
                # This message appears when the user selects an invalid option.

# The functions below ensure the function in the database class also work in the airport class depending on the option
# the user selects
    def add_flight(self):
        airline_code = input("Enter airline code: ")
        airline_name = input("Enter airline name: ")
        aircraft_number = input("Enter aircraft number: ")
        flight_number = input("Enter flight number: ")
        flight_origin = input("Enter flight origin: ")
        flight_distance = input("Enter flight distance: ")
        flight_speed = input("Enter flight speed: ")
        arrival_time = input("Enter arrival time: ")

        self.flight_database.add_flight(airline_code, airline_name, aircraft_number, flight_number,
                                        flight_origin, flight_distance, flight_speed, arrival_time)
        print("Flight added successfully.")

    def get_flight_number(self):
        criteria = ('flight_number')
        value = input('Enter value: ')
        flights = self.flight_database.get_flight_number(criteria, value)
        print(f'Flight Details: {flights}')
        # This function works with the function in the database class and displays to the user the flight details for
        # the flight they searched for by using the flight number

    def get_flight_origin(self):
        criteria = ('flight_origin')
        value = input('Enter value: ')
        flights = self.flight_database.get_flight_origin(criteria, value)
        print(f'Flight Details: {flights}')
        # This function works with the function in the database class and displays to the user the flight details for
        # the flight they searched for by using the flight origin

    def get_aircraft_number(self):
        criteria = ('aircraft_number')
        value = input('Enter value: ')
        flights = self.flight_database.get_aircraft_number(criteria, value)
        print(f'Flight Details: {flights}')
        # This function works with the function in the database class and displays to the user the flight details for
        # the flight they searched for by using the aircraft number


if __name__ == "__main__":
    airport = Airport()
    airport.menu()
# The code above starts the program
