class Country:
    """
    Represents a country with various happiness factors.
    All attributes are private and accessed via getter and setter methods to enforce encapsulation.
    """

    def __init__(self, name):
        
        #Initializes a Country object with a name and default factor values set to 0.  
        self.__name = name
        self.__environment = 0
        self.__economy = 0
        self.__culture = 0
        self.__healthcare = 0
        self.__education = 0

    #  Getter Methods 

    def get_name(self):
        #Returns the name of the country.2
        return self.__name

    def get_environment(self):
        #Returns the environment factor of the country.
        return self.__environment

    def get_economy(self):
        #Returns the economy factor of the country.
        return self.__economy

    def get_culture(self):
       #Returns the culture factor of the country.
        return self.__culture

    def get_healthcare(self):
        #Returns the healthcare factor of the country.
        return self.__healthcare

    def get_education(self):
        #Returns the education factor of the country.
        return self.__education

    #  Setter Methods 

    def set_environment(self, value):
        #Sets the environment factor after validating the input.
        if 0 <= value <= 100:
            self.__environment = value
        else:
            raise ValueError("Environment must be between 0 and 100")

    def set_economy(self, value):
        #Sets the economy factor after validating the input.
        if 0 <= value <= 100:
            self.__economy = value
        else:
            raise ValueError("Economy must be between 0 and 100")

    def set_culture(self, value):
        #Sets the culture factor after validating the input.
        if 0 <= value <= 100:
            self.__culture = value
        else:
            raise ValueError("Culture must be between 0 and 100")

    def set_healthcare(self, value):
        #Sets the healthcare factor after validating the input.
        if 0 <= value <= 100:
            self.__healthcare = value
        else:
            raise ValueError("Healthcare must be between 0 and 100")

    def set_education(self, value):
        #Sets the education factor after validating the input.
        if 0 <= value <= 100:
            self.__education = value
        else:
            raise ValueError("Education must be between 0 and 100")


class HappinessMeter:
    #Manages a list of Country objects and calculates their happiness scores.
    __slots__ = ['__countries']

    def __init__(self):
        #Initializes the HappinessMeter with an empty list of countries.
        self.__countries = []

    def add_country(self, country):
        #Adds a Country object to the list.        
        self.__countries.append(country)

    def measure_happiness(self):
        #Calculates and prints the happiness score of each country in the list.            
        print("\nHappiness Measurement:")
        for country in self.__countries:
            total = (country.get_environment() + country.get_economy() +
                     country.get_culture() + country.get_healthcare() +
                     country.get_education())
            average = total / 5
            print(f"{country.get_name()} : {average:.2f}")


def main():
    """
    Main function that interacts with the user to input data for multiple countries,
    create Country objects, and use HappinessMeter to display happiness scores.
    """
    meter = HappinessMeter()

    try:
        num_countries = int(input("Enter the number of countries: "))

        for i in range(num_countries):
            print(f"\nCountry {i + 1}")
            name = input("Enter the name of the country: ")
            country = Country(name)

            # Input and set each factor using setter methods
            try:
                country.set_environment(int(input("Enter environment factor (0-100): ")))
                country.set_economy(int(input("Enter economy factor (0-100): ")))
                country.set_culture(int(input("Enter culture factor (0-100): ")))
                country.set_healthcare(int(input("Enter healthcare factor (0-100): ")))
                country.set_education(int(input("Enter education factor (0-100): ")))
            except ValueError as e:
                print("Invalid input:", e)
                continue  # Skip this country and move to the next

            # Add the country to the happiness meter
            meter.add_country(country)

        # Calculate and display happiness scores
        meter.measure_happiness()

    except ValueError:
        print("Invalid input! Please enter a valid number of countries.")


# Entry point of the script
if __name__ == "__main__":
    main()
