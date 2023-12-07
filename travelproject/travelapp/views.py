from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import photo
# Create your views here.
def addition(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo(request):
    obj1=photo.objects.all()
    return render(request,"index.html",{'result1':obj1})
#def about(request):
  #  return render(request,"about.html")
#def contact(request):
   # return render(request,'contact.html')
#def addition(request):
  #  return render(request, "add.html")
#def addresult1(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # result=x+y
   # return render(request,"addresult.html",{'res':result})

