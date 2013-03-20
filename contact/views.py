from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from contact.forms import ContactForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.core.cache import cache
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

def contact(request):
    next = request.GET.get('next', '/')
    anti_spam_delay = 10
    if hasattr(settings, 'CONTACTS_ANTI_SPAM_DELAY'):
        anti_spam_delay = settings.CONTACTS_ANTI_SPAM_DELAY
    if request.method == "POST":
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            # send mail
            from smtplib import SMTPException
            from django.core.mail import send_mail, BadHeaderError

            key = '%s_cannot_send_email' % request.META.get('REMOTE_ADDR', 'unknown_host')
            cannot_send_email = cache.get(key)
            if cannot_send_email:
                cannot_send_email = cannot_send_email*2
                cache.set(key, cannot_send_email)
                messages.error(request, _('To prevent spamming you cannot send another message so soon, please wait another %s seconds.') % cannot_send_email)
            else:
                try:
                    send_mail(contactForm.cleaned_data.get('subject'), contactForm.cleaned_data.get('message'), contactForm.cleaned_data.get('email'), settings.CONTACT_EMAILS)
                    messages.success(request, _('Your message has been sent'))
                    cache.set(key, anti_spam_delay)
                    return HttpResponseRedirect(next)
                except BadHeaderError:
                    messages.error(request, _('Sorry, we were unable to send your message due to a technical difficulty. Please retry later.'))

    else:
        # prefillForm with GET params
        initial_values = request.GET.copy()
        if request.user.is_authenticated():
            initial_values.update({'name': request.user.get_full_name(), 'email': request.user.email})
        contactForm = ContactForm(initial=initial_values)
    return render_to_response('contact/contact.html', locals(), context_instance=RequestContext(request))
