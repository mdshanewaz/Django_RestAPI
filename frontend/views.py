from urllib import response
from django.shortcuts import render
from .forms import ContactForm
import requests, json

# Create your views here.

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        d = {"username":"Sawon", "password":"12345"}
        url0 = "http://127.0.0.1:8000/api/token/"
        api0 = requests.post(url=url0, json=d)
        try:
            resp0 = json.loads(api0.text)
        except:
            resp = None
        token = resp0['access']
        print (token) 

        data = form.data
        url = "http://127.0.0.1:8000/api/contact/"
        api = requests.post(url=url, data=data, headers={'Authorization':f'Bearer {token}'})
        try:
            resp = json.loads(api.text)
        except:
            resp = None
        
        print(resp)
    
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form':form})