from urllib import response
from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from datosbecas.models import Becario, Estudio, Beca

from datosbecas.serializers import BecarioSerializer, EstudioSerializer, BecaSerializer

#Create your views here.
class RetrieveBecario(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        becarios_list = Becario.objects.all().values()
        serializer = BecarioSerializer(becarios_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBecario(APIView):
    def post(self, request):
        data = request.data
        serializer = BecarioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveEstudio(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        estudios_list = Estudio.objects.all().values()
        serializer = EstudioSerializer(estudios_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateEstudio(APIView):
    def post(self, request):
        data = request.data
        serializer = EstudioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveBeca(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        beca_list = Beca.objects.all().values()
        serializer = BecaSerializer(beca_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBeca(APIView):
    def post(self, request):
        data = request.data
        serializer = BecaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveBeca