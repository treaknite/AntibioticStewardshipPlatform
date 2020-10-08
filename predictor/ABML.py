import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
#from imblearn import under_sampling, over_sampling
from sklearn.preprocessing import MinMaxScaler
#from predictor.models import predictor
import warnings
#from predictor.myserializer import predictorSerializer
from  collections import Counter
warnings.filterwarnings('ignore')
#import matplotlib.pyplot as plt
from keras.layers import Dense
#from predictor import views
from django.forms.models import model_to_dict
import json
from keras import Sequential

#from collections import OrderedDict, defaultdict




def training(df):
    df = df.dropna()
    df.isna().any()
    #df = df.drop('id', axis=1)
    pre_y = df['resistance']
    pre_X = df.drop('resistance',axis = 1)
    dm_X = pd.get_dummies(pre_X)
    dm_y = pre_y.map(dict(Y=1, N=0))
    #smote = SMOTE(ratio='minority')   #for balancing yes/nos
    #X1, y = smote.fit_sample(dm_X, dm_y)
    sc = MinMaxScaler()
    X = sc.fit_transform(dm_X)
    #Counter(y)
    X_train, X_test, dm_y_train, dm_y_test = train_test_split(X, dm_y, test_size=0.3, random_state = 42, shuffle = True)
    classifier = Sequential()
    classifier.add(Dense(units = 400, activation = 'relu', kernel_initializer='random_normal', input_dim=X_test.shape[1]))
    classifier.add(Dense(units = 800, activation = 'relu', kernel_initializer='random_normal'))
    classifier.add(Dense(units = 10, activation = 'relu', kernel_initializer='random_normal'))
    classifier.add(Dense(units = 1, activation = 'sigmoid', kernel_initializer='random_normal'))
    classifier.compile(optimizer='adam',loss = 'binary_crossentropy', metrics = ['accuracy'])
    classifier.fit(X_train,dm_y_train,batch_size=30,epochs=100,verbose=0)
    eval_model = classifier.evaluate(X_train, dm_y_train)
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred>0.5)
    #print (y_pred)
    import pickle
    from sklearn.externals import joblib
    filename = "abpredictor.pkl"
    joblib.dump(classifier, filename)
    #a lot of yes' hidden in 0.4 and 0.5

if __name__=='__main__':
    df = pd.read_csv('C:\\Users\\pawan\\Desktop\\pharmafuture\\pharmafuture\\predictor\\data.csv')
    training(df)
    
    
#def cls(ob):
#    dct = predictorSerializer(ob).data
#    return dct   
           
