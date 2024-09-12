
class RegisterData:
    def __init__(self, useBonus=False, doctorPhoneNumber="", doctorId="", id="", lon="", address="", punktId="", type="laboratory", lat=""):
        self.useBonus = useBonus
        self.doctorPhoneNumber = doctorPhoneNumber
        self.doctorId = doctorId
        self.id = id
        self.lon = lon
        self.address = address
        self.punktId = punktId
        self.type = type
        self.lat = lat

    def to_dict(self):
        return {
            "useBonus": str(self.useBonus).lower(),  # Преобразуем булево значение в строку "false" или "true"
            "doctorPhoneNumber": self.doctorPhoneNumber,
            "doctorId": self.doctorId,
            "id": self.id,
            "lon": self.lon,
            "address": self.address,
            "punktId": self.punktId,
            "type": self.type,
            "lat": self.lat
        }
class RegisterDataRequest:
    def __init__(self):
        self.register_data = None
        self.request = [
            {
                "useBonus": False,
                "doctorPhoneNumber": "",
                "doctorId": "",
                "id": "66d804609330d8fce81f16c7",
                "lon": "",
                "address": "",
                "punktId": "",
                "type": "laboratory",
                "lat": ""
            }
    ]
        register_data = RegisterData(id="66d804609330d8fce81f16c7", type="laboratory", useBonus=False,
                                        doctorPhoneNumber="", lon="", address="", punktId="",lat="")
        print(register_data.to_dict())
