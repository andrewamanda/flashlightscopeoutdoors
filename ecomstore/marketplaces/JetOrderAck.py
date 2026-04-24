#!/usr/local/bin/python2.7

import json
import smtplib
import requests

def sendemail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("andrew.ann2016@gmail.com", "Go123amanda")

    print "Sending msg=", msg
    server.sendmail("andrew.ann2016@gmail.com", "sales@andrew-amanda.com", msg)
    server.quit()

JET_API_USER = "5F4E8D2AE882C89A69B9B7EEB8C40104A5894FD7"
JET_SECRET = "C6SBhe1Mou0mdApwIiXrT29UYzqeizILQ+B6+vGaAtEY"
JET_MERCHANT_ID = "82fdc6460d0445999092c05b4d1a4175"

JET_TOKEN_REQUEST = {"user": JET_API_USER, "pass": JET_SECRET}

headers = {"Accept": "application/json"}
testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
reqJson = json.loads(testJet.text)
authHeader = "bearer " + reqJson['id_token']
print "authHeader = " + authHeader

headers = {"Content-Type":"application/json", "Authorization":authHeader}

retStatus = ""
base_order_url = "https://merchant-api.jet.com/api/orders/"
status_list = ['created','ready','acknowledged','inprogress','complete']
for status in status_list:
    url = base_order_url + status
    jetResponse = requests.get(url, headers=headers)
    orders = json.loads(jetResponse.text)
    for o in orders['order_urls']:
        msg = "Status: {}, order imported: {}".format(status, o)
        #sendemail(msg)
	print msg

        # populate order Details
        order_details_url = "https://merchant-api.jet.com/api/" + o
        jetResponse = requests.get(order_details_url, headers=headers)
        orderDetails = json.loads(jetResponse.text)

        #if status == 'ready':
        if status != 'complete':
          url = "https://merchant-api.jet.com/api/orders/" + orderDetails['merchant_order_id'] + "/acknowledge"

          ack_order_items = []

	  msg = ""
          order_items = orderDetails['order_items']
          for ci in order_items:
            ack_order_item = {}
            ack_order_item['order_item_id'] = ci.get('order_item_id', 'None')
            ack_order_item['order_item_acknowledgement_status'] = "fulfillable"
            ack_order_items.append(ack_order_item)
	    msg = msg + ci.get("product_title", "None") + " | "
	    msg = msg + str(ci.get("request_order_quantity", "None")) + " | " 
          ack_order = {}
          ack_order['acknowledgement_status'] = "accepted"
          ack_order['order_items'] = ack_order_items

          testJet = requests.put(url, headers=headers, data=json.dumps(ack_order))
          retStatus = "- ack status: " + str(testJet.status_code) + ":" + testJet.text

          #msg =  "Order: {} acked, status: {}".format(o, retStatus)
	  msg = msg + retStatus
          sendemail(msg)
