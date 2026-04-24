from django.core.mail import EmailMultiAlternatives, EmailMessage
from ecomstore.settings import EMAIL_ORDER


#def send_pdf(subject, content, from, to, pdf, ordernum):
#  EmailMsg = EmailMessage(subject,content,from,[to, EMAIL_ORDER],headers={'Reply-To':from})
#  EmailMsg.attach(str(ordernum) + '.pdf',pdf,'application/pdf')
#  EmailMsg.send()


def send_email_nonuser(dst_email, src_email, subject, plain_text, html_text=""):
  #print "Email to: "+dst_email+", from: "+src_email

  msg = EmailMultiAlternatives(subject, plain_text, src_email, [dst_email])
  if html_text != "":
    msg.attach_alternative(html_text, "text/html")

  #try:
  msg.send()



def send_email(dst_email, src_email, subject, plain_text, html_text=""):

  #print "Email to: ", dst_email, ", from: ", src_email, ", subject: ", subject

  msg = EmailMultiAlternatives(subject, plain_text, src_email, [dst_email, EMAIL_ORDER])
  if html_text != "":
    msg.attach_alternative(html_text, "text/html")

  #try:
  msg.send()
  #except:
  #  message = "Due to a problem with our server, we cannot complete your registration at this time."
  #  data = hdr_info(request)
  #  data = { 'message': message }
  #  return render_to_response('message',data)

def send_mail_with_attachment(subject, body, from_email, replyto_email, recipient_list, files):
    #try:
        headers = {'Reply-To': replyto_email}
        mail = EmailMessage(subject, body, from_email, recipient_list, headers=headers)
        for f in files:
            mail.attach(f.name, f.read())
        mail.send()
        return "email sent"
    #except:
    #        return "email failed to send"

import threading
class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_mail_async(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()
