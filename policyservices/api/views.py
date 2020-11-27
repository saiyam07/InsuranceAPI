'''
Views to get and update Policy data are defined here
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Extract
from django.db.models import  Count
from django.core.exceptions import ObjectDoesNotExist
from .models import Policy
from .serializers import PolicySerializer

# Create your views here.
class PolicyView(ListAPIView):
    '''
    View to get the policy through policy ID
    :model:Policy
    '''
    permission_classes=[IsAuthenticated]
    model = Policy
    serializer_class = PolicySerializer
    def get_queryset(self):
        '''
        Query Set fromed by matching the policy ID
        :param:PolicyId
        :returns:Policy
        '''
        policy_id = self.request.query_params.get('policy',None)
        self.request.query_params.get('policy')
        if policy_id is not None:
            policy = Policy.objects.filter(policyId = policy_id)
            return policy
        raise ObjectDoesNotExist

class CustomerPolicyView(ListAPIView):
    '''
    View to get the Custome Policies
    :model:Policy
    '''
    permission_classes=[IsAuthenticated]
    model = Policy
    serializer_class = PolicySerializer
    def get_queryset(self):
        '''
        Query set created using the customer id
        :params:customerId
        :returns:Polices
        '''
        customer = self.request.query_params.get('customer',None)
        if customer is not None:
            queryset = Policy.objects.filter(customer_id = customer)
            return queryset
        return ObjectDoesNotExist

class PolicyUpdateView(UpdateAPIView):
    '''
    Policy Update view to update policy premium
    :model:policy
    :param:policyId
    '''
    permission_classes=[IsAuthenticated]
    model = Policy
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()

class PolicyRegionalSalesView(APIView):
    '''
    Policy Sales View to get the monthly sales view of the policy
    :model:Policy
    '''
    permission_classes=[IsAuthenticated]
    model = Policy
    serializer_class = PolicySerializer
    def get(self,request,**kwargs):
        '''
        Query Set created for getting the policies in a particular region in different months
        :returns:JSON Object with keys policy,purchase month for a specific region
        '''
        #group by customer region and purchase month
        region = request.GET.get('region')
        regional_policy_sales = Policy.objects.annotate(
                    month=Extract('purchaseDate','month')).values('month').annotate(
                    policies=Count('policyId')).filter(customer__region=region).order_by('month')
        return Response(regional_policy_sales)


class PolicyMonthlySalesView(APIView):
    '''
    View to get the monthly sales view of the policy
    :model:Policy
    '''
    permission_classes=[IsAuthenticated]
    model = Policy
    serializer_class = PolicySerializer
    def get(self,request):
        '''
        Query Set created by grouping the policy by their purchase month
        :returns:Policy Count grouped monthly
        '''
        monthly_policy_sales = Policy.objects.annotate(
                    month=Extract('purchaseDate','month')).values('month').annotate(
                    policies=Count('policyId')).order_by('month')
        return Response(monthly_policy_sales)