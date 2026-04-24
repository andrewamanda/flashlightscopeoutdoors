from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from pprint import pformat
import sys, datetime, logging
import smtplib
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
import logging
from django.core.mail import EmailMessage
from ecomstore.checkout.models import Promotion
from ecomstore.catalog.models import Product, DealOfTheDay, Brand, RichTextField
#import re
#import dns.resolver

class EmailSubscription(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500)
    interestedProducts = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'email_subscription'
        ordering = ['email']


    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

class EmailSubscription_Excluded(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500)
    why = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'emailsubscription_excluded'
        ordering = ['email']


    def __str__(self):
        return u"%s" % (self.email)

    def __unicode__(self):
        return u"%s" % (self.email)


class ConfigNewsletter(models.Model):
    sender_name = models.CharField(blank=False, null=False, max_length=128, default="info@info.it")
    subject = models.CharField(blank=False, null=False, max_length=128, default="Newsletter da ...")
    sender_test_name = models.CharField(blank=False, null=False, max_length=128, default="test-info@info.it")
    subject_test = models.CharField(blank=False, null=False, max_length=128, default="Test Newsletter da ...")

    class Meta:
        verbose_name = 'Newsletter Configuration'
        verbose_name_plural = 'Newsletter Configuration'


class UnsubscribeText(models.Model):
    text = models.CharField(max_length=300, help_text="use html markup, put %s for first in the link for the name of the site and for second where you want to insert the mail of the unsubscribing user", default="<p align='center'>Per disiscriversi seguire questo <a href='%s/newsletter/disiscrivi/?val=%s'>link</a></p>")

    class Meta:
        verbose_name = 'Optional Text for unsubscribing Newsletter'
        verbose_name_plural = 'Optional Text for unsubscribing Newsletter'

