

import pandas as pd
import csv
i = []
k = []
count = 0
fd = pd.read_csv('data.csv')
pre_y = fd['resistance']
pre_X = fd.drop('resistance',axis = 1)
dm_X = pd.get_dummies(pre_X)
dm_y = pre_y.map(dict(Y=1, N=0))
from sklearn.externals import joblib
filename = "allcol.pkl"
joblib.dump(dm_X, filename)

#for col in dm_X.columns:
#    if count < 10000:
#        i.append(col)
#        count += 1
#    #print (i)
#for j in range(0,len(i)):
#    k.append(i[j])
#    k.append("0")
#    #print (k)
#def Convert(k): 
#    k1 = {k[i]: k[i + 1] for i in range(0, len(k), 2)} 
#    return k1
#nd = Convert(k)
#print (nd)
#api1 = res
#    for key in api1.keys():
#        if api1['antibiotic'] == "piperacillin":
#            nd['antibiotic_Piperacillin'] = '1'
#        else:
#            if api1['antibiotic'] == "aminoglycoside":       
#                nd['antibiotic_Aminoglycoside'] = '1'
        
#            elif api1['antibiotic'] == "ampicillin":       
#                nd['antibiotic_Ampicillin'] = '1'
       

#            elif api1['antibiotic'] == "linezolid":    
#                nd['antibiotic_Linezolid'] = '1'
        

#            elif api1['antibiotic'] == "carbapenem":       
#                nd['antibiotic_carbapenem'] = '1'
        
#            elif api1['antibiotic'] == "metronidazole":       
#                nd['antibiotic_Metronidazole'] = '1'
        

#            elif api1['antibiotic'] == "fluoroquinolone":     
#                nd['antibiotic_Fluoroquinolone'] = '1'
       
#            elif api1['antibiotic'] == "clindamycin":
#                nd['antibiotic_Clindamycin'] = '1'

    
#        if api1['gender'] == 'male':
#            nd['gender_Male'] = '1'
        
#        elif api1['gender'] == 'female':
#            nd['gender_Female'] = '1'
#            if api1['pregnancy'] == 'TRUE':
#                nd['pregnancy'] ='1'
        
#        if api1['immune'] == 'TRUE':
#            nd['immune'] ='1'
  
#        nd['age'] = api1['age']

#        if api1['location'] == 'delhi':
#            nd['location_delhi'] = '1'
            
#        elif api1['location'] == 'gurgaon':
#            nd['location_gurgaon'] = '1'
            
#        elif api1['location'] == 'raipur':
#            nd['location_raipur'] = '1'
           
#        elif api1['location'] == 'bhubhaneshwar':
#            nd['location_bhubhaneshwar'] = '1'

#        elif api1['location'] == 'noida':
#            nd['location_noida'] = '1'

#        elif api1['location'] == 'srinagar':
#            nd['location_srinagar'] = '1'

#        elif api1['location'] == 'lucknow':
#            nd['location_lucknow'] = '1'

#        elif api1['location'] == 'ghaziabad':
#            nd['location_ghaziabad'] = '1'

#        elif api1['location'] == 'kanpur':
#            nd['location_kanpur'] = '1'

#        if api1['infection'] == "upper/lower respiratory tract infection":
#            #nd['infection_Abdominal infection/Peritonitis']: '0'
#            #nd['infection_Bones and Joints Sepsis']: '0'
#            #nd['infection_Pyogenic meningitis']: '0'
#            nd['infection_Upper/Lower Respiratory Tract Infection'] = '1'
#            #nd['infection_Urinary Tract infection']: '1'
#            #nd['infection_Soft Tissue Infection']: '0'
        
#        elif api1['infection'] == "infection_Abdominal infection/Peritonitis":
#            nd['infection_Abdominal infection/Peritonitis'] = '1'
        
#        elif api1['infection'] == "bones and joints sepsis":
#            nd['infection_Bones and Joints Sepsis'] = '1'

#        elif api1['infection'] == "Pyogenic meningitis":
#            nd['infection_Pyogenic meningitis'] = '1'

#        elif api1['infection'] == "urinary tract infection":
#            nd['infection_Urinary Tract infection'] = '1'

