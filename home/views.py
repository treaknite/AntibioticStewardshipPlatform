
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Record,Rcord
from django.contrib import auth
from home import views
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
from .forms import UploadrecordForm
import csv, io
import pandas as pd 
from django.db.models import Q
from django.contrib import messages

from .models import *
 


# Create your views here.
def home(request):

    return render(request, 'home/home.html') 

def login(request):
    context={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'home/main.html')
        else:
            context['error']="provide valid credentials!!"
            

    
    return render(request, 'home/login.html',context)

def search(request):
    context={}
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=Record.objects.filter(Q(PatientId__icontains=srch))
            

            if match:
                return render(request,'home/search.html',{'sr':match})
            else:
                print("no result found")
                context['error']="no result found"
    else:
        context['error']="provide valid credentials!!"
            #return render(request,'home/search.html')


    return render(request,'home/search.html')



def logout(request):
    if request.method=='POST':
        logout(request)
        return render(request,'home/login.html',{})


 
def main(request):
    
    return render(request, 'home/main.html')
def pastrecord(request):

    
    return render(request,"home/pastrecord.html")
def pastrecord(request):
    pastrecord=Record.objects.all().order_by('PatientId')     
    return render(request,'home/pastrecord.html',{'pastrecord':pastrecord,})


def uploadrecord(request):
          
     return render(request,'home/uploadrecord.html')

def uploadrecordsub(request):      
    print('hello form is submitted')
    id = request.POST['id']
    try:
          antibiotic1 = request.POST['antibiotic1']
          
          
          ar_1 = request.POST['ar_1']
    except MultiValueDictKeyError:
         antibiotic1 = None
         
         
         ar_1 = None
         
    try:
         antibiotic2 = request.POST['antibiotic2']
         
         
         ar_2 = request.POST['ar_2']

    except MultiValueDictKeyError:
         antibiotic2 = None
        
         
         ar_2 = None

     
    try:

          antibiotic3 = request.POST['antibiotic3']
          
          
          ar_3 = request.POST['ar_3']

          
    except MultiValueDictKeyError:
          antibiotic3 = None
          
          
          ar_3 = None

    try:

          antibiotic4 = request.POST['antibiotic4']
          
          
          ar_4 = request.POST['ar_4']

          
    except MultiValueDictKeyError:
          antibiotic4 = None
          
          
          ar_4 = None
  
    in1 = request.POST['in1']
    city = request.POST['city']
    state = request.POST['state']
    age = request.POST['age']
    gender = request.POST['gender']
    try:
         pregnancy = request.POST['pregnancy']
    except MultiValueDictKeyError:
         pregnancy = None   
    istate = request.POST['istate']
    
    

    record_upl = Record(FirstAntibiotic  = antibiotic1,PatientId=id, ar_1=ar_1,SecondAntibiotic = antibiotic2,ar_2=ar_2,ThirdAntibiotic=antibiotic3,ar_3=ar_3,FourthAntibiotic=antibiotic4,ar_4=ar_4,in1=in1, city=city,state=state,age=age,gender=gender,pregnancy=pregnancy,immunestatus=istate )
    record_upl.save()

                
    


    items = Record.objects.all()
    with open ('data1.csv','a') as csvfile:
        writer = csv.writer(csvfile , delimiter=',')
        #writer.writerow(['Antibiotic','ar', 'age','infection','location','gender','pregnancy','immunestatus'])

        for obj in items:
  
             writer.writerow([obj.FirstAntibiotic,obj.ar_1, obj.age, obj.in1,obj.city,obj.gender,obj.pregnancy or 'not applicable',obj.immunestatus])
             writer.writerow([obj.SecondAntibiotic,obj.ar_2, obj.age,obj.in1,obj.city,obj.gender,obj.pregnancy or 'not applicable',obj.immunestatus])
             writer.writerow([obj.ThirdAntibiotic,obj.ar_3, obj.age,obj.in1,obj.city,obj.gender,obj.pregnancy or 'not applicable' ,obj.immunestatus])
             writer.writerow([obj.FourthAntibiotic,obj.ar_4, obj.age, obj.in1,obj.city,obj.gender,obj.pregnancy or 'not applicable',obj.immunestatus])
    
                  

    ab = pd.read_csv('data1.csv')
    d = ab.dropna()
    d.to_csv('data.csv',index=False)
    
       
    return render(request,'home/uploadrecord.html')
def prerecord(request):
          
    return render(request,'home/prerecord.html')

def prerecordsub(request): 
    # print('hello form is submitted')
    if request.method=='POST':
      antibiotic = request.POST['antibiotic']
      in1 = request.POST['infection']
      city = request.POST['location']
      age = request.POST['age']
      gender = request.POST['gender']
      try:
                pregnancy = request.POST['pregnancy']
      except MultiValueDictKeyError:
                  pregnancy = False   
      istate = request.POST['immunestatus']
    
    

      record_ul = Rcord(antibiotic  = antibiotic,infection=in1, location=city,age=age,gender=gender,pregnancy=pregnancy,immunestatus=istate )
      record_ul.save()
      myDict = (request.POST).dict()
      df=pd.DataFrame(myDict, index=[0])

      answer=approvereject(ohevalue(df))[0]
      Xscalers=approvereject(ohevalue(df))[1]
      messages.success(request,'Application Status: {}'.format(answer))
    form=answer

    return render(request,'home/prerecord.html',{'form':form})          
  

class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers

def ohevalue(df):
	ohe_col=joblib.load("allcol.pkl")
	cat_columns=['antibiotic','age','infection','location','gender','pregnancy', 'immunestatus']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	newdf=pd.DataFrame(newdict,index=[0])
	return newdf

def approvereject(unit):
	try:
		import keras.backend.tensorflow_backend as tb
		tb._SYMBOLIC_SCOPE.value = True
		mdl=joblib.load("loan_model.pkl")
		scalers=joblib.load("scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Resistant', False:'Non-Resistant'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])

def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				antibiotic = form.cleaned_data['antibiotic']
				age = form.cleaned_data['age']
				location = form.cleaned_data['location']
				gender = form.cleaned_data['gender']
				pregnancy = form.cleaned_data['pregnancy']
				immunestatus = form.cleaned_data['immunestatus']
				infection = form.cleaned_data['infection']
				myDict = (request.POST).dict()
				df=pd.DataFrame(myDict, index=[0])
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				if int(df['age'])<120:
					messages.success(request,'Antibiotic Status: {}'.format(answer))
				else:
					messages.success(request,'Invalid Age')
	
	form=ApprovalForm()
				
	return render(request, 'home/cxform.html', {'form':form})

def cxcontact2(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				antibiotic = form.cleaned_data['antibiotic']
				age = form.cleaned_data['age']
				location = form.cleaned_data['location']
				gender = form.cleaned_data['gender']
				pregnancy = form.cleaned_data['pregnancy']
				immunestatus = form.cleaned_data['immunestatus']
				infection = form.cleaned_data['infection']
				myDict = (request.POST).dict()
				df=pd.DataFrame(myDict, index=[0])
        
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				messages.success(request,'Application Status: {}'.format(answer))
	
	form=ApprovalForm()
				
	return render(request, 'home/form.html', {'form':form})



