import ebaysdk
from ebaysdk.utils import getNodeText
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading
import os
import json

#ebay category id and item specifics can be found https://developer.ebay.com/tools/item-specifics

def verify_additem_to_aa_ebay(opts):
        print ("current dir = ", os.getcwd())
        retMsg = ""
        try:
            api = Trading(debug=opts['debug'], config_file=opts['yaml'], appid=opts['appid'],
                      certid=opts['certid'], devid=opts['devid'], warnings=False)

            myitem = {
                "Item": {
                    "Title": "Harry Potter and the Philosopher's Stone",
                    "Description": "This is the first book in the Harry Potter series. In excellent condition!",
                    "PrimaryCategory": {"CategoryID": "377"},
                    "StartPrice": "10.0",
                    "BuyItNowPrice": "15.0",
                    "CategoryMappingAllowed": "true",
                    "Country": "US",
                    "ConditionID": "3000",
                    "Currency": "USD",
                    "DispatchTimeMax": "3",
                    "ListingDuration": "Days_7",
                    "ListingType": "FixedPriceItem",
                    "PaymentMethods": "PayPal",
                    "PayPalEmailAddress": "sales@andrew-amanda.com",
                    "PictureDetails": {"PictureURL": "http://www.andrew-amanda.com/static/images/products/main/C21_1.png"},
                    "PostalCode": "95125",
                    "Quantity": "1",
                    "ReturnPolicy": {
                        "ReturnsAcceptedOption": "ReturnsAccepted",
                        "RefundOption": "MoneyBack",
                        "ReturnsWithinOption": "Days_30",
                        #"Description": "If you are not satisfied, return the book for refund.",
                        "ShippingCostPaidByOption": "Buyer"
                    },
                    "SellerProfiles": {
                        "SellerPaymentProfile": {
                            "PaymentProfileName": "PayPal:Immediate pay",
                        },
                        "SellerReturnProfile": {
                            "ReturnProfileName": "30 Day Return Policy",
                        },
                        "SellerShippingProfile": {
                            "ShippingProfileName": "USPS First Class, Priority, Priority Express Flat Rate Envelope",
                        }
                    },
                    "ShippingDetails": {
                        "ShippingType": "Calculated",
                        "ShippingServiceOptions": {
                            "ShippingServicePriority": "1",
                            "ShippingService": "USPSMedia"
                        },
                        "CalculatedShippingRate": {
                            "OriginatingPostalCode": "95125",
                            "PackagingHandlingCosts": "0.0",
                            "ShippingPackage": "PackageThickEnvelope",
                            "WeightMajor": "1",
                            "WeightMinor": "0"
                        }
                    },
                    "Site": "US"
                }
            }

            pData = {}
            item = {}
            item["AutoPay"] = "true"

            bestOfferDetails = {}
            bestOfferDetails["BestOfferEnabled"] = "true"
            item["BestOfferDetails"] = bestOfferDetails

            buyerRequirementDetails = {}
            buyerRequirementDetails["ShipToRegistrationCountry"] = "true"
            item["BuyerRequirementDetails"] = buyerRequirementDetails

            item["Title"] = "Harry Potter and the Philosopher's Stone"
            item["Description"] = "This is the first book in the Harry Potter series. In excellent condition!"

            cateID = {}
            cateID["CategoryID"] = "16037"  #this is the LED flashlight under outdoor/camping

            item["PrimaryCategory"] = cateID
            item["StartPrice"] = "10.0"
            #item["BuyItNowPrice"] = "15.0"
            item["CategoryMappingAllowed"] = "true"
            item["Country"] = "US"
            item["ConditionID"] = "1000"
            item["Currency"] = "USD"
            item["DispatchTimeMax"] = "1"
            item["HitCounter"] = "HiddenStyle"
            item["ListingDuration"] = "GTC"
            item["ListingType"] = "FixedPriceItem"
            item["PaymentMethods"] = "PayPal"
            item["PayPalEmailAddress"] = "james@roadtamerus.com"

            productListingDetails = {}
            brandMPN = {}
            brandMPN["Brand"] = "Nitecore"
            brandMPN["MPN"] = "HC60"
            productListingDetails["BrandMPN"] = brandMPN
            productListingDetails["EAN"] = "6952506062652"
            item["ProductListingDetails"] = productListingDetails


            pictureURL = {}
            pictureURL["PictureURL"] = "http://www.andrew-amanda.com/static/images/products/main/C21_1.png"

            item["PictureDetails"] = pictureURL
            item["PostalCode"] = "95125"
            item["Quantity"] = "1"

            retPolicy = {}
            retPolicy["ReturnsAcceptedOption"] = "ReturnsAccepted"
            retPolicy["RefundOption"] = "MoneyBack"
            retPolicy["ReturnsWithinOption"] = "Days_30"
            retPolicy["ShippingCostPaidByOption"] = "Buyer"
            item["ReturnPolicy"] = retPolicy

            sellerProfiles = {}
            sellerPaymentProfile = {}
            sellerPaymentProfile["PaymentProfileName"] = "PayPal:Immediate pay"
            sellerProfiles["SellerPaymentProfile"] = sellerPaymentProfile
            sellerReturnProfile = {}
            sellerReturnProfile["ReturnProfileName"] ="30 Day Return Policy"
            sellerProfiles["SellerReturnProfile"] = sellerReturnProfile
            sellerShippingProfile = {}
            sellerShippingProfile["ShippingProfileName"] = "USPS First Class, Priority, Priority Express Flat Rate Envelope"
            sellerProfiles["SellerShippingProfile"] = sellerShippingProfile

            item["SellerProfiles"] = sellerProfiles

            shippingDetails = {}
            shippingDetails["ShippingType"] = "Calculated"
            shippingServiceOptions = {}
            shippingServiceOptions["ShippingServicePriority"] = "1"
            shippingServiceOptions["ShippingService"] = "USPSMedia"
            shippingDetails["ShippingServiceOptions"] = shippingServiceOptions
            calculateShippingRate = {}
            calculateShippingRate["OriginatingPostalCode"] = "95125"
            calculateShippingRate["PackagingHandlingCosts"] = "0.0"
            calculateShippingRate["ShippingPackage"] = "PackageThickEnvelope"
            calculateShippingRate["WeightMajor"] = "1"
            calculateShippingRate["WeightMinor"] = "0"
            shippingDetails["CalculatedShippingRate"] = calculateShippingRate

            item["ShippingDetails"] = shippingDetails

            item["Site"] = "US"

            pData["Item"] = item

            print ("data=" + json.dumps(pData))

            price = api.execute('VerifyAddItem', pData)
            #price = api.execute('AddItem', myitem)
            print ("Response = ", price.json())
            pJson = price.json
            loaded_json = json.loads(price.json())
            fees = loaded_json["Fees"]

            try:
                print ("Ack = ", loaded_json["Ack"])
                retMsg += loaded_json["Ack"] + ":"
            except: pass
            try:
                print ("SeverityCode = ", loaded_json["Errors"]["SeverityCode"])
                retMsg += loaded_json["Errors"]["SeverityCode"]
            except Exception as e:
                print(e)
            try:
                print ("LongMessage = ", loaded_json["Errors"]["LongMessage"])
                retMsg += loaded_json["Errors"]["LongMessage"]
            except: pass
            for x in fees["Fee"]:
                #print x["Name"], x["Fee"]["value"]
                #for x in fees["Fee"]:
                    if x["Fee"]["value"] != "0.0":
                        print (x["Name"], x["Fee"]["value"])
                        retMsg += "," + x["Name"] + ": " + x["Fee"]["value"]


        except ConnectionError as e:
            print(e)
            print(e.response.dict())

        print (retMsg)
        return retMsg
