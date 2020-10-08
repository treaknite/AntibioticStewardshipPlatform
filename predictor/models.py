from django.db import models

class predictor(models.Model):
    antibiotic = models.CharField(max_length=30, default = 'SOME STRING')
    age = models.IntegerField()
    resistance = models.CharField(max_length=30, default = 'SOME STRING')
    gender = models.CharField(max_length=30, default = 'SOME STRING')
    pregnancy = models.CharField(max_length=30, default = 'SOME STRING')
    immune = models.CharField(max_length=30, default = 'SOME STRING')
    location = models.CharField(max_length=30, default = 'SOME STRING')
    infection = models.CharField(max_length=100, default = 'SOME STRING')

#def to_dict(self):
#    return {
#        'antibiotic':self.antibiotic ,
#        'age':self.age ,
#        'resistance':self.resistance ,
#        'gender':self.gender ,
#        'pregnancy':self.pregnancy ,
#        'immune':self.immune ,
#        'location':self.location ,
#        'infection':self.infection
 #       }
      

   
    
    
   

