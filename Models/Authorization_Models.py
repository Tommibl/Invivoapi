from dataclasses import dataclass
from urllib.parse import urlencode
class RequestDataVerification:
    def __init__(self):
        self.requestBody =  {
            "PhoneNumber": "77072777313",
            "CountryCode": "KZ",
            "DeviceId": "1be1d46a62ac645e",
            "DeviceToken": "eSLRdbuRT4SPQ5Nc81EBoF:APA91bEKsHAJOuO5reLyWXR1vDjtbnVnjd4sV8-ddQsaU8bQ8HjM2JgjM1az7oRGcyKK96y7_osIORKBndaujE6TLxf7PWFj3BYskldXji0bx85hAVyKtU8rrK1Bc3oy3MDUAUiA3nUj",
            "OperatingSystem": "Android",
            "PhoneVersion": "12",
            "AppVersion": "171 3.0.1",
            "Lat": "43.2498264",
            "Lon": "76.9201907"
        }
class ResponseDataVerification:
    def __init__(self, verificationToken, resendToken, address):
        self.verificationToken = verificationToken
        self.resendToken = resendToken
        self.address = address
    def __repr__(self):
        return f"User(verificationToken={self.verificationToken}, resendToken={self.resendToken}, address={self.address})"
@dataclass
class ResponseDataVerification:
    verification_token: str
    resend_token: str
    address: str
class RequestDataToken:
    def __init__(self, verificationToken):
        self.requestBody = {
            'grant_type': 'verification_token',
            'client_id': 'mobile-client',
            'client_secret': 'de4c3427-9c00-4d28-aa1b-a5ac1d8bd3f2',
            'username': '77072777313',
            'verification_token': verificationToken
        }
    def get_encoded_body(self):
        return urlencode(self.requestBody)
