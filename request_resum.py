import requests

# To run the docker image, which automatically starts the model serving API, run:
# $ docker run -it -p 5000:5000 max-text-summarizer


monText = "The time has come for consumer electronics products that are designed to last: products that give you back the power to upgrade, customize, and repair them. We’re excited for the opportunity to fix the consumer electronics industry together."

def resume(monText):

    # Pour interagir avec la page html  
    url = "http://localhost:5000/model/predict"

    headers= {"Content-Type": "application/json; charset=utf-8", "accept":"application/json"}
    data  = { "text": [monText]}

    r = requests.post(url, json=data)

    return r.text

print(resume(monText))