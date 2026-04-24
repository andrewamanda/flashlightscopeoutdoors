from MPItemFeed import *

mpItemFeed = MPItemFeed()
mpItemFeedHeader = MPItemFeedHeader()
mpItemFeed.MPItemFeedHeader = mpItemFeedHeader
mpItemFeed.MPItemFeedHeader.version = "2.1"
mpItemFeed.MPItemFeedHeader.requestId = "jhdjhfdf"

mpItem = MPItem()

pyxb.RequireValidWhenGenerating(False)

mpItem.sku = "mysku"

product = MPProduct()
product.ProductName = "Nitecore MT23"
product.longDescription = "Nitecore MT23 long description"
product.shelfDescription = "Nitecore MT23 shelf description"
product.shortDescription = "Nitecore MT23 short description"
product.mainImage = pyxb.BIND()
product.mainImage.mainImageUrl = "http://someurl"

product.additionalAssets = AdditionalAssets()
product.additionalAssets.append(pyxb.BIND())
asset = product.additionalAssets.additionalAsset[-1]
asset.altText = "image1"
asset.assetUrl = "********************************"
itm2 = type(asset)(altText='image 2', assetUrl='++++++++++++++++++++++++++')
product.additionalAssets.additionalAsset.append(itm2)

product.productIdentifiers = ProductIdentifiers()
product.productIdentifiers.append(pyxb.BIND())

# Now pull it off the array and do stuff to it
itm = product.productIdentifiers.productIdentifier[-1]
itm.productIdType = 'EAN'
itm.productId = "11112323"
#the above can be refered to https://sourceforge.net/p/pyxb/discussion/956708/thread/c3da791a/

product.productTaxCode = "2038710"

product.SportAndRecreation = SportAndRecreation()
product.SportAndRecreation.brand = "Wangming Ye Brand"
product.SportAndRecreation.condition = "Brand New"
product.SportAndRecreation.manufacturer = "Wangming Ye"
product.SportAndRecreation.modelNumber = "NL888"

 

mpItem.sku = "mysku"
mpItem.Product = product
print(mpItem.Product.toxml("utf-8"))

mpItem.price = pyxb.BIND()
mpItem.price.currency = "USD"
mpItem.price.amount = "3323"


mpItem.shippingWeight = WeightMeasure()
mpItem.shippingWeight.value_ = "23234"
mpItem.shippingWeight.unit = "LB"




mpItemFeed.MPItem.append(mpItem)
print(mpItemFeed.toxml("utf-8"))
