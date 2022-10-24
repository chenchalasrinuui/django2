from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from .models import Students
from rest_framework import status
from rest_framework.response import Response
#from myapp.serializers import StudentsSerializer


# Create your views here.

@api_view(["POST"])
def regStudent(request):
    try:
        print("post")
        # data = json.loads(request.body)
        # stdSerializer=StudentsSerializer(data=data)
        # if stdSerializer.is_valid():
        #     stdSerializer.save()
        #     return Response("Success", status=status.HTTP_201_CREATED)
        # return Response("Not Inserted", status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        print(e)

@api_view(["PUT"])
def updateStudent(request):
  try:
    print("put")
    #  obj=Students.objects.get(id = request.headers["id"])
    #  data = json.loads(request.body)
    #  stdSerializer=StudentsSerializer(obj,data=data)
    #  if stdSerializer.is_valid():
    #       stdSerializer.save()
    #       return Response("Success", status=status.HTTP_201_CREATED)
    #  return Response("Not Updated", status=status.HTTP_400_BAD_REQUEST)
  except BaseException as e:
    print(e)

@api_view(["GET"])
def getStudents(request):
    try:
        print("get")
        # students = Students.objects.all()
        # serializer = StudentsSerializer(students, many=True)
        # return Response(serializer.data)
    except BaseException as e:
        print(e)

@api_view(["DELETE"])
def delStudent(request):
   try:
    print("delete")
    #  obj=Students.objects.get(id = request.GET["id"])
    #  obj.delete()
    #  return Response("Success", status=status.HTTP_201_CREATED)
   except BaseException as e:
     print(e)
     return Response("Not Deleted", status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')