def pred(ob):
    dct = predictorSerializer(ob).data
    import pandas as pd
    import csv
    i = []
    k = []
    count = 0
    fd = pd.read_csv('MOCK_DATA1.csv')
    pre_y = fd['resistance']
    pre_X = fd.drop('resistance',axis = 1)
    dm_X = pd.get_dummies(pre_X)
    dm_y = pre_y.map(dict(Y=1, N=0))
    for col in dm_X.columns:
        if count < 10000:
            i.append(col)
            count += 1
    #print (i)
    for j in range(0,len(i)):
        k.append(i[j])
        k.append("0")
    #print (k)
    def Convert(k): 
        k1 = {k[i]: k[i + 1] for i in range(0, len(k), 2)} 
        return k1
    nd = Convert(k)
    #print (nd)
    api1 = dct
    for key in api1.keys():
        if api1['antibiotic'] == "piperacillin":
            nd['antibiotic_Piperacillin'] = '1'
        else:
            if api1['antibiotic'] == "aminoglycoside":       
                nd['antibiotic_Aminoglycoside'] = '1'
        
            elif api1['antibiotic'] == "ampicillin":       
                nd['antibiotic_Ampicillin'] = '1'
       

            elif api1['antibiotic'] == "Cephalosporin":    
                nd['antibiotic_Cephalosporin'] = '1'
        
            elif api1['antibiotic'] == "Cephdosporems":    
                nd['antibiotic_Cephdosporems'] = '1'
        

            elif api1['antibiotic'] == "Cindamycine":    
                nd['antibiotic_Cindamycine'] = '1'
            elif api1['antibiotic'] == "Clarithromycin":    
                nd['antibiotic_Clarithromycin'] = '1'
            elif api1['antibiotic'] == "Colistine":    
                nd['antibiotic_Colistine'] = '1'
            elif api1['antibiotic'] == "Deptomycin":    
                nd['antibiotic_Deptomycin'] = '1'
            elif api1['antibiotic'] == "Deptomycine":    
                nd['antibiotic_Deptomycine'] = '1'
            elif api1['antibiotic'] == "Doxycylin":    
                nd['antibiotic_Doxycylin'] = '1'
            elif api1['antibiotic'] == "Erythromycin":    
                nd['antibiotic_Erythromycin'] = '1'
            elif api1['antibiotic'] == "Gentamicin":    
                nd['antibiotic_Gentamicin'] = '1'
            elif api1['antibiotic'] == "Gentamycine":    
                nd['antibiotic_Gentamycine'] = '1'
            elif api1['antibiotic'] == "Manurol":    
                nd['antibiotic_Manurol'] = '1'
            elif api1['antibiotic'] == "Monobactums":    
                nd['antibiotic_Monobactums'] = '1'
            elif api1['antibiotic'] == "Ninocycline":    
                nd['antibiotic_Ninocycline'] = '1'
            elif api1['antibiotic'] == "Penicillins":    
                nd['antibiotic_Penicillins'] = '1'
            elif api1['antibiotic'] == "Polymyxin":    
                nd['antibiotic_Polymyxin'] = '1'
            elif api1['antibiotic'] == "Streptamycine":    
                nd['antibiotic_Streptamycine'] = '1'
            elif api1['antibiotic'] == "Streptomycin":    
                nd['antibiotic_Streptomycin'] = '1'
            elif api1['antibiotic'] == "linezolid":    
                nd['antibiotic_Linezolid'] = '1'
            elif api1['antibiotic'] == "Azithromycine":    
                nd['antibiotic_Azithromycine'] = '1'
        
            

            elif api1['antibiotic'] == "carbapenem":       
                nd['antibiotic_carbapenem'] = '1'
        
            elif api1['antibiotic'] == "metronidazole":       
                nd['antibiotic_Metronidazole'] = '1'
        

            elif api1['antibiotic'] == "fluoroquinolone":     
                nd['antibiotic_Fluoroquinolone'] = '1'
       
            elif api1['antibiotic'] == "clindamycin":
                nd['antibiotic_Clindamycin'] = '1'

    
        if api1['gender'] == 'male':
            nd['gender_Male'] = '1'
        
        elif api1['gender'] == 'female':
            nd['gender_Female'] = '1'
            if api1['pregnancy'] == 'TRUE':
                nd['pregnancy'] ='1'
        
        if api1['immune'] == 'TRUE':
            nd['immune'] ='1'
  
        nd['age'] = api1['age']

        if api1['location'] == 'Delhi':
            nd['location_Delhi'] = '1'
            
        elif api1['location'] == 'Guna':
            nd['location_Guna'] = '1'
            
        elif api1['location'] == 'Jaipur':
            nd['location_Jaipur'] = '1'
           
        elif api1['location'] == 'Jaisalmer':
            nd['location_Jaisalmer'] = '1'

        elif api1['location'] == 'Pune':
            nd['location_Pune'] = '1'

        elif api1['location'] == 'Kharagour':
            nd['location_Kharagour'] = '1'

        elif api1['location'] == 'Kanchipuram':
            nd['location_Kanchipuram'] = '1'

        elif api1['location'] == 'Chennai':
            nd['location_Chennai'] = '1'

        elif api1['location'] == 'Bhopal':
            nd['location_Bhopal'] = '1'

        elif api1['location'] == 'Meerut':
            nd['location_Meerut'] = '1'


        elif api1['location'] == 'Meerut':
            nd['location_Meerut'] = '1'


        elif api1['location'] == 'Ghaziabad':
            nd['location_Ghaziabad'] = '1'

        elif api1['location'] == 'kanpur':
            nd['location_kanpur'] = '1'

        if api1['infection'] == "upper/lower respiratory tract infection":
            nd['infection_Upper/Lower Respiratory Tract Infection'] = '1'
        
        elif api1['infection'] == "Abdominal infection /Peritonitis":
            nd['infection_Abdominal infection/Peritonitis'] = '1'
        
        elif api1['infection'] == "bones and joints sepsis":
            nd['infection_Bones and Joints Sepsis'] = '1'

        elif api1['infection'] == "pyogenic meningitis":
            nd['infection_Pyogenic meningitis'] = '1'

        elif api1['infection'] == "urinary tract infection":
            nd['infection_Urinary Tract infection'] = '1'

        elif api1['infection'] == "soft tissue infection":
            nd['infection_Soft Tissue Infection'] = '1'


################ EXTRA CODE HERE #########################

    return nd
    

    import pickle
    pkl_filename = "abpredictor.pkl"
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict(nd) 
    return pred
    




