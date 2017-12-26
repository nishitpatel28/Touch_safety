import requests

#print(response.text)
url ="http://api.thingspeak.com/apps/thinghttp/send_request" 
querystring = {"api_key":"CWWBBZTP63GUHOTI"}
payload ="from=%22NEXMO%22&number=918160515383&message==%22Hello%22" 
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "b21c8ccf-6c82-d2e6-e9ba-6e2e497ac37d"
    }
response = requests.request("POST", url, data=payload, headers=headers, 
params=querystring)
print(response.text)
