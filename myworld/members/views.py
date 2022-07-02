from audioop import reverse
from multiprocessing import context
from re import template
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse



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

def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))   
    
def addrecord(request):
    x_name=request.POST['name']
    x_last=request.POST['last']
    member=Members(firstname=x_name, lastname=x_last)
    member.save()
    #return HttpResponseRedirect('/members')
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    member=Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    member=Members.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'mymember':member,
    }
    return HttpResponse(template.render(context,request))
def updaterecord(request,id):
    first=request.POST['first']
    last=request.POST['last']
    member=Members.objects.get(id=id)
    member.firstname=first
    member.lastname=last
    member.save()
    return HttpResponseRedirect(reverse('index'))

