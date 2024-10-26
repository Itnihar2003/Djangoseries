from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from .models import student
from .serializer import studentserializer
# Create your views here.
def singlestudent(request,pk):
    stu=student.objects.get(id=pk)
    print(stu)
    serialize=studentserializer(stu)
    print(serialize)
    print(serialize.data)
    return JsonResponse(serialize.data,safe=True)
def allstudent(request):
    stu=student.objects.all()
    serialize=studentserializer(stu,many=True)
    return JsonResponse(serialize.data,safe=False)