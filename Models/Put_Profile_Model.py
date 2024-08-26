from typing import Any
from dataclasses import dataclass
class Request_Data_Put_Profile:
    def __init__(self):
        self.requestBody = {
            "id": "6684c9678320ab8f451a8536",
            "phoneNumber": "77072777313",
            "description": "",
            "uin": "232323232323",
            "firstName": "Революс",
            "midName": "",
            "lastName": "Манифестов",
            "birthDate": "1995-07-03T12:00:00",
            "sex": 0,
            "type": 0,
            "role": "client",
            "isResident": True,
            "avatarPath": "",
            "isSmsSubscribed": True,
            "isPushSubscribed": True,
            "isEmailSubscribed": True,
            "email": "tsgsh@mail.ru"
        }
@dataclass
class Request_Put_Profile:
    id: str
    phoneNumber: str
    description: str
    uin: str
    firstName: str
    midName: str
    lastName: str
    birthDate: str
    sex: int
    type: int
    role: str
    isResident: bool
    avatarPath: str
    isSmsSubscribed: bool
    isPushSubscribed: bool
    isEmailSubscribed: bool
    email: str
    @staticmethod
    def from_request_profile(obj: Any) -> 'Request_Data_Put_Profile':
        _id = str(obj.get("id"))
        _phoneNumber = str(obj.get("phoneNumber"))
        _description = str(obj.get("description"))
        _uin = str(obj.get("uin"))
        _firstName = str(obj.get("firstName"))
        _midName = str(obj.get("midName"))
        _lastName = str(obj.get("lastName"))
        _birthDate = str(obj.get("birthDate"))
        _sex = int(obj.get("sex"))
        _type = int(obj.get("type"))
        _role = str(obj.get("role"))
        _isResident = bool(obj.get("isResident"))
        _avatarPath = str(obj.get("avatarPath"))
        _isSmsSubscribed = bool(obj.get("isSmsSubscribed"))
        _isPushSubscribed = bool(obj.get("isPushSubscribed"))
        _isEmailSubscribed = bool(obj.get("isEmailSubscribed"))
        _email = str(obj.get("email"))
        return Request_Data_Put_Profile(_id, _phoneNumber, _description, _uin, _firstName,
                    _midName, _lastName, _birthDate, _sex, _type, _role,
                    _isResident, _avatarPath, _isSmsSubscribed, _isPushSubscribed,
                    _isEmailSubscribed, _email)