#        elif api1['infection'] == "soft tissue infection":
#            nd['infection_Soft Tissue Infection'] = '1'


################# EXTRA CODE HERE #########################

#    return nd
#r1 = {
#    "antibiotic": "fluoroquinolone",
#    "age": 30,
#    "resistance": "FALSE",
#    "gender": "female",
#    "pregnancy": "TRUE",
#    "immune": "TRUE",
#    "location": "kanpur",
#    "infection": "soft tissue infection"
#}
#print (pred(r1))
























#import pandas as pd
#import csv
#i = []
#k = []
#count = 0
#df = pd.read_csv('MOCK_DATA1.csv')
#df = df.dropna()
#df = df.dropna()
#df.isna().any()
#pre_y = df['resistance']
#pre_X = df.drop('resistance',axis = 1)
#dm_X = pd.get_dummies(pre_X)
#dm_y = pre_y.map(dict(Y=1, N=0))
#for col in dm_X.columns:
#    if count < 10000:
#        i.append(col)
#        count += 1
#print (i)
#for j in range(0,len(i)):
#    k.append(i[j])
#    k.append("0")
#print (k)
#def Convert(k): 
#    k1 = {k[i]: k[i + 1] for i in range(0, len(k), 2)} 
#    return k1
#nd = Convert(k)
#print (nd)
#api2 = {"antibiotic": "Piperacillin", "age": 19, "resistance": "FALSE", "gender": "Male", "pregnancy": "FALSE", "immune": "TRUE", "location": "DELHI", "infection": "Upper/Lower Respiratory Tract Infection"}
#api1 = api2
#for key in api1.keys():
#    if api1['antibiotic'] == "Piperacillin":
#        nd['antibiotic_Piperacillin'] = '1'
#    else:
#        if api1['antibiotic'] == "Aminoglycoside":       
#            nd['antibiotic_Aminoglycoside']: '1'
        
#        elif api1['antibiotic'] == "Ampicillin":       
#            nd['antibiotic_Ampicillin']: '1'
       

#        elif api1['antibiotic'] == "Linezolid":    
#            nd['antibiotic_Linezolid']: '1'
        

#        elif api1['antibiotic'] == "carbapenem":       
#            nd['antibiotic_carbapenem']: '1'
        

#        elif api1['antibiotic'] == "Metronidazole":       
#            nd['antibiotic_Metronidazole']: '1'
        

#        elif api1['antibiotic'] == "Fluoroquinolone":     
#            nd['antibiotic_Fluoroquinolone']: '1'
       

#        else:
#            nd['antibiotic_Clindamycin']: '1'

    
#    if api1['gender'] == 'Male':
#            nd['gender_Male'] = '1'
#    else:
#        nd['gender_Female']: '1'
#        if api1['pregnancy'] == 'TRUE':
#            nd['pregnancy'] ='1'
        
#    if api1['immune'] == 'TRUE':
#        nd['immune'] ='1'
  
#    nd['age'] = api1['age']

#    if api1['location'] == 'DELHI':
#        nd['location_delhi'] = '1'
            
#    elif api1['location'] == 'gurgaon':
#        nd['location_gurgaon'] = '1'
            
#    elif api1['location'] == 'raipur':
#        nd['location_raipur'] = '1'
           
#    elif api1['location'] == 'bhubhaneshwar':
#        nd['location_bhubhaneshwar'] = '1'

#    elif api1['location'] == 'noida':
#        nd['location_noida'] = '1'

#    elif api1['location'] == 'srinagar':
#        nd['location_srinagar'] = '1'

#    elif api1['location'] == 'lucknow':
#        nd['location_lucknow'] = '1'

#    elif api1['location'] == 'ghaziabad':
#        nd['location_ghaziabad'] = '1'

#    elif api1['location'] == 'kanpur':
#        nd['location_kanpur'] = '1'

#    if api1['infection'] == "Upper/Lower Respiratory Tract Infection":
#            nd['infection_Abdominal infection/Peritonitis']: '0'
#            nd['infection_Bones and Joints Sepsis']: '0'
#            nd['infection_Pyogenic meningitis']: '0'
#        nd['infection_Upper/Lower Respiratory Tract Infection'] = '1'
#            nd['infection_Urinary Tract infection']: '1'
#            nd['infection_Soft Tissue Infection']: '0'

