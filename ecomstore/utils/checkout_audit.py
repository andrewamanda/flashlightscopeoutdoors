from ecomstore.checkout.models import checkout_audit
from ecomstore.cart import cart
from ecomstore.utils.getip import get_user_ip

def _audit(request, stage, message, status='Success'):
        audit = checkout_audit()
        audit.stage = stage
        audit.ipaddress = "{}:{}".format(request.flavour,request.META.get('HTTP_X_FORWARDED_FOR'))
        #audit.address = get_user_ip(request)
        audit.email = request.session.get('email','')
        audit.cart_id = cart._cart_id(request)
        audit.message = message
        audit.status = status
        audit.save()
