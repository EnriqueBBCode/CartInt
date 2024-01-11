from django.shortcuts import render
from django.views import View
from .models import *
from googletrans import Translator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

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

class HomeView(View):
    def get(self,request,*args, **kwargs):
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
        }
        return render(request,'index.html',context)