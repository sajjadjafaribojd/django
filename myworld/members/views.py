from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from .models import Members


def index(request):
    mymembers=Members.objects.all().values()
    template= loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def index_2(requst):
   membres=Members.objects.all().values()
   output=""
   for x in membres:
       output +=x["firstname"]+"<br/>"
   return HttpResponse(output)    
    
    

