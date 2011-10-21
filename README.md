Django-contact
==============

Provides a simple to reuse contact form for users to send mails to settings.CONTACT_EMAILS which should be an array of emails.

There is an anti spamming mechanism included that prevent users from sending too many messages


Installation
------------

Add contact to your `INSTALLED_APPS`

    INSTALLED_APPS = (
        ...
        'contact',
        ...
    )

Set `CONTACT_EMAILS` to the emails you want to be notified

    CONTACTS_EMAILS = ['contact@mydomain.com', 'myemail@mydomain.com', ]

Add contact to your urls

    ...
    url('^contacts/', include('contact.urls')),
    ...
    
Override the contact/contact.html template if necessary

Set `CONTACTS_ANTI_SPAM_DELAY` to the value you want, default is 10 (its the duration within which another attempt will lead to an exception)