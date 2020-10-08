from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from predictor import views
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'predictor', views.predictorViewSet)
#router.register(r'auth', views.UserViewset)
# the code in the above line only grants the persmission to view 
# dataset to the person who is "LOGGED IN" i.e authorised.

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('', RedirectView.as_view(url="api/")),
    #url(r'^api-token-auth/', obtain_jwt_token),
    #path('predictor/', views.myClass.as_view()),
]













"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
""""#from django.contrib import admin
#from django.urls import path
#from django.urls.conf import include
#from django.views.generic.base import RedirectView

#from predictor.urls import urlpatterns as mau  
#(r'^predictor/', include(mau)),

#urlpatterns = [
    path('admin/', admin.site.urls),
    path('predictor/', include("predictor.urls")),
    path('', RedirectView.as_view(url="predictor/")),
    #path('predictor/', views.myClass.as_view()),
]"""

