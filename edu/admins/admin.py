from django.contrib import admin
from .models import Category,Subject,Topic,Subtopic,Syllabus
# Register your models here.


class Admin_Category(admin.ModelAdmin):
    list_display = ['id','name','date_created','date_updated','slug']
admin.site.register(Category,Admin_Category)    

class Admin_Subject(admin.ModelAdmin):
     list_display = ['id','name','date_created','date_updated','code']
   
admin.site.register(Subject,Admin_Subject)


class Admin_Topic(admin.ModelAdmin):
       list_display = ['id','name','date_created','date_updated']

admin.site.register(Topic,Admin_Topic)       


class Admin_Subtopic(admin.ModelAdmin):
       list_display = ['id','name','category','subject','topic','date_created','date_updated','slug']

admin.site.register(Subtopic,Admin_Subtopic)       


class Admin_Syllabus(admin.ModelAdmin):
       list_display = ['id','name','category','subject','syllabus_file','date_created','date_updated']

admin.site.register(Syllabus,Admin_Syllabus)       
