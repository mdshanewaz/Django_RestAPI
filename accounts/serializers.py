from asyncore import write
from pyexpat import model
from tkinter.ttk import Style
from xml.dom import ValidationErr
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password2 != password:
            raise ValidationErr({'password' : 'Passwords did not matche'})
        
        user.set_password(password)
        user.save()
        return user