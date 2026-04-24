from django.shortcuts import render
from django.template import RequestContext

def file_not_found_404(request, exception):
    page_title = 'Page Not Found'
    return render(request, '404.html', locals())

def server_error_500(request):
    return render(request, '500.html', locals())

def app_offline(request):
    page_title = 'Application is offline'
    return render(request, 'app_offline.html', locals())
