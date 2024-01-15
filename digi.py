import json
import jsonpath
import requests

url = ""
data = {
        "title": "Arab Maklum Automate",
        "title_en": "Arab Maklum Automate",
        "image_url": "https://static.mncnow.id/images/series/aeb12d16/6698_r83.jpg",
        "next_url": "string1",
        "image_popup": "automate",
        "image_popup_web": "automate",
        "position": 0,
        "content": {
        "id": 59000,
            "tags": [
                "Drama",
                "Religi"
            ],
            "type": "Series",
            "synopsis": "Cerita tentang keluarga Arab yang tinggal di kota Jakarta, dimana sang Aba ingin mempertahankan tradisi Arab dalam keluarga dan pekerjaannya di era modernisasi. 1"
            },
        "content_en": {
        "id": 59000,
            "tags": [
                "Drama",
                "Religi"
            ],
            "type": "Series",
            "synopsis": "Arab Maklum is a story about an Arab Family living in Jakarta, where the Aba wants to maintain Arabic traditions in his family and work in the  modernization era 1"
        }
        }
    
headersAuth = {
    "Authorization" : "Bearer " + "",
    "Accept-Language" : "id"
            }
response = requests.put(url, json=data, headers=headersAuth)
code = response.status_code
print(response)
getJson = json.loads(response.text)
print(getJson)
dataJson = jsonpath.jsonpath(getJson, "data.title")
print(dataJson)