#print (nd)









#def cls(ob):
#    import pandas as pd
#    import csv
#    i = []
#    k = []
#    count = 0
#    fd = pd.read_csv('MOCK_DATA1.csv')
#    pre_y = fd['resistance']
#    pre_X = fd.drop('resistance',axis = 1)
#    dm_X = pd.get_dummies(pre_X)
#    dm_y = pre_y.map(dict(Y=1, N=0))
#    for col in dm_X.columns:
#        if count < 10000:
#            i.append(col)
#            count += 1
#    #print (i)
#    for j in range(0,len(i)):
#        k.append(i[j])
#        k.append("0")
#    #print (k)
#    def Convert(k): 
#        k1 = {k[i]: k[i + 1] for i in range(0, len(k), 2)} 
#        return k1
#    nd = Convert(k)
#    #print (nd)
#    api1 = dct1
#    for key in api1.keys():
#        if api1['antibiotic'] == "Piperacillin":
#            nd['antibiotic_Piperacillin'] = '1'
#        else:
#            if api1['antibiotic'] == "Aminoglycoside":       
#                nd['antibiotic_Aminoglycoside']: '1'
        
#            elif api1['antibiotic'] == "Ampicillin":       
#                nd['antibiotic_Ampicillin']: '1'
       

#            elif api1['antibiotic'] == "Linezolid":    
#                nd['antibiotic_Linezolid']: '1'
        

#            elif api1['antibiotic'] == "carbapenem":       
#                nd['antibiotic_carbapenem']: '1'
        
#            elif api1['antibiotic'] == "Metronidazole":       
#                nd['antibiotic_Metronidazole']: '1'
        

#            elif api1['antibiotic'] == "Fluoroquinolone":     
#                nd['antibiotic_Fluoroquinolone']: '1'
       
#            else:
#                nd['antibiotic_Clindamycin']: '1'

    
#        if api1['gender'] == 'Male':
#            nd['gender_Male'] = '1'
#        else:
#            nd['gender_Female']: '1'
#            if api1['pregnancy'] == 'TRUE':
#                nd['pregnancy'] ='1'
        
#        if api1['immune'] == 'TRUE':
#            nd['immune'] ='1'
  
#        nd['age'] = api1['age']

#        if api1['location'] == 'DELHI':
#            nd['location_delhi'] = '1'
            
#        elif api1['location'] == 'gurgaon':
#            nd['location_gurgaon'] = '1'
            
#        elif api1['location'] == 'raipur':
#            nd['location_raipur'] = '1'
           
#        elif api1['location'] == 'bhubhaneshwar':
#            nd['location_bhubhaneshwar'] = '1'

#        elif api1['location'] == 'noida':
#            nd['location_noida'] = '1'

#        elif api1['location'] == 'srinagar':
#            nd['location_srinagar'] = '1'

#        elif api1['location'] == 'lucknow':
#            nd['location_lucknow'] = '1'

#        elif api1['location'] == 'ghaziabad':
#            nd['location_ghaziabad'] = '1'

#        elif api1['location'] == 'kanpur':
#            nd['location_kanpur'] = '1'

#        if api1['infection'] == "Upper/Lower Respiratory Tract Infection":
#            #nd['infection_Abdominal infection/Peritonitis']: '0'
#            #nd['infection_Bones and Joints Sepsis']: '0'
#            #nd['infection_Pyogenic meningitis']: '0'
#            nd['infection_Upper/Lower Respiratory Tract Infection'] = '1'
#            #nd['infection_Urinary Tract infection']: '1'
#            #nd['infection_Soft Tissue Infection']: '0'

#    return nd

#ob = {"antibiotic": "Piperacillin", "age": 19, "resistance": "FALSE", "gender": "Male", "pregnancy": "FALSE", "immune": "TRUE", "location": "DELHI", "infection": "Upper/Lower Respiratory Tract Infection"}
##print (len(cls(ob)))
#print (cls(ob))


    






        


        





    

        
