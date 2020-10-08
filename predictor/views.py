from django.http.response import HttpResponse
from django.shortcuts import render
from predictor.models import predictor
import json
from rest_framework import viewsets
#from predictor.models import antibiotics_details
#####from predictor import nnc
from rest_framework.response import Response
#from predictor.myserializer import antibiotics_detailsSerializer #, UserSerializer
#from django.contrib.auth.models import user
from predictor.myserializer import predictorSerializer
#from django.views.generic import View
from rest_framework import viewsets
from predictor.models import predictor
from rest_framework.response import Response
from predictor import ABML
from django.http.response import HttpResponse
from home.models import prerecord

class predictorViewSet(viewsets.ModelViewSet):
    queryset = prerecord.objects.order_by('-id')
    serializer_class = predictorSerializer
    
    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self, request, *args, **kwargs)
        ob = prerecord.objects.latest('id')
        #res = ABML.cls(ob)
        lo = ABML.pred(ob)
        return Response({"status": "Non-Resistant","non-resistant":lo, 'tmp':args})

 
        

        



#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all().order_by("-id")
#    serializer_class = UserSerializer

























#from django.shortcuts import render
#from django.conf import settings 
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import authentication, permissions
#from django.contrib.auth.models import User

#predictor = getattr(settings, 'predictor', 'the_default_value')


#class myClass(APIView):
 #   permission_classes = (permissions.AllowAny,)

  #  '''Httpverb post method'''
   # def post(self, request,format=None):

    #    predictor = getattr(settings, 'abpredictor.pkl', 'the_default_value')
     #   data = preparePostData(request.data)
      #  res = predictor.predict_proba(data).tolist()
      #  message = preareMessage(res)
      #  return Response(message, status=status.HTTP_200_OK)

