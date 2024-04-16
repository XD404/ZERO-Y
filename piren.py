import requests,re
import time
from user_agent import generate_user_agent as ua
def solve_captcha():
 #full it
 #site_key : 6Ldx7ZkUAAAAAF3SZ05DRL2Kdh911tCa3qFP0-0r
 #page_url : https://www.pinterest.com/
def get_unix_time():
    return int(time.time())
USA = ua()
response = requests.get("https://www.pinterest.com/", headers={"User-Agent": USA, "Pragma": "no-cache", "Accept": "*/*"})
cookies = response.cookies.get_dict()
csrftoken = cookies.get("csrftoken")
solution = solve_captcha()
UNIX = get_unix_time()
url = "https://www.pinterest.com/resource/UserRegisterResource/create/"
data = {
    "source_url": "%2F",
    "data": {
        "options": {
            "type": "email",
            "birthday": 946684800,
            "email": "jjsbsvsbxx@yopmail.com",
            "password": "Haxkx0503@@",
            "country": "IQ",
            "first_name": "Tanji",
            "last_name": "",
            "recaptchaV3Token": solution,
            "visited_pages": "[{\"path\":\"/\",\"pageType\":\"home\",\"ts\":" + str(UNIX) + "}]",
            "user_behavior_data": "{}"
        },
        "context": {}
    }
}
headers = {
    "Accept": "application/json, text/javascript, */*, q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.pinterest.com",
    "Referer": "https://www.pinterest.com/",
    "DNT": "1",
    "Sec-GPC": "1",
    "X-Requested-With": "XMLHttpRequest",
    "X-APP-VERSION": "0c02a2d",
    "X-CSRFToken": csrftoken,
    "X-Pinterest-AppState": "background",
    "X-Pinterest-Source-Url": "/",
    "X-Pinterest-PWS-Handler": "www/index.js"
}

response = requests.post(url, data=data, headers=headers)
print(response.text)
if "\"status\":\"success\"" in response.text:
    print("Success")
elif "\"status\":\"failure\"" in response.text:
    print("Failure")