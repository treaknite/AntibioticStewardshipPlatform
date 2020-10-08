
from predictor.models import predictor #antibiotics_details
from rest_framework import serializers

class predictorSerializer(serializers.ModelSerializer):
    class Meta:
        model = predictor
        fields = "__all__"

#print(predictorSerializer(ob).data)


    
        #antibiotics_details
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ('username',    'password')
