from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products, customers, fav, users
from django.contrib import messages
# Create your views here.
def home(request):
    return HttpResponse("<h1>hello welcome to my page</h1>")
def index(request):
    if 'cus_email' in request.session:
        current_user=request.session['cus_email']
        return render(request,"index.html",{'current':current_user})
    return render(request,"index.html")
def register(request):
    if request.method=='POST':
        cname=request.POST['name']
        cemail=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        cage=request.POST['age']
        caddress=request.POST['address']
        cimage=request.FILES.get('image')
        emailexists=customers.objects.filter(cus_email=cemail)
        if emailexists:
            messages.info(request,"email id already registered Please login")
        elif passw!=cpass:
            messages.info(request,"Password does not match")
        else:   
            customers.objects.create(cus_name=cname,cus_email=cemail,password=passw,cus_age=cage,cus_address=caddress,cus_image=cimage)
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        cemail=request.POST['email']
        passw=request.POST['password']
        user=customers.objects.filter(cus_email=cemail,password=passw)
        if user:
            request.session['cus_email']=cemail
            return redirect('index')
        else:
            messages.info(request,"failed")
    return render(request,"login.html")
def logout(request):
    del request.session['cus_email']
    return redirect('index')
def read(request):
    data=customers.objects.all()
    return render(request,"read.html",{'data1':data})
def view(request,id):
    data=customers.objects.get(id=id)
    return render(request,"view.html",{'data1':data})
def update(request,id):
    data=customers.objects.get(id=id)
    if request.method=='POST':
        cname=request.POST['name']
        cemail=request.POST['email']
        passw=request.POST['password']
        cage=request.POST['age']
        caddress=request.POST['address']
        data.cus_name=cname
        data.cus_email=cemail
        data.password=passw
        data.cus_age=cage
        data.cus_address=caddress
        data.save()
        return redirect('read')
    return render(request,"update.html",{'data1':data})
def delete(request,id):
    data=customers.objects.get(id=id)
    data.delete()
    return redirect('read')
def userregister(request):
    if request.method=='POST':
        cname=request.POST['name']
        cemail=request.POST['email']
        passw=request.POST['password']
        cage=request.POST['age']
        users.objects.create(name=cname,email=cemail,password=passw,age=cage)
        return redirect('userlogin')
    return render(request,"userregister.html")
def userlogin(request):
    if request.method=='POST':
        cemail=request.POST['email']
        passw=request.POST['password']
        user=users.objects.filter(email=cemail,password=passw)
        if user:
            request.session['email']=cemail
            return redirect('userhome')
        else:
            messages.info(request,"failed")
    return render(request,"userlogin.html")
def userhome(request):
    if 'email' in request.session:
        current_user=request.session['email']
        return render(request,"userhome.html",{'currentuser':current_user})
    return render(request,"userhome.html")
def addproduct(request):
    if request.method=='POST':
        name=request.POST['name']
        rate=request.POST['rate']
        des=request.POST['desc']
        im=request.FILES.get('image')
        Products.objects.create(p_name=name,p_rate=rate,p_desc=des,p_image=im)
        return redirect('userhome')
    return render(request,"addproducts.html")
def viewproduct(request):
    data=Products.objects.all()
    return render(request,"viewproducts.html",{'data1':data})
def userlogout(request):
    del request.session['email']
    return redirect('userhome')
def favourites(request,id):
    if 'email' in request.session:
        current_user=request.session['email']
        user=users.objects.get(email=current_user)
        data=Products.objects.get(id=id)
        fav.objects.create(username=user,prd_name=data)
        return redirect('userhome')
    return redirect('userhome')
def viewfav(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=users.objects.get(email=current_user)
        favit=fav.objects.filter(username=user)
        return render(request,"viewfav.html",{'fav':favit})



    