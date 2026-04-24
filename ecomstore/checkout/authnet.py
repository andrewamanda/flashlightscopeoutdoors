from ecomstore import settings
import http.client as httplib
import urllib

def do_auth_capture(amount='0.00', card_num=None, exp_date=None,card_cvv=None,
                    bfname=None,baddr=None,bcity=None,bstate=None,bzip=None,bphone=None,bcountry=None,
                    sfname=None,saddr=None,scity=None,sstate=None,szip=None,scountry=None):
    """ function that connects to the Authorize.Net with billing information. Returns a Python list 
    containing the response parameters of sent back by the payment gateway.
    The first item in the response list is the reponse code; the 7th item is the uniquely identifying 
    transaction ID
    
    """  
    delimiter = '|'
    raw_params = { 'x_login': settings.AUTHNET_LOGIN,
                   'x_tran_key': settings.AUTHNET_KEY,
                   'x_type': 'AUTH_CAPTURE',
                   'x_amount': amount,
                   'x_version': '3.1',
                   'x_card_num': card_num,
                   'x_exp_date': exp_date,
                   'x_delim_char': delimiter,
                   'x_relay_response': 'FALSE',
                   'x_delim_data': 'TRUE',
                   'x_card_code': card_cvv,
                   'x_first_name':bfname,
                   'x_address':baddr,
                   'x_city':bcity,
                   'x_state':bstate,
                   'x_zip':bzip,
                   'x_phone':bphone,
                   'x_country':bcountry,
                   'x_ship_to_first_name':sfname,
                   'x_ship_to_address':saddr,
                   'x_ship_to_city':scity,
                   'x_ship_to_state':sstate,
                   'x_ship_to_zip':szip,
                   'x_ship_to_country':scountry,
                  }
    params = urllib.parse.urlencode(raw_params)
    headers = { 'content-type':'application/x-www-form-urlencoded',
                'content-length':len(params) }
    post_url = settings.AUTHNET_POST_URL
    post_path = settings.AUTHNET_POST_PATH
    cn = httplib.HTTPSConnection(post_url, httplib.HTTPS_PORT)
    cn.request('POST', post_path, params, headers)
    return cn.getresponse().read().decode().split(delimiter)
    
