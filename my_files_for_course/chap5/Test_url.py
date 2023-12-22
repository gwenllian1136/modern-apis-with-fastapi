import requests


url = 'https://api.openweathermap.org/data/2.5/weather?q=portland,OR,US&appid=98348bd915cb41bc4fdacdaec74dfd23&units=imperial'

response=requests.get(url, verify="Zscaler Root CA.crt") #verify=False

print(response.status_code)

#ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:992)

#cacert.pem