class NewsLetterPage(models.Model):
    title = models.CharField(blank=False, max_length=128, unique=True)
    date = models.DateField(blank=False, default=datetime.date.today())
    body = models.TextField(blank=False)
    regenerate = models.BooleanField("Regenerate Content", default=False)
    send_unsubscribe_text = models.BooleanField("Enter link to unsubscribe", default=False)
    sent = models.BooleanField("Sent", default=False)
    sent_test = models.BooleanField("Forwarding Test", default=False)
    starts_with_letter = models.CharField(blank=False, max_length=5, default="0",
              help_text='Specify the starting email letter, e.g. 0:b, b:d, d:f, f:s, s:zzzz, Be aware that the search is not inclusive; but if you specify, say, czzzz in the end letter, it will become inclusive')
    ends_with_letter = models.CharField(blank=False, max_length=5, default="zzzz",
              help_text='Specify the ending email letter, e.g. 0:b, b:d, d:f, f:s, s:zzzz,Be aware that the search is not inclusive; but if you specify, say, czzzz in the end letter, it will become inclusive')

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __init__(self, *args, **kwargs):
        return super(NewsLetterPage, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.regenerate:
            products2include = self.productstoinclude_set.all()
            events = self.eventstoannounce_set.all()
            newclearance = self.newclearancetoannounce_set.all()
            deals = DealOfTheDay.future.all()
            brands = Brand.active.all().order_by('ranking')

            for p in products2include:
                if not p.full_description or len(p.full_description.strip()) == 0:
                      p.full_description = p.product.full_description
                      p.save()

            from ecomstore.misc.models import MediaImage
            media = MediaImage.objects.all()
            for m in media:
                 if 'groupbuy' in m.url_link:
                      groupbuy = m
                      print ('groupbuy = ', groupbuy.url_link)
                 if 'dealof' in m.url_link:
                      dealoftheday = m
            from django.template.loader import render_to_string
            template = 'newsletter/newsletter_template_1.htm'
            self.body = render_to_string(template, {'brands': brands, 'title': self.title, 'newclearance': newclearance, 'events': events, 'deals': deals, 'groupbuy': groupbuy, 'products': products2include})

        super(NewsLetterPage, self).save(*args, **kwargs)

        excludes = []
        for e in EmailSubscription_Excluded.objects.all():
            excludes.append(e.email)

        msg = self.body
        if self.send_unsubscribe_text:
            msg += "<br/>"
            testo = UnsubscribeText.objects.all()[0].text
            msg += str(testo)

        msg = '<html><head></head><body>' + msg + '</body></html>'

        import os
        dirspot = os.getcwd()
        file=dirspot + '/ecomstore/templates/newsletter/newsletter.html'
        with open(file, 'w') as filetowrite:
            filetowrite.write(msg)
            filetowrite.close()

        iscritti = []
        if self.sent:
            iscritti = NewsLetterUser.objects.all().filter(email__range=(self.starts_with_letter, self.ends_with_letter))
            sender_name = ConfigNewsletter.objects.all()[0].sender_name
            sub = ConfigNewsletter.objects.all()[0].subject
        if self.sent_test:
            iscritti = NewsLetterTestUser.objects.all().filter(email__range=(self.starts_with_letter, self.ends_with_letter))
            sender_name = ConfigNewsletter.objects.all()[0].sender_test_name
            sub = ConfigNewsletter.objects.all()[0].subject_test

        for user in iscritti:
            checkemailexcludes = user.email
            if checkemailexcludes.lower().strip() in [x.lower().strip() for x in excludes]:
                try:
                    logging.error("User %s is in the excluded list", str(user.email))
                    continue
                except Exception as e:
                    continue
            if user.email.find('mail.ru') != -1:
                try:
                    logging.error("User %s is in Russian email", str(user.email))
                    continue
                except Exception as e:
                    continue
            logging.error("Sending newsletter to %s", str(user.email))

            try:
                username = str(user.name)
            except Exception as e:
                logging.error("In Exc getting user name, error %s", e)
                username = None
            if username and user.name:
                name = user.name.split( )
                fName = name[0]
                subject = fName.upper() + " " + sub
            else:
                subject = sub
            fq_sender = sender_name + "<" + settings.DEFAULT_FROM_EMAIL + ">"
            EmailMsg = EmailMessage(subject,msg,fq_sender,[str(user.email)],headers={'Reply-To':settings.EMAIL_ORDER})
            EmailMsg.content_subtype = "html"


            try:
                # this call starts to create html tags in the content after django1.11
                #EmailMsg.send()

                from django.core.mail import EmailMultiAlternatives
                text_content = subject
                eMultiAlternative = EmailMultiAlternatives(subject, text_content, fq_sender, [str(user.email)])
                eMultiAlternative.attach_alternative(msg, "text/html")
                eMultiAlternative.send()

            except Exception as e:
                logging.error("In Exc sending mail to %s -- Error: %s", user, e)
        return
        """
    This is the original save code

	                ----EmailMsg.send()

    def save(self, *args, **kwargs):
        super(NewsLetterPage, self).save(*args, **kwargs)
        if self.sent:
            msg = self.body
            if self.send_unsubscribe_text:
                msg += "<br/>"
                testo = UnsubscribeText.objects.all()[0].text
                msg += str(testo)
            iscritti = NewsLetterUser.objects.all()
            msg = '<html><head></head><body>' + msg + '</body></html>'
            msg = MIMEText(msg, 'html')
            msg['From'] = ConfigNewsletter.objects.all()[0].sender_name
            msg['Subject'] = ConfigNewsletter.objects.all()[0].subject
            for user in iscritti:
                logging.error("MAIL a %s", str(user))
                msg['To'] = str(user)
                try:
                    s = smtplib.SMTP(settings.EMAIL_HOST)
                    s.ehlo()
                    s.starttls()
                    s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    if self.send_unsubscribe_text:
                        s.sendmail(ConfigNewsletter.objects.all()[0].sender_name, str(user), str(msg.as_string()) % (Site.objects.get_current(), user))
                    else:
                        s.sendmail(ConfigNewsletter.objects.all()[0].sender_name, str(user), msg.as_string())
                    s.quit()
                except Exception as e:
                    logging.error("In Exc sending mail to %s -- Error: %s", user, e)
        if self.sent_test:
            msg = str(self.body)
            if self.send_unsubscribe_text:
                msg += "<br/>"
                testo = UnsubscribeText.objects.all()[0].text
                msg += str(testo)
            msg = '<html><head></head><body>' + msg + '</body></html>'
            msg = MIMEText(msg, 'html')
            msg['From'] = ConfigNewsletter.objects.all()[0].sender_test_name
            msg['Subject'] = ConfigNewsletter.objects.all()[0].subject_test
            usertest = NewsLetterTestUser.objects.all()
            for us in usertest:
                logging.error("MAIL TEST a %s", str(us))
                msg['To'] = str(us)
                try:
                    s = smtplib.SMTP(settings.EMAIL_HOST)
                    s.ehlo()
                    s.starttls()
                    s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    if self.send_unsubscribe_text:
                        s.sendmail(ConfigNewsletter.objects.all()[0].sender_test_name, str(us), str(msg.as_string()) % (Site.objects.get_current(), us))
                    else:
                        s.sendmail(ConfigNewsletter.objects.all()[0].sender_test_name, str(us), msg.as_string())
                    s.quit()
                except Exception as e:
                    logging.error("In Exc sending mail to %s -- Error: %s", us, e)
        return
    """


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

"""
class NewsLetterUser(models.Model):
    mail = models.EmailField(_('e-mail'), blank=False, default="")

    class Meta:
        verbose_name = 'Newsletter User'
        verbose_name_plural = 'Newsletter User'


    def __str__(self):
        return self.mail

    def __unicode__(self):
        return self.mail

class NewsLetterTestUser(models.Model):
    test_mail = models.EmailField(_('e-mail for test'), blank=False, default="")

    class Meta:
        verbose_name = 'Newsletter Test User'
        verbose_name_plural = 'Newsletter Test User'


    def __str__(self):
        return self.test_mail
    def __unicode__(self):
        return self.test_mail
"""

class NewsLetterUser(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    email = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    imported_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'newsletteruser'
        ordering = ['email']



    def __str__(self):
        return u"%s" % (self.email)

    def __unicode__(self):
        return u"%s" % (self.email)

class NewsLetterTestUser(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    email = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    imported_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'newslettertestuser'
        ordering = ['email']



    def __str__(self):
        return u"%s" % (self.email)

    def __unicode__(self):
        return u"%s" % (self.email)



class ProductsToInclude(models.Model):
    newsletter = models.ForeignKey(NewsLetterPage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    full_description = RichTextField(null=True, blank=True)
    arrival_date = models.DateField()
    coupon = models.ForeignKey(Promotion, null=True, blank=True, on_delete=models.CASCADE)

class EventsToAnnounce(models.Model):
    newsletter = models.ForeignKey(NewsLetterPage, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255, unique=True)
    Description = models.TextField(null=True, blank=True)
    coupon = models.ForeignKey(Promotion, null=True, blank=True, on_delete=models.CASCADE)

class NewClearanceToAnnounce(models.Model):
    newsletter = models.ForeignKey(NewsLetterPage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

"""""
Below is the newsletter for the referenceusa research
"""""
DEPARTMENT_CHOICES = (
                  ('labscience' , 'Lab & Science'),
                  ('flashlights' , 'Flashlights & Outdoors'),
                  ('batterycharger' , 'Batteries & Chargers'),
                  ('Battery' , 'Battery'),
                 )
from ecomstore.referenceusa.models import *
class NewsLetter4ReferenceUSA(models.Model):
    title = models.CharField(blank=False, max_length=128, unique=True)
    date = models.DateField(blank=False, default=datetime.date.today())
    body = models.TextField(blank=False)
    ignore_sent = models.BooleanField("Send to everybody, ignoring the sent flag", default=False)
    send_unsubscribe_text = models.BooleanField("Enter link to unsubscribe", default=False)
    sent = models.BooleanField("Sent", default=False)
    sent_test = models.BooleanField("Forwarding Test", default=False)
    max_email_can_sent = models.IntegerField()
    target_industry = models.CharField(max_length=20, default='labscience', choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = 'Newsletter For ReferenceUSA Marketing'
        verbose_name_plural = 'Newsletter For ReferenceUSA Marketing'

    def __init__(self, *args, **kwargs):
        return super(NewsLetter4ReferenceUSA, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(NewsLetter4ReferenceUSA, self).save(*args, **kwargs)
        excludes = []
        for e in EmailSubscription_Excluded.objects.all():
            excludes.append(e.email)

        msg = self.body
        if self.send_unsubscribe_text:
            msg += "<br/>"
            testo = UnsubscribeText.objects.all()[0].text
            msg += str(testo)

        msg = '<html><head></head><body>' + msg + '</body></html>'
        if "lab" in self.target_industry:
            fq_sender = "Ecosphere Technologies<info@eco-sensa.com>"
            replyto = "info@eco-sensa.com"
            DS = ReferenceUSAData
        else:
            fq_sender = "Andrew & Amanda Outdoors<info@andrew-amanda.com>"
            replyto = "info@andrew-amanda.com"
            DS = ReferenceUSAData_4_Flashlights

        iscritti = []
        if self.sent:
            if self.ignore_sent:
                iscritti = DS.objects.all().filter(email_addresses__isnull = False, never_send_email = False)
            else:
                iscritti = DS.objects.all().filter(email_sent = False, email_addresses__isnull = False, never_send_email = False)

            sub = self.title

        max_email_can_sent = self.max_email_can_sent
        email_count = 0
        emails_already_sent = []
        for o in iscritti:
            if email_count > max_email_can_sent:
                break
            emails = o.email_addresses.split(',')
            emails = list(set(emails))
            for email in emails:
                if email in emails_already_sent:
                    print("{} already sent").format(email)
                    continue

                match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

                if match == None:
                    print('Bad Syntax in ' + email)
                    continue

                #Step 2: Getting MX record
                #Pull domain name from email address
                domain_name = email.split('@')[1]
                #get the MX record for the domain
                try:
                    records = dns.resolver.query(domain_name, 'MX')
                except Exception as e:
                    print(e.message)
                    continue

                if email.lower().strip() in [x.lower().strip() for x in excludes]:
                    logging.error("User %s is in the excluded list", str(email))
                    continue
                if "@" not in email:
                    logging.error("Email %s not valid", str(email))
                    continue
                logging.error("Sending newsletter to %s", str(email))

                try:
                    username = str(o.company_name)
                except Exception as e:
                    logging.error("In Exc getting user name, error %s", e)
                    username = None
                subject = sub
                EmailMsg = EmailMessage(subject,msg,fq_sender,[str(email)],headers={'Reply-To':replyto})
                EmailMsg.content_subtype = "html"
                try:
                    email_count = email_count + 1
                    EmailMsg.send()
                    o.email_sent = True
                    emails_already_sent.append(email)
                except Exception as e:
                    logging.error("In Exc sending mail to %s -- Error: %s", email, e)
            o.save()
        self.max_email_can_sent = email_count
        print ("email count = ", self.max_email_can_sent)

        super(NewsLetter4ReferenceUSA, self).save(*args, **kwargs)
        return


class NewsLetter4LexisNexis(models.Model):
    title = models.CharField(blank=False, max_length=128, unique=True)
    date = models.DateField(blank=False, default=datetime.date.today())
    body = models.TextField(blank=False)
    ignore_sent = models.BooleanField("Send to everybody, ignoring the sent flag", default=False)
    send_unsubscribe_text = models.BooleanField("Enter link to unsubscribe", default=False)
    sent = models.BooleanField("Sent", default=False)
    sent_test = models.BooleanField("Forwarding Test", default=False)
    max_email_can_sent = models.IntegerField()
    target_industry = models.CharField(max_length=20, default='labscience', choices=DEPARTMENT_CHOICES)

    class Meta:
        verbose_name = 'Newsletter For LexisNexis Marketing'
        verbose_name_plural = 'Newsletter For LexisNexis Marketing'

    def __init__(self, *args, **kwargs):
        return super(NewsLetter4LexisNexis, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(NewsLetter4LexisNexis, self).save(*args, **kwargs)
        excludes = []
        for e in EmailSubscription_Excluded.objects.all():
            excludes.append(e.email)

        msg = self.body
        if self.send_unsubscribe_text:
            msg += "<br/>"
            testo = UnsubscribeText.objects.all()[0].text
            msg += str(testo)

        msg = '<html><head></head><body>' + msg + '</body></html>'
        if "lab" in self.target_industry:
            fq_sender = "Ecosphere Technologies<info@eco-sensa.com>"
            replyto = "info@eco-sensa.com"
            DS = LexisNexisLabScience
        else:
            fq_sender = "Andrew & Amanda Outdoors<info@andrew-amanda.com>"
            replyto = "info@andrew-amanda.com"
            DS = LexisNexisFlashlights

        iscritti = []
        if self.sent:
            if self.ignore_sent:
                iscritti = DS.objects.all().filter(email_address__isnull = False, never_send_email = False)
            else:
                iscritti = DS.objects.all().filter(email_sent = False, email_address__isnull = False, never_send_email = False)

            sub = self.title

        max_email_can_sent = self.max_email_can_sent
        email_count = 0
        emails_already_sent = []
        for o in iscritti:
            if email_count > max_email_can_sent:
                print ("***** email_count = ", email_count)
                break
            emails = o.email_addresses.split(',')
            emails = list(set(emails))
            for email in emails:
                if email in emails_already_sent:
                    print("{} already sent").format(email)
                    continue

                match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

                if match == None:
                    print('Bad Syntax in ' + email)
                    continue

                #Step 2: Getting MX record
                #Pull domain name from email address
                domain_name = email.split('@')[1]
                #get the MX record for the domain
                try:
                    records = dns.resolver.query(domain_name, 'MX')
                except Exception as e:
                    print(e.message)
                    continue

                if email.lower().strip() in [x.lower().strip() for x in excludes]:
                    logging.error("User %s is in the excluded list", str(email))
                    continue
                if "@" not in email:
                    logging.error("Email %s not valid", str(email))
                    continue
                logging.error("Sending newsletter to %s", str(email))

                try:
                    username = str(o.company_name)
                except Exception as e:
                    logging.error("In Exc getting user name, error %s", e)
                    username = None
                subject = sub
                EmailMsg = EmailMessage(subject,msg,fq_sender,[str(email)],headers={'Reply-To':replyto})
                EmailMsg.content_subtype = "html"
                try:
                    email_count = email_count + 1
                    EmailMsg.send()
                    o.email_sent = True
                    emails_already_sent.append(email)
                except Exception as e:
                    logging.error("In Exc sending mail to %s -- Error: %s", email, e)
            o.save()
        self.max_email_can_sent = email_count
        print ("email count = ", self.max_email_can_sent)

        super(NewsLetter4LexisNexis, self).save(*args, **kwargs)
        return
