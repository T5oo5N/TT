import json
import requests
from faker import Faker
from termcolor import colored
import random
import sys
import string

sys.stdout.write('\x1b]2;Aetheris by : 佐賀県産 （𝒀𝑼𝑼𝑹𝑰）\x1b\\')
sys.stdout.flush()

print("""
╔══════════════════════════════════════════════╗
║   🌟 AETHERIS REG - Automated Registration   ║
║ Automate your Aetheris account creation!     ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝
""")

fake = Faker()
url = "https://aetheris.company/api/reg"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ja,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "cookie": "",
    "origin": "https://aetheris.company",
    "priority": "u=1, i",
    "referer": "https://aetheris.company/sign-in",
    "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

ref_code = input("Enter referral code: ")
num_requests = int(input("Enter number of requests: "))
data_list = []

for i in range(num_requests):
    email = f"{fake.user_name()}{random.randint(100, 999)}@gmail.com"
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    
    payload = {
        "email": email,
        "first": first_name,
        "last": last_name,
        "password": password,
        "password2": password,
        "ref": ref_code
    }
    
    headers["cookie"] = f"ref={ref_code}"
    
    print(colored(f"Preparing registration for {email}", "yellow"))
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            print(colored(f"Successfully registered {email}", "green"))
            data_list.append({"email": email, "name": f"{first_name} {last_name}", "password": password})
        else:
            print(colored(f"Failed to register {email}", "red"))
            
    except Exception as e:
        print(colored(f"Error registering {email}", "red"))
    
with open("data.json", "w") as f:
    json.dump(data_list, f, indent=4)
    
print(colored("Registration data saved to data.json", "green"))
