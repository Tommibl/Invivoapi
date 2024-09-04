from typing import List, Optional

class Lab:
    def __init__(self,
                 id: str,
                 code: str,
                 name: str,
                 logo: str,
                 small_logo: str,
                 description: str,
                 region_code: Optional[str],
                 country_code: str,
                 is_departure: bool,
                 connection_parametr: Optional[str]):
        self.id = id
        self.code = code
        self.name = name
        self.logo = logo
        self.small_logo = small_logo
        self.description = description
        self.region_code = region_code
        self.country_code = country_code
        self.is_departure = is_departure
        self.connection_parametr = connection_parametr

    def __repr__(self):
        return f"Lab(id={self.id}, name={self.name}, country_code={self.country_code})"

class LabResult:
    def __init__(self,
                 results: List[Lab],
                 current_page: int,
                 page_count: int,
                 page_size: int,
                 row_count: int,
                 first_row_on_page: int,
                 last_row_on_page: int):
        self.results = results
        self.current_page = current_page
        self.page_count = page_count
        self.page_size = page_size
        self.row_count = row_count
        self.first_row_on_page = first_row_on_page
        self.last_row_on_page = last_row_on_page

    def __repr__(self):
        return f"LabResult(page={self.current_page}/{self.page_count}, results={len(self.results)} labs)"

lab_data = [
    {
        "id": "632975ef8910f8a366d44e2b",
        "code": "Invivo",
        "name": "INVIVO",
        "logo": "64928ebe792392ac8e4fec97",
        "smallLogo": "64928ebe792392ac8e4fec94",
        "description": "",
        "regionCode": None,
        "countryCode": "KZ",
        "isDeparture": True,
        "connectionParametr": None
    },
    {
        "id": "66545e0834178bb4a64a316f",
        "code": "3",
        "name": "Новая лаборатория в KZ test",
        "logo": "667ab7e3b241df7fcd99cd35",
        "smallLogo": "667ab7e3b241df7fcd99cd35",
        "description": "Лаборатория для сдачи анализов",
        "regionCode": "KZ_R_2",
        "countryCode": "KZ",
        "isDeparture": True,
        "connectionParametr": None
    },
    {
        "id": "667aba07f2245a010af14e61",
        "code": "Timson Lab",
        "name": "Timson Lab",
        "logo": "667aba07b241df7fcd99cd38",
        "smallLogo": "667aba07b241df7fcd99cd38",
        "description": "Timson Lab",
        "regionCode": "KZ_R_2",
        "countryCode": "KZ",
        "isDeparture": False,
        "connectionParametr": None
    }
]