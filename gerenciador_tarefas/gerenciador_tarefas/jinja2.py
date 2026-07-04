from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

#test para tentar fazer o jinja2 funcionar junto

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    return env