from django.shortcuts import get_object_or_404

def Auction_Paid(request):

    b_id = request.session['b_id']
    from ecomstore.nameyourprice.models import NameYourPrice
    bid = get_object_or_404(NameYourPrice, id=b_id)
    bid.status = "PAID"
    bid.save()
    from ecomstore.nameyourprice.views import Cleanup_auction_session
    Cleanup_auction_session(request)


def is_auction(request):
    if 'win_price' in request.session:
        return True
    return False

def get_auction_price(request):
    return request.session.get('win_price')

