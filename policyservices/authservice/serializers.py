'''
Serializer class to create User serializer and Login Serialier
'''
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializer class for User model
    :model:Policy
    '''
    class Meta:
        '''
        Container class for User model
        '''
        model = User
        fields=('id','username','email')


#pylint: disable=W0223
class LoginSerializer(serializers.Serializer):
    '''
    Serializer class for Login Model
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self,data):
        '''
        User authentication validation
        :params:username and email
        :returns: user data on successful authentication
        '''
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise(serializers.ValidationError('Incorrect Credentials'))
