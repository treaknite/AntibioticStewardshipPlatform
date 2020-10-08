from django.urls import path
from .import views


from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('predictor', views.ApprovalsView)

 
urlpatterns = [

    path('', views.home, name='home'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),
    path('main',views.main, name='main'),
    path('form/', views.cxcontact, name='cxform'),
    path('form2', views.cxcontact2, name='cxform2'),
    path('uploadrecord',views.uploadrecord, name='uploadrecord'),
    path('uploadrecordsub',views.uploadrecordsub, name='uploadrecordsub'),
    path('prerecord',views.prerecord, name='prerecord'),
    path('prerecordsub',views.prerecordsub, name='prerecordsub'),
    path('search',views.search,name='search'),
    path('pastrecord',views.pastrecord, name='pastrecord'), 
    
]