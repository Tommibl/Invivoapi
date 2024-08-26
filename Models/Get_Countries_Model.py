class ResponseDataCountries:
    def __init__(self, id, name, code, icon):
        self.id = id
        self.name = name
        self.code = code
        self.icon = icon
    def __eq__(self, other):
        if not isinstance(other, ResponseDataCountries):
            return False
        return (self.id == other.id and
                self.name == other.name and
                self.code == other.code and
                self.icon == other.icon)