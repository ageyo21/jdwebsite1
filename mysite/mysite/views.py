from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import ContactForm # type: ignore
from ContactEnquiry.models import contactEnquiry # type: ignore


def homePage(request):
    return render(request,"home.html")

def aboutus(request):
     return render(request,"aboutus.html")

def contact(request):
    return  render(request,"contact.html")

def terms(request):
    return  render(request,"condition.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For example, send an email or save the data to the database
            pass
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        referral=request.POST.get('referral')
        date=request.POST.get('date')
        occassion=request.POST.get('occassion')
        location=request.POST.get('location')
        currency=request.POST.get('currency')
        budget=request.POST.get('budget')
        comments=request.POST.get('comments')
        en=contactEnquiry(name=name,email=email,phone=phone,referral=referral,date= date,occassion=occassion,location=location,currency=currency,budget=budget,comments=comments)
        en.save(
            
        )
    return render(request,"contact.html")

def maternity(request):
    return  render(request,"maternity.html")

def films(request):
    return  render(request,"films.html")

def prewedding(request):
    return  render(request,"prewedding.html")

def wedding(request):
    return  render(request,"wedding.html")

"""def weddingfilms(request):
    return  render(request,"weddingfilms.html")"""

def a(request):
    return render(request,"page1.html")  

def b(request):
    return render(request,"page2.html")  

def c(request):
    return render(request,"page3.html")  

def d(request):
    return render(request,"page4.html")  

def e(request):
    return render(request,"page5.html")  

def f(request):
    return render(request,"page6.html")  

def g(request):
    return render(request,"page7.html")  

def h(request):
    return render(request,"page8.html")  

def i(request):
    return render(request,"page9.html")  

def j(request):
    return render(request,"page10.html")  

def k(request):
    return render(request,"page11.html")  

def l(request):
    return render(request,"page12.html")  

'''def submitform(request):
    try:
        if request.method == "POST":
        #  n1=int(request.GET['num1'])
        #  n2=int(request.GET['num2'])    
            
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            
            return HttpResponse(finalans)    
    except:
        pass 
     
def userform(request): 
    finalans=0
    fn=userForms()
    data={'form':fn}
    try:
        if request.method == "POST":
        #  n1=int(request.GET['num1'])
        #  n2=int(request.GET['num2'])    
            
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'form':fn,
                'output':finalans
            }
            url="/about-us/?output={}".format(finalans)
            
            return HttpResponseRedirect(url)
        
        
    except Exception as e:
        print(e)       
    return render(request, "userform.html",data)'''


 