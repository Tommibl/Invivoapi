class Service:
    def __init__(self, provider_type, provider, code, name, amount, additional_service=None):
        self.provider_type = provider_type
        self.provider = provider
        self.code = code
        self.name = name
        self.amount = amount
        self.additional_service = additional_service

class AdditionalService:
    def __init__(self, provider_type, provider, code, name, amount):
        self.provider_type = provider_type
        self.provider = provider
        self.code = code
        self.name = name
        self.amount = amount

class Response:
    def __init__(self, value, code=None, success=True, message="", failure=False, exception=None):
        self.id = value.get("id")
        self.provider_type = value.get("providerType")
        self.provider = value.get("provider")
        self.device_id = value.get("deviceId")
        self.user_id = value.get("userId")
        self.patient_id = value.get("patientId")
        self.doctor_id = value.get("doctorId")
        self.code = value.get("code")
        self.operation_id = value.get("operationId")
        self.in_house = value.get("inHouse")
        self.address = value.get("address")
        self.punkt = value.get("punkt")
        self.is_for_another_patient = value.get("isForAnotherPatient")
        self.payment_method = value.get("paymentMethod")
        self.payment_card_type = value.get("paymentCardType")
        self.payment_id = value.get("paymentId")
        self.provider_order_id = value.get("providerOrderId")
        self.lab_view = value.get("labView")
        self.provider_order_number = value.get("providerOrderNumber")
        self.status = value.get("status")
        self.total = value.get("total")
        self.created = value.get("created")
        self.patient = value.get("patient")
        self.doctor = value.get("doctor")
        self.use_bonuses = value.get("useBonuses")
        self.type = value.get("type")
        self.selected_services = [Service(**service) for service in value.get("selectedServices", [])]
        self.additional_services = [Service(**service) for service in value.get("additionalServices", [])]
        self.campaign = value.get("campaign")
        self.optional = value.get("optional")
        self.bonus_amount = value.get("bonusAmount")
        self.spent_bonus = value.get("spentBonus")
        self.region_code = value.get("regionCode")
        self.finish_date = value.get("finishDate")
        self.author_user_id = value.get("authorUserId")
        self.author = value.get("author")
        self.country_code = value.get("countryCode")
        self.planned_time = value.get("plannedTime")
        self.is_insurance = value.get("isInsurance")
        self.debt = value.get("debt")
        self.code = code
        self.success = success
        self.message = message
        self.failure = failure
        self.exception = exception

    def __str__(self):
        return f"Response(id={self.id}, provider_type={self.provider_type}, provider={self.provider}, total={self.total})"
class RequestData:
    request_json = {
        "id": "",
        "deviceId": "fqEOebecT7u2nq1BNdCRGa:APA91bHuIhlf2zziWrKHJrDoqmTFGxn_kE-TgbxLEblFTPop4Yoy1wu5bBq3jwLYR_PCCHMxxX9hS5717InARxcwDhBh7YzPvEOJqtiMN879AyHXvSc2dAMjjNXv6lNXMymOiYGB1Vte",
        "inHouse": False,
        "regionCode": "KZ_R_4",
        "services": [
            {
                "providerType": "Lab",
                "provider": "Invivo",
                "code": "Q890",
                "name": "IgE к лидокаину 10%",
                "amount": 4000.0,
                "additionalService": "SMS1"
            },
            {
                "providerType": "Lab",
                "provider": "Invivo",
                "code": "Q8006",
                "name": "17-ОН прогестерон в крови (ВЭЖХ-МС/МС)",
                "amount": 16100.0,
                "additionalService": "SMS1"
            }
        ],
        "additionalService": [
            {
                "providerType": "Lab",
                "provider": "Invivo",
                "code": "SMS1",
                "name": "Смс оповещение",
                "amount": 100.0
            },
            {
                "providerType": "Lab",
                "provider": "Invivo",
                "code": "Q897",
                "name": "Забор биоматериала",
                "amount": 1000.0
            },
            {
                "providerType": "Lab",
                "provider": "Invivo",
                "code": "SMS1",
                "name": "Смс оповещение",
                "amount": 100.0
            }
        ],
        "campaignCode": "qqwd",
        "couponCode": "",
        "isForAnotherPatient": False
    }