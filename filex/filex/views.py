from django.template import Context, loader
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world.")


def index(request):
    t = loader.get_template('tmpl/index.html')
    c = Context({ 'DATA': "TEST DE DATA", })
    return HttpResponse(t.render(c))
