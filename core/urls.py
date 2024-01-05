from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name='home'),
    path('trans/<lang>/', translate,name='trans'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)