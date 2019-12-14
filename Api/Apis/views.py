from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView,status
from .models import Goods
from .serializers import GoodsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
# Create your views here.

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
class TokenAuth(BaseAuthentication):
    def authenticate(self,request):
        token = request.META.get("HTTP_AUTHENTICATION",None)
        print(request.META)
        print(token)
        if token:
            obj = Token.objects.filter(key=token)
            if obj:
                return None
        raise exceptions.AuthenticationFailed('token 异常')


class Goodsp(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    def get(self,request,*args,**kwargs):
        goods = Goods.objects.all()
        se = GoodsSerializer(goods,many=True)
        print(se.data)
        return Response({'code':200,'msg':se.data})
    #增
    def post(self,request):
        goodsser = GoodsSerializer(data=request.data)
        #验证
        if goodsser.is_valid():
            goodsser.save()#增
            return Response(goodsser.data,status=status.HTTP_200_OK)
        print(goodsser.is_valid())
        return Response(goodsser.errors,status=status.HTTP_400_BAD_REQUEST)

class GoodsOneview(APIView):
    def put(self,request,*args,**kwargs):
        goodsser = GoodsSerializer(data=request.data)
        if goodsser.is_valid():
            goodsser.update(Goods.objects.filter(id=kwargs['id']).first(),request.data)#改
            return Response(goodsser.data,status=status.HTTP_200_OK)
        return Response(goodsser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        obj = Goods.objects.filter(id=kwargs['id']).first()
        if obj:
            obj.delete()#删
            return Response({'msg':'ok'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            token = Token.objects.filter(user_id=user.id).first()
            # print(token.key)
            return Response({'msg':'ok','token':token.key})
        else:
            return Response({'msg':'no'})

