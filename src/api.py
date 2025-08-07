import requests

headers = {
    "Authorization": "Basic ZGl0cmF2b3llYnNwOmRpdHJhMzQhdm8u",
    "Referer": "https://ebilet.tcddtasimacilik.gov.tr/sefer-listesi",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    ),
}


def post_request(url, body):
    return requests.post(url, json=body, headers=headers)
