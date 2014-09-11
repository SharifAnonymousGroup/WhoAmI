import threading

from django.core.mail.message import EmailMultiAlternatives
from django.template.context import Context
from django.template.loader import get_template


class EmailThread(threading.Thread):
    def __init__(self, subject, from_email, recipient_list,
                 plaintext_template, html_template, context, fail_silently):
        self.subject = subject
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html_template = html_template
        self.plaintext_template = plaintext_template
        self.context = context
        threading.Thread.__init__(self)

    def run(self):
        # print self.plaintext_template
        #print self.html_template
        plaintext = get_template(self.plaintext_template)
        html = get_template(self.html_template)
        d = Context(self.context)
        subject, from_email, to = self.subject, self.from_email, self.recipient_list
        text_content = plaintext.render(d)
        html_content = html.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        if self.html_template:
            msg.attach_alternative(html_content, "text/html")
        msg.send()


def send_mail(subject, from_email, recipient_list, plaintext_template,
              html_template=None, context=None, fail_silently=False, *args, **kwargs):
    EmailThread(subject, from_email, recipient_list,
                plaintext_template, html_template, context, fail_silently).start()