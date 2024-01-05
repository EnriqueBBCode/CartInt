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
        data[c] = t.translate(v,dest=lang).text
    return HttpResponse(json.dumps(data),content_type='aplication/json')

class HomeView(View):
    def get(self,request,*args, **kwargs):
        header = Header.objects.get(pk=1)
        theme = Theme.objects.get(pk=1)
        carrousel = Carrousel.objects.get(pk=1)
        service = Service.objects.get(pk=1)
        about = AboutUs.objects.get(pk=1)
        context = {
            'header':header,
            'theme':theme,
            'carrousel':carrousel,
            'service':service,
            'about':about,
        }
        return render(request,'index.html',context)