from django.db import models

# Create your models here.
class Record(models.Model):
    PatientId = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    FirstAntibiotic = models.CharField(max_length=50,blank = True,null = True,default='SOME STRING')
    #ag_1 = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    #Days1 = models.CharField(max_length=10,blank = True,null = True,default='SOME STRING' )
    ar_1 = models.CharField(max_length=40,blank = True,null = True,default= 'SOME STRING')
    SecondAntibiotic = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    #ag_2 = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    #Day2 = models.CharField(max_length=10,blank = True,null = True,default= 'SOME STRING' )
    ar_2 = models.CharField(max_length=40,blank = True,null = True, default= 'SOME STRING')
    ThirdAntibiotic = models.CharField(max_length=50,blank = True,null = True, default='SOME STRING')
    #ag_3 = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    #Days3 = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    ar_3 = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
    FourthAntibiotic = models.CharField(max_length=50,blank = True,null = True, default='SOME STRING')
    #ag_4 = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    ar_4 = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
    in1 = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
    city = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
    state = models.CharField(max_length=30,blank = True,null = True, default='SOME STRING')
    age = models.CharField(max_length=30,blank = True,null = True, default='SOME STRING')
    gender = models.CharField(max_length=20,blank = True,null = True, default='SOME STRING')
    pregnancy = models.CharField(max_length=20,blank = True,null = True,default='SOME STRING')
    immunestatus = models.CharField(max_length=10, blank = True,null = True,default='SOME STRING')
    #outcome = models.CharField(max_length=30)


class approvals(models.Model):
    antibiotic = models.CharField(max_length=50,blank = True,null = True,default='SOME STRING')
    
     
    age = models.CharField(max_length=30,blank = True,null = True, default='SOME STRING')
    infection = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
    location = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
 
    gender = models.CharField(max_length=20,blank = True,null = True, default='SOME STRING')
    pregnancy = models.CharField(max_length=20,blank = True,null = True,default='SOME STRING')
    immunestatus = models.CharField(max_length=10, blank = True,null = True,default='SOME STRING')
class Rcord(models.Model):    
      antibiotic = models.CharField(max_length=50,blank = True,null = True,default='SOME STRING')
      infection = models.CharField(max_length=50,blank = True,null = True, default= 'SOME STRING')
      location = models.CharField(max_length=40, blank = True,null = True,default= 'SOME STRING')
      age = models.CharField(max_length=30,blank = True,null = True, default='SOME STRING')
      
      
 
      gender = models.CharField(max_length=20,blank = True,null = True, default='SOME STRING')
      pregnancy = models.CharField(max_length=20,blank = True,null = True,default='SOME STRING')
      immunestatus = models.CharField(max_length=10, blank = True,null = True,default='SOME STRING')
def __str__(self):
        return '{}'.format(self.antibiotic)
   
   

        
                