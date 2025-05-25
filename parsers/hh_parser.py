import requests
import config

def get_hh_vacancies():
    params = {
        "text": "для инвалидов OR ОВЗ",
        "accept_incomplete_resumes": "true",
        "per_page": 50
    }
    response = requests.get(config.HH_API_URL, params=params).json()
    return response["items"]
