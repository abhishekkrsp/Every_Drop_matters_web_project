from django.http import HttpResponse
from django.shortcuts import render,redirect
from bloodbank.models import Contact,Bloodbank
from django.contrib.auth.models import User

# from django,contrib import messages

context={'home':'http://127.0.0.1:8000/',
    'stock':'http://127.0.0.1:8000/stock/',
    'collect':'http://127.0.0.1:8000/collect/',
    'give':'http://127.0.0.1:8000/give/'}

def index(request):
    if request.method == "POST":
        firstName= request.POST.get("firstName")
        lastName= request.POST.get("lastName")
        email= request.POST.get("email")
        address= request.POST.get("address")
        city= request.POST.get("city")
        state= request.POST.get("state")
        pincode= request.POST.get("pincode")
        phoneNumber= request.POST.get("phoneNumber")
        contact=Contact(firstName=firstName,lastName=lastName , email=email
        ,address=address , city=city , state=state , pincode=pincode ,
        phoneNumber=phoneNumber)
        if contact.is_valid():
            contact.save()
        return redirect('/')
    return render(request,'index.html',context)

def stock(request):
    new_context=context
    ap=Bloodbank.objects.get(category="a+").amount
    bp=Bloodbank.objects.get(category="b+").amount
    abp=Bloodbank.objects.get(category="ab+").amount
    op=Bloodbank.objects.get(category="o+").amount
    am=Bloodbank.objects.get(category="a-").amount
    bm=Bloodbank.objects.get(category="b-").amount
    abm=Bloodbank.objects.get(category="ab-").amount
    om=Bloodbank.objects.get(category="o-").amount
    new_context["ap"]=ap
    new_context["bp"]=bp
    new_context["abp"]=abp
    new_context["op"]=op
    new_context["am"]=am
    new_context["bm"]=bm
    new_context["abm"]=abm
    new_context["om"]=om
    return render(request,'stock.html',context)

def collect(request):
    if request.method == "POST":
        category=request.POST.get("category")
        amount=request.POST.get("amount")
        print(category)
        try:
            curr=Bloodbank.objects.get(category=category)
            curr.amount+=int(amount)
            curr.save()
        except:
            print("DO NOT EXIST")
        return redirect('collect')
    return render(request,'collect.html',context)

def give(request):
    if request.method == "POST":
        category=request.POST.get("category")
        amount=request.POST.get("amount")
        print(category)
        try:
            curr=Bloodbank.objects.get(category=category)
            curr.amount-=int(amount)
            if curr.amount>=0:
                curr.save()
        except:
            print("DO NOT EXIST")
        return redirect('give')
    return render(request,'give.html',context)

