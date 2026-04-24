from ecomstore import settings
import requests
import base64
from ecomstore.utils.call_java import *
import os
import random

def getToken(url):
    import os
    import random

    headers = {"Accept": "application/xml"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    headers['WM_SVC.VERSION'] = '1.0.0'
    headers['WM_SVC.NAME'] = 'Walmart Marketplace'

    clientHeader = settings.WM_CLIENTID + ":" + settings.WM_CLIENTSECRET
    encodedBytes = base64.b64encode(clientHeader.encode("utf-8"))
    #encodedStr = str(encodedBytes, "utf-8")
    authHeader = "Basic " + encodedBytes.decode("utf-8")
    headers['Authorization'] = authHeader
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    len =15
    corID = ''
    for y in range(len):
        corID += characters[random.randint(0, len)]
    headers['WM_QOS.CORRELATION_ID'] = corID

    data = "grant_type=client_credentials"



    walmart_status = requests.post(url, headers=headers, data=data)


    print ("Response = ", walmart_status.text)

    #retMsg = "Request Payload: " + data
    #retMsg += "Response: " + walmart_status.text

    from ecomstore.utils.strops import find_between
    retMsg = find_between(walmart_status.text, "<accessToken>", "</accessToken>")

    return retMsg

def callwalmart(method, token, url, data):


    headers = {"Accept": "application/xml"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    #headers = {"Content-Type": "multipart/form-data"}

    #headers['WM_SVC.VERSION'] = '1.0.0'
    headers['WM_SVC.NAME'] = 'Walmart Marketplace'

    clientHeader = settings.WM_CLIENTID + ":" + settings.WM_CLIENTSECRET
    encodedBytes = base64.b64encode(clientHeader.encode("utf-8"))
    #encodedStr = str(encodedBytes, "utf-8")
    authHeader = "Basic " + encodedBytes.decode("utf-8")
    headers['Authorization'] = authHeader

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    len =15
    corID = ''
    for y in range(len):
        corID += characters[random.randint(0, len)]
    headers['WM_QOS.CORRELATION_ID'] = corID
    headers['WM_SEC.ACCESS_TOKEN'] = token
    #headers['host'] = "https://marketplace.walmartapis.com"
    print ("****** headers = ", headers)


    if method == "GET":
        walmart_status = requests.get(url, headers=headers, data=data)
    if method == "POST":
        files = {'file': open(data)}
        #walmart_status = requests.post(url, headers=headers, files=files)
        walmart_status = requests.post(url, headers=headers, data=open(data,'rb').read())


    print ("Response = ", walmart_status.text)

    retMsg = "Request Payload: " + data
    retMsg += "Response: " + walmart_status.text

    return retMsg

def getfeedstatus(url, token, feedid):


    headers = {"Accept": "application/xml"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    headers['WM_SVC.VERSION'] = '1.0.0'
    headers['WM_SVC.NAME'] = 'Walmart Marketplace'

    clientHeader = settings.WM_CLIENTID + ":" + settings.WM_CLIENTSECRET
    encodedBytes = base64.b64encode(clientHeader.encode("utf-8"))
    #encodedStr = str(encodedBytes, "utf-8")
    authHeader = "Basic " + encodedBytes.decode("utf-8")
    headers['Authorization'] = authHeader

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    len =15
    corID = ''
    for y in range(len):
        corID += characters[random.randint(0, len)]
    headers['WM_QOS.CORRELATION_ID'] = corID
    headers['WM_SEC.ACCESS_TOKEN'] = token
    #headers['host'] = "https://marketplace.walmartapis.com"


    url = url + "feeds/" + feedid + "?includeDetails=true&limit=20&offset=0"
    walmart_status = requests.get(url, headers=headers)

    print ("Response = ", walmart_status.text)

    #retMsg = "Request Payload: " + data
    #retMsg += "Response: " + walmart_status.text

    return walmart_status.text
