'''
serializer file to define model serializers
'''
from rest_framework import serializers
from .models import Policy

#Policy Serializer class
class PolicySerializer(serializers.ModelSerializer):
    '''
    Policy Serializer class
    :model:Policy
    '''
    class Meta:
        '''
        Meta container class for Policy Model
        Defines read only fields only Premium can be updated
        '''
        model=Policy
        fields = '__all__'
        read_only_fields=['policyId','purchaseDate','fuel',
                          'vehicleSegment','bodilyInjuryLiability',
                          'personalInjuryProtection','propertyDamageLiability',
                          'collision','comprehensive','customer']
        depth = 1
        