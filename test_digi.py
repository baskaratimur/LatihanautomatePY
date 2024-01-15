import requests
import pytest
import json
import jsonpath

class TestBannerUpdate:
    @pytest.fixture
    def token(self):
        url = ""
        data = {
           ""
        }
        headersAuth = {"Accept-Language": "id"}
        response = requests.post(url, json=data, headers=headersAuth)
        code = response.status_code
        getJson = json.loads(response.text)
        dataJson = jsonpath.jsonpath(getJson, "data.access_token")
        yield dataJson

    def test_updateBanner(self, token):
        url = ""
        data = {
            "title": "Arab Maklum Automate",
            "title_en": "Arab Maklum Automate",
            "image_url": "images/series/aeb12d16/6698_r83.jpg",
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
            "Authorization": "Bearer " + token[0],
            "Accept-Language": "id"
        }
        response = requests.put(url, json=data, headers=headersAuth)
        code = response.status_code
        assert code == 200
        getJson = json.loads(response.text)
        dataTitle = jsonpath.jsonpath(getJson, "data.image_popup")
        assert dataTitle[0] == "automate"
