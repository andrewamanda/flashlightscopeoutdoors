def get_user_ip(request):
        ipaddress = request.META.get('HTTP_X_FORWARDED_FOR')
        if not ipaddress:
           ipaddress = request.META.get('REMOTE_ADDR')
        if not ipaddress:
           ipaddress = '127.0.0.1'
        return ipaddress
