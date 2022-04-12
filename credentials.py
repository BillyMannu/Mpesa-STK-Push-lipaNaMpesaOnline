import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
from dotenv import load_dotenv
import os

load_dotenv()
#mpesa details
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
base_URL ='http://192.168.5.41:801/'


#access token
class Token:
    # def ac_token():
    mpesa_auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    data = requests.get(mpesa_auth_url, auth = HTTPBasicAuth(consumer_key,consumer_secret)).json()
    validate_token = data['access_token']

#Generate request values for lipa na mpesa online
class Generate:
    # def password():
        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        Business_ShortCode = "174379"
        offsetValue = '0'
        passKey = os.getenv("passKey")
        data_to_encode = Business_ShortCode + passKey + lipa_time
        online_password = base64.b64encode(data_to_encode.encode())
        decode_password = online_password.decode('utf-8')
        MSISDN = os.getenv('phone_number')
        
