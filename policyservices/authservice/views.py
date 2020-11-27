'''
Authentication view for User authentication
'''
from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,LoginSerializer


#LogIn API
class Login(generics.GenericAPIView):
    '''
    Login View for user authentication and login
    :model:User
    '''
    serializer_class = LoginSerializer
    def post(self,request):
        '''
        User is validated against username and password
        :returns:authToken
        '''
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        _,token = AuthToken.objects.create(user)
        return Response({
            "user":UserSerializer(user,
                context=self.get_serializer_context()).data,
            "token":token
        })

#User API
class UserView(generics.RetrieveAPIView):
    '''
    View to get User data
    :model:User
    '''
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    def get_object(self):
        '''
        :returns:User data
        '''
        return self.request.user
