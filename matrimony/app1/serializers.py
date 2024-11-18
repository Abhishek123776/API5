from rest_framework import serializers
from .models import Basicdetails
class BasicdetialsSerializer(serializers.Serializer):
    age=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    surname=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=40)

    def create(self, validated_data):
        age=validated_data['age']
        name=validated_data['name']
        surname=validated_data['surname']
        email=validated_data['email']

        obj=Basicdetails(age=age,name=name,surname=surname,email=email)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.age=validated_data.get['age']
        instance.name=validated_data.get['name']
        instance.surname=validated_data.get['surname']
        instance.email=validated_data.get['email']
        instance.save()
        return instance