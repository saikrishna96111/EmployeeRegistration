from EmployeeHome.models import Employeedb
from rest_framework import serializers


class ListSerializer(serializers.Serializer):
    ssn=serializers.IntegerField()
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    dob=serializers.DateField()
    city=serializers.CharField()
    
    def create(self, validated_data):
        return Employeedb.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.dob=validated_data.get('dob',instance.dob)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance