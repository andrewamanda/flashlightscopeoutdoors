from django.template import RequestContext as Context
from ecomstore.newsletter.models import NewsLetterPage, NewsLetterUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import ecomstore.settings
import logging
#from django.core.validators import email_re

@csrf_protect
def newsletter(request, template_name="newsletter/newsletter.html"):
    return render(request, template_name, locals())

def is_valid_email(email):
    if email_re.match(email):
        return True
    return False
    
def iscrivi(request):
    mail = request.GET['val']
    if not is_valid_email(mail):
        var = "<p class='error'>inserire una email corretta</p>"
    else:
        try:
            newmail = NewsLetterUser.objects.get(mail=mail)
            var = "<p class='error'>indirizzo email %s gia' esistente nel database</p>" % mail
        except:
            newmail = NewsLetterUser()
            newmail.mail = mail
            newmail.save()
            var = "<p class='correct'>contatto %s inserito nel database</p>" % mail
    return render(request, 'newsletter.html', locals())


def disiscrivi(request):
    mail = request.GET['val']
    if not is_valid_email(mail):
        var = "<p class='error'>inserire una mail corretta</p>"
    else:
        try:
            oldmail = NewsLetterUser.objects.get(mail=mail)
            oldmail.delete()
            var = "<p class='correct'>email %s eliminata dal database</p>" % mail
        except:
            var = "<p class='error'>email inesistente nel Database, nulla da eliminare</p>"
    return render(request, 'newsletter.html', locals())

