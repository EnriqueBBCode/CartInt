from django.shortcuts import render,redirect
from django.views import View
from .models import *
from googletrans import Translator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from Contacts.models import *
import json, requests
from django.core.mail import EmailMessage
from django import forms
from django_recaptcha.fields import ReCaptchaField
from core import settings

@csrf_exempt
def translate(request,lang):
    t = Translator()
    data = {}
    for c,v in request.POST.items():
        print(f"{c} - {v}")
        try:
            data[c] = t.translate(v,dest=lang).text
        except:
            data[c] = v
            print(v)
            print(type(v))
    return HttpResponse(json.dumps(data),content_type='aplication/json')

@csrf_exempt
def suscribe(request):
    email = request.POST.get('email')
    print(email)
    Contact.objects.create(email=email)
    return HttpResponse(json.dumps(email),content_type='aplication/json')

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

def check_captcha(captcha_response):
    external_api_url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': captcha_response,
    }
    res = requests.post(external_api_url, data)
    if res.json()['success']:
        return True
    else:
        return False

def contact(request):
    print(request.method)
    if request.method == "POST":
        if check_captcha(request.POST['g-recaptcha-response']):
            message = request.POST['msg']
            tel = request.POST['phone']
            name = request.POST['name']
            email = request.POST['email']
            Contacting.objects.create(
                name = name,
                email = email,
                phone = tel,
                msg = message
            )
            msg = f"""Name / Nombre\n{name}\nPhone / Teléfono\n{tel}\nEmail\n{email}\n\n{message}"""
            emails = []
            for m in Manager.objects.all():
                emails.append(m.email)
            email = EmailMessage(
                f'New Contact / Nuevo Contacto',
                msg,
                "sendertest@godjango.dev",
                emails
            )
            email.send()
            print('mail sent')
    return redirect('home')

def track(request):
    if request.method == 'POST':
        track = request.POST['track']
        Shiping.objects.create(text=track)
        
    return redirect('home')

class HomeView(View):
    def get(self,request,*args, **kwargs):
        form = FormWithCaptcha()
        header = Header.objects.get(pk=1)
        theme = Theme.objects.get(pk=1)
        carrousel = Carrousel.objects.get(pk=1)
        service = Service.objects.get(pk=1)
        about = AboutUs.objects.get(pk=1)
        track = Track.objects.get(pk=1)
        review = ReviewSection.objects.get(pk=1)
        contact = ContactUs.objects.get(pk=1)
        suscribe = Suscribe.objects.get(pk=1)
        footer = Footer.objects.get(pk=1)
        context = {
            'header':header,
            'theme':theme,
            'carrousel':carrousel,
            'service':service,
            'about':about,
            'track':track,
            'review':review,
            'contact':contact,
            'subscribe':suscribe,
            'footer':footer,
            'form':form,
        }
        return render(request,'index.html',context)
