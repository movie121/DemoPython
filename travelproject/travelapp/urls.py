from xml.etree.ElementInclude import include

from.import views
from django.urls import path

from travelproject import settings
from django.conf.urls.static import static
urlpatterns = [

   # path('about/',views.about,name='about'),
 #   path('add/',views.addresult1,name='addresult1'),
    path('',views.addition,name='addition'),
    path('',views.demo,name='demo'),
    # path('',include('travelapp.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
