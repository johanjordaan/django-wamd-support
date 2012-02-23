from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template import Template
from django.template import Context

def send_mail(to_email_list,from_email,subject_str,template_str,template_context,attachements = []):
  context = Context(template_context)  

  body_template = Template(template_str)
  html_body = "<html><body>"+body_template.render(context)+"</body></html>"
  text_body = body_template.render(context)

  subject_template = Template(subject_str)
  subject = subject_template.render(context)
    
  for to_email in to_email_list:
    msg = EmailMultiAlternatives(subject = subject, body = text_body, from_email=from_email,to=[to_email])
    msg.attach_alternative(html_body,"text/html")
    for attachment in attachements:
      msg.attach(attachment[0],attachment[1],attachment[2])
    msg.send()
