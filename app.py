from flask import Flask
from credentials import *
import requests

app = Flask(__name__)

# access token
@app.route('/access_token')
def token():
    data = Token.validate_token
    
    return data
#lipa na mpesa online
@app.route('/LipaNaMpesaOnline')
def lipa_na_mpesa_online():
    mpesa_endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    access_token = Token.validate_token
    headers = {"Authorization":"Bearer %s" % access_token}
    request_body = {        
        "BusinessShortCode":Generate.Business_ShortCode,    
        "Password": Generate.decode_password,    
        "Timestamp":Generate.lipa_time,        
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":"1",    
        "PartyA":Generate.MSISDN,    
        "PartyB":Generate.Business_ShortCode,    
        "PhoneNumber":Generate.MSISDN, 
        "CallBackURL":"https://192.168.5.177",    
        "AccountReference":"Relax Ni Billy we fala",    
        "TransactionDesc":"BillyWeDidIt"
    }
    print(Generate.MSISDN)
    mpesa_online_response = requests.post(
        mpesa_endpoint,
        json = request_body,
        headers= headers
    )
    return mpesa_online_response.json()   


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3400,debug=True)
