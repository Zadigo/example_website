# DJANGO WEBSITE TEMPLATE
Your looking to upstart a website quickly with Django using professional settings? This template project is for you. It includes, all SEO and analytics tags and dependencies used in professionnal setup.

# Dependencies

The template depends on the following librairies:

    - Celery
    - Celery Beat
    - Social Django
    - Psycopg2
    - Stripe
    - Django Extensions
    - Django Rest Framework
    - Boto 3
    - Pandas + Numpy
    - Flower
    - Django Storages
    - Python Memcache

And for production:

    - Gunicorn
    - Redis

Additional librairies include:

    - Zappa

This template uses MD Bootrap's [Ecommerce template](https://mdbootstrap.com/freebies/jquery/e-commerce/) and [Dashboard](https://mdbootstrap.com/freebies/jquery/admin-dashboard/) it's main design interface. If you want to implement new items from these original templates, feel free to visit the former links.

By extension, the design CSS framework used for this website is [Bootstrap](https://getbootstrap.com/).

Finally, this was created with the lastest version of Django (3.0.x) and Python (3.8.x) and has never been tested with previous versions. There is therefore no guaranty that you application will work as intended if you decide to use versions prior to these ones.

## Front end

The whole website's frontend is based around using [Vue JS](https://vuejs.org/). Vue is by the definition the best thing to have ever happened to frontend web development because it simplifies to no extent the implementation of reactivity on you modern web pages.

Vue JS works very very well with Django's templates in the sense that they [the Django template syntax and Vue Js' template syntax] can be binded with one another without any problem.

Vue JS is very easy to pick up and if you wish improve the scripts on the various pages, have no experience with Vue, please visit the link above.

# Organization

The template uses three main applications: `shop`, `accounts` and `dashboard`.

## Templates folder

Each template folder is organized in this specific manner:

* Pages - They represent the main HTML page for the customer
* Components - Represent sub-elements from the main page for reusability (e.g. header, tables...)
* Vue - These are specific Vue JS scripts/components for reactivity
* Scripts - Very specific scripts binded with the Django template (e.g. Stripe payment, Quill...)

__NOTE:__ Under components there are folders named after the page to which they apply. Global components are stored under some sort of global folder.

# Support / Development

I will be updating and pushing new features on the different templates on a regular basis. Do not hesitate to watch and star :heart:

If you are interested in me participating in some other projects for you relate to the current work that I have done I am currently available for remote and on-site consulting for small, large and enterprise teams. Please contact me at pendenquejohn@gmail.com with your needs and let's work together!
