# Company Application

Allows you to bind specific details from your company to the templates.

## Settings

Add `ENTERPRISE` parameter to your settings file and in context processors, add `company.context_processors.company`.

You can use these in the template as `{{ contact.address.main }}`.

## Company description

The company lead.

### Address

Company address.

## Contact

Contact information related to the company.

### Emails

Company emails.

It takes two main parameters such as `main` and `customer_support`.

### Link to app store

Display the link to your application on the app store.

### Link to play store

Display the link to your application on the play store.

### Socials

'socials': [
{'alt': 'Facebook', 'url': 'https://www.facebook.com/mdbootstrap'},
{'alt': 'Github', 'url': 'https://github.com/Zadigo'}
],

### Telephone

Company telephones.

It accepts parameters such as `main` and `customer_support`.

### Zip code

Company zip code.
