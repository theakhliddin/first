class Country:
    def __init__(self, name):
        self._name = name
        self._environment = 0
        self._economy = 0
        self._culture = 0
        self._healthcare = 0
        self._education = 0

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
    
    def set_environment(self, value):
        if 0 <= value <= 100:
            self._environment = value
        else:
            raise ValueError("Environment value must be between 0 and 100")
        
    def set_economy(self, value):
        if 0 <= value <= 100:
            self._economy = value
        else:
            raise ValueError("Economy value must be between 0 and 100")
    
    def set_culture(self, value):
        if 0 <= value <= 100:
            self._culture = value
        else:
            raise ValueError("Culture value must be between 0 and 100")
    
    def set_healthcare(self, value):
        if 0 <= value <= 100:
            self._healthcare = value
        else:
            raise ValueError("Healthcare value must be between 0 and 100")
    
    def set_education(self, value):
        if 0 <= value <= 100:
            self._education = value
        else:
            raise ValueError("Education value must be between 0 and 100")
    
