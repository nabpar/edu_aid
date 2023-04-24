from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework import generics
from .serializer import Category_Serializer,Subject_Serializer,Topic_Serializer,Subtopic_Serializer,Syllabus_Serializer
from .models import Category,Subject,Topic,Subtopic,Syllabus


# Create your views here.

# For Category
class Create_Category_View(generics.CreateAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer

class List_Category_view(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class = Category_Serializer

class Update_Category_View(generics.UpdateAPIView):
    queryset = Category.objects.all()    
    serializer_class = Category_Serializer

class Delete_Category_View(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =Category_Serializer

# For Subject
class Create_Subject_View(generics.CreateAPIView):
    queryset= Subject.objects.all()
    serializer_class = Subject_Serializer

class List_Subject_view(generics.ListAPIView):
    queryset= Subject.objects.all()
    serializer_class = Subject_Serializer

class Update_Subject_View(generics.UpdateAPIView):
    queryset = Subject.objects.all()    
    serializer_class = Subject_Serializer

class Delete_Subject_View(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer


# For Topic

class Create_Topic_View(generics.CreateAPIView):
    queryset= Subject.objects.all()
    serializer_class = Syllabus_Serializer

class List_Topic_view(generics.ListAPIView):
    queryset= Topic.objects.all()
    serializer_class = Syllabus_Serializer

class Update_Topic_View(generics.UpdateAPIView):
    queryset = Topic.objects.all()    
    serializer_class = Syllabus_Serializer

class Delete_Topic_View(generics.DestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = Syllabus_Serializer

# For Sub_Topic

class Create_Subtopic_View(generics.CreateAPIView):
    queryset= Subtopic.objects.all()
    serializer_class = Subtopic_Serializer

class List_Subtopic_view(generics.ListAPIView):
    queryset= Subtopic.objects.all()
    serializer_class =Subtopic_Serializer

class Update_Subtopic_View(generics.UpdateAPIView):
    queryset = Subtopic.objects.all()    
    serializer_class = Subtopic_Serializer

class Delete_Subtopic_View(generics.DestroyAPIView):
    queryset = Subtopic.objects.all()
    serializer_class = Subtopic_Serializer


# For Syllabus


class Create_Syllabus_View(generics.CreateAPIView):
    queryset= Syllabus.objects.all()
    serializer_class = Subtopic_Serializer

class List_Syllabus_view(generics.ListAPIView):
    queryset= Syllabus.objects.all()
    serializer_class =Subtopic_Serializer

class Update_Syllabus_View(generics.UpdateAPIView):
    queryset = Syllabus.objects.all()    
    serializer_class = Subtopic_Serializer

class Delete_Syllabus_View(generics.DestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = Subtopic_Serializer