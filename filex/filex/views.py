from django.template import Context, loader
from django.http import HttpResponse

import datetime

def hello(request):
    return HttpResponse("Hello, world.")


def index(request):
    t = loader.get_template('tmpl/index.html')
    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")

    c = Context({ 
        'DATA': "TEST DE DATA", 
        'PUB_DATE':PUB_DATE, 
        'TITRE_PAGE' : 'WELCOME',
        })
    return HttpResponse(t.render(c))
