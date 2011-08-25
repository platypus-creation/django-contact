from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
  name = forms.CharField(label=_(u'Name'), required=True)
  email = forms.EmailField(label=_(u'Your email'), required=True)
  subject = forms.CharField(label=_(u'Subject'), required=True)
  message = forms.CharField(label=_(u'Message'), widget=forms.Textarea(), required=True)