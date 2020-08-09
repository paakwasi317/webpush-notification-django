from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404  
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.conf import settings
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import Users
from Users.serializers import UserSerializer, NoPasswwordUserSerializer
from Madakoraa.utilities import Utilities

init = Utilities()

class UserList(APIView):

    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        elif self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
            

    
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = NoPasswwordUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        utility = Utilities()
        
        email = request.data['email']
        name = request.data['firstname']
        msg = "Hello "+name+"!!\n"
        msg += "Thanks for signing up on Madakoraa."
        print(msg)
        subject = "Welcome to the lifestyle"
        header = "Madakoraa"

        pk = utility.GenerateUserId()
        numberid = str(next(pk))
        username = name+numberid

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=username)
            res=utility.sendgridNew(email, name, msg, subject, header)
            print(res)

            data = 'User successfully created'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = NoPasswwordUserSerializer(users)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = NoPasswwordUserSerializer(users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = 'User successfully updated'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        users = self.get_object(pk)
        users.delete()
        data = 'User successfully deleted'
        return Response(data=data,status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def GetUserInfo(request):
    userid = request.user.id
    users = Users.objects.get(pk=userid)
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    print(vapid_key)
    serializer = NoPasswwordUserSerializer(users)
    data = serializer.data
    data["vapid_key"] = vapid_key
    print(serializer.data)
    return Response(data)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def UserLogin(request):
    number = request.data['number']
    try:
        users = Users.objects.get(phone=number)
        name = Users.objects.get(phone=number).firstname
        pk = init.GenerateUserId()
        numberid = str(next(pk))
        data = {}
        serializer = NoPasswwordUserSerializer(users, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(code = numberid)
        message = "Hello "+name+", Welcome to Madakoraa, your verification code is "+numberid
        sms = init.send_sms(number, message)
        
    except Users.DoesNotExist:
        data = {}
        data['details'] = "User not found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def CodeVerification(request):
    number = request.data['code']
    try:
        user = Users.objects.get(code=number)
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    except Users.DoesNotExist:
        data = {}
        data['details'] = "User not found."
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    return Response(data=data, status=status.HTTP_202_ACCEPTED)