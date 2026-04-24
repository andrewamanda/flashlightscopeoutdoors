from django.http import HttpResponsePermanentRedirect

old_urls = {"www.heartwoodandbeyond.com", "heartwoodandbeyond.com", "heartwoodpine.com", "www.heartwoodpine.com"}
new_url = 'https://www.tarheelreclaimed.com'

class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host in old_urls:

            return HttpResponsePermanentRedirect(new_url + request.path)
        return self.get_response(request)
