from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . models import*

class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model=Registration
        fields = ['id','name','email','phone_no','password','confirm_password']

    def validate_data(self,data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError('Password do not match')
        return data
        
    def create(self,validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return Registration.objects.create(**validated_data)