import requests
from subprocess import *

# Subroutine to invoke a java util
def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret

# Subroutine to call walmart APIs
def callwalmart(method, url, data):
    import os
    import random

    WM_CONSUMERID = "04aaea70-b106-4b25-9f8f-d9f693767084"
    WM_SECRETKEY = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAMuZPngTnBW//3c8pS95hz6ZoGtLUMvS4FbPiWQXkbTT3RbtuR7yGFaqkPRePEsXS3+8zYAtrcUB15ZPvWldsKXoX7SUWNyxdOaz1Xg+nzKgz/oSmEqkmStG/OjLRRwqZqqP53ojrz0Lk0y44DXzirPgE8ilN/1mi58qwY61eIb7AgMBAAECgYBG4wovAJTdtcWanFDfIK8ICrEh6k0tSjS1xPiPEu22SfW2X/qOXbg/pI9npc/UTT4KMZBTSpQv/Z40RXsrTmWMHm8l30tdjhkEK77xgliBZDA4XbTnmf6WJwoSGZb/s70NsnWag00cXrL4QcS2HdpM55T4MGWApxsmT6Ou528hIQJBAP1YnApg5t8XZbR1SNB4b2wspsNXsY3+gErkQhVaI84ano7oIVEFBTE/3Ka314nHmM5U7Rs7MZVGk/N+LJcSNCMCQQDNuzpkwHXiRIbj68h347guOZbfXC6+FRzdLHOZhVq+qJyaQn6IIPGOLWTX60ruJOgF8cAgWdBpFx5vzuB6u8NJAkAgvhD8rmVoM8frOLU+bDJKUsMCwBSse1XtV+7Kf6nc+0e+xHV52SJAqTZFPcFXhzpSgFtch5vy5Po+H/J3W9ztAkEAymtnHu6GjmRiXCsHiX6TH1gmbAolK31Wcv9jli+xg1ofC2BVYtcXFI7xY8jsZrgFWqPsJ2h3OI84sUXZdKj9kQJAfvTTWqtCdtjofbvWhd4hug1iqNI05YCz/Hu7psuKstI6xzO6iieQCiZrUzl2C/Y6zDbiXp3eQjfLixa3i6vp9Q=="

    jar_dir = os.getcwd()

    print "Current working dir = {}".format(jar_dir)

    if method == "GET":
        args = [jar_dir + '/DigitalSignatureUtil-1.0.0.jar', 'DigitalSignatureUtil', url, WM_CONSUMERID, WM_SECRETKEY, 'GET', 'wm_signature_response.txt']
    if method == "POST":
        args = [jar_dir + '/DigitalSignatureUtil-1.0.0.jar', 'DigitalSignatureUtil', url, WM_CONSUMERID, WM_SECRETKEY, 'POST', 'wm_signature_response.txt']

    status = jarWrapper(*args)
    print "Digital signature/timestamp = {}/{}".format(status[0],status[1])


    headers = {"Accept": "application/xml"}
    headers['WM_CONSUMER.ID'] = WM_CONSUMERID
    headers['WM_SVC.NAME'] = 'Walmart Marketplace'
    s = status[0].split(":")
    headers[s[0]] = s[1]
    s = status[1].split(":")
    headers[s[0]] = s[1]

    # generate a random WM_QOS_COORELATION_ID
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    len =15
    corID = ''
    for y in range(len):
        corID += characters[random.randint(0, len)]
    headers['WM_QOS.CORRELATION_ID'] = corID
    headers['Content-Type'] = 'multipart/form-data;'

    print "HTTP headers = {}".format(headers)

    if method == "GET":
        api_status = requests.get(url, headers=headers, data=data)
    if method == "POST":
	files = {'file': open('Test.xml')}
        #api_status = requests.post(url, headers=headers, files=files)
	return "did not call"


    return api_status.text


# test a POST API all
url = "https://marketplace.walmartapis.com/v2/feeds?feedType=item"
action = "POST"

with open("Test.xml") as myfile:
    testxml="".join(line.rstrip() for line in myfile)
print "testxml = {}".format(testxml)

status = callwalmart(action, url, testxml)

print "API call status = {}".format(status)
