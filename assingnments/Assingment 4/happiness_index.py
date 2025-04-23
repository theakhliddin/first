class Country:
    """
    A class to represent a country and its happiness factors.
    All factors are stored as private attributes with getter and setter methods.
    """
    def __init__(self, name):
        self._name = name
        self._environment = 0
        self._economy = 0
        self._culture = 0
        self._healthcare = 0
        self._education = 0

    # Getter methods
    def get_name(self):
        return self._name

    def get_environment(self):
        return self._environment

    def get_economy(self):
        return self._economy

    def get_culture(self):
        return self._culture

    def get_healthcare(self):
        return self._healthcare

    def get_education(self):
        return self._education

    # Setter methods
    def set_environment(self, value):
        if 0 <= value <= 100:
            self._environment = value
        else:
            raise ValueError("Environment factor must be between 0 and 100")

    def set_economy(self, value):
        if 0 <= value <= 100:
            self._economy = value
        else:
            raise ValueError("Economy factor must be between 0 and 100")

    def set_culture(self, value):
        if 0 <= value <= 100:
            self._culture = value
        else:
            raise ValueError("Culture factor must be between 0 and 100")

    def set_healthcare(self, value):
        if 0 <= value <= 100:
            self._healthcare = value
        else:
            raise ValueError("Healthcare factor must be between 0 and 100")

    def set_education(self, value):
        if 0 <= value <= 100:
            self._education = value
        else:
            raise ValueError("Education factor must be between 0 and 100")


class HappinessMeter:
    """
    A class to manage and measure happiness indices for multiple countries.
    """
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        """Add a country to the list of countries being measured."""
        self.countries.append(country)

    def measure_happiness(self):
        """
        Calculate and return the happiness index for each country.
        The happiness index is the average of all factors.
        """
        happiness_indices = {}
        for country in self.countries:
            total = (country.get_environment() + 
                    country.get_economy() + 
                    country.get_culture() + 
                    country.get_healthcare() + 
                    country.get_education())
            average = total / 5
            happiness_indices[country.get_name()] = round(average, 2)
        return happiness_indices


def main():
    """
    Main function to run the Happiness Index Measurement System.
    Handles user input and displays results.
    """
    happiness_meter = HappinessMeter()
    
    try:
        num_countries = int(input("Enter the number of countries: "))
        if num_countries <= 0:
            raise ValueError("Number of countries must be positive")
        
        for i in range(1, num_countries + 1):
            name = input(f"Enter the name of country {i}: ")
            country = Country(name)
            
            # Get all factors for the country
            factors = {
                'environment': country.set_environment,
                'economy': country.set_economy,
                'culture': country.set_culture,
                'healthcare': country.set_healthcare,
                'education': country.set_education
            }
            
            for factor, setter in factors.items():
                while True:
                    try:
                        value = int(input(f"Enter {factor} factor (0-100): "))
                        setter(value)
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
            
            happiness_meter.add_country(country)
        
        # Measure and display happiness indices
        print("\nHappiness Measurement:")
        happiness_indices = happiness_meter.measure_happiness()
        for country, index in happiness_indices.items():
            print(f"{country} : {index}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main() 