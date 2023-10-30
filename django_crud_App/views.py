from django.shortcuts import render,redirect
from django_crud_App.models import candidate
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method =="POST":
        name = request.POST.get("name")
        country = request.POST.get("country")
        state = request.POST.get("state")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        data = candidate(name=name,country=country,state=state,email=email,phone=phone)
        data.save()
        return render (request,"home.html",{"data":data})
    return render(request,"home.html")


def read(request):
    data = candidate.objects.all()
    return render(request,"read.html",{"data":data})

def delete(request,id):
    data = candidate.objects.get(id=id)
    data.delete()
    return redirect("/read/")

def update(request,id):
    if request.method =="POST":
        name = request.POST.get("name")
        country = request.POST.get("country")
        state = request.POST.get("state")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        data = candidate(id=id,name=name,country=country,state=state,email=email,phone=phone)
        data.save()
        return redirect("/read")
    data = candidate.objects.get(id=id)
    return render(request,"update.html",{'data':data})

def search(request):
    if request.method=="POST":
        query = request.POST.get("query")
        data = candidate.objects.filter(Q(name__contains=query)|Q(country__contains=query)|Q(state__contains=query)|Q(email__contains=query)|Q(phone__contains=query))
        return render (request,"search.html",{'data':data})