from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import BasicdetialsSerializer
from . models import Basicdetails
from rest_framework import status
# Create your views here.

class Basicdetails_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Basicdetails.objects.all()
            serializer=BasicdetialsSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Basicdetails,id=pk)
        serializer=BasicdetialsSerializer(objs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=BasicdetialsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data,status=status.HTTP_201_CREATED)
        return Response(data={"msg":"DATA IS INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        obj=Basicdetails.objects.get(id=pk)
        serializer=BasicdetialsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        obj=Basicdetails.objects.get(id=pk)
        serializer=BasicdetialsSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data={"msg":"DATA INVALID"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Basicdetails,id=pk)
        obj.delete()
        return Response(data={"msg":"DATA DELETED"},status=status.HTTP_200_OK)