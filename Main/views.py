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
        data[c] = t.translate(v,dest='es').text
    return HttpResponse(json.dumps(data),content_type='aplication/json')

class HomeView(View):
    def get(self,request,*args, **kwargs):
        header = Header.objects.get(pk=1)
        context = {
            'header':header,
        }
        return render(request,'index.html',context)