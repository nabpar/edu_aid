from .models import Category,Subject,Topic,Subtopic,Syllabus
from rest_framework import serializers

# Category Serialization

# class Create_Category_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'



class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



# subject Serialization

class Subject_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


#Topic Serialization

class Topic_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Topic
        fields = '__all__' 

# Subtopic serializer        

class Subtopic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = '__all__' 

# Syllabus Serializer
class Syllabus_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'        