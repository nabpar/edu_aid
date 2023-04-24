from django.urls import path
# from .views import Create_Category_View,List_Category_view,Update_Category_View,Delete_Category_View,List_Syllabus_view
from . import views

urlpatterns = [
    # For Category
    path('category_create/',views.Create_Category_View.as_view(),name="reate_Category"),
    path('category_view/',views.List_Category_view.as_view(),name="liist_category"),
    path('category_update/<int:pk>/',views.Update_Category_View.as_view(),name="Update_Category"),
    path('category_delete/<int:pk>/',views.Delete_Category_View.as_view(),name="Delete_Category"),

    # For Subject
    path('subject_create/',views.Create_Category_View.as_view(),name="Create_Subject"),
    path('subject_view/',views.List_Subject_view.as_view(),name="liist_cSubject"),
    path('subject_update/<int:pk>/',views.Update_Subject_View.as_view(),name="Update_Subject"),
    path('subject_delete/<int:pk>/',views.Delete_Subject_View.as_view(),name="Delete_Subject"),

    # For Topic
    path('topic_create/',views.Create_Topic_View.as_view(),name="cCreate_Topic"),
    path('topic_view/',views.List_Topic_view.as_view(),name="liist_Topic"),
    path('topic_update/<int:pk>/',views.Update_Topic_View.as_view(),name="Update_Topic"),
    path('topic_delete/<int:pk>/',views.Delete_Topic_View.as_view(),name="Delete_Topic"),


     # For Subtopic
    path('subtopic_create/',views.Create_Subtopic_View.as_view(),name="Create_Subtopic"),
    path('subtopic_view/',views.List_Subtopic_view.as_view(),name="liist_Subtopic"),
    path('subtopic_update/<int:pk>/',views.Update_Subtopic_View.as_view(),name="Update_Subtopic"),
    path('subtopic_delete/<int:pk>/',views.Delete_Subtopic_View.as_view(),name="Delete_Subtopic"),


 # For Syllabus
    path('syllabus_create/',views.Create_Syllabus_View.as_view(),name="Create_Syllabus"),
    path('syllabus_view/',views.List_Syllabus_view.as_view(),name="liist_Syllabus"),
    path('syllabus_update/<int:pk>/',views.Update_Syllabus_View.as_view(),name="Update_Syllabus"),
    path('syllabus_delete/<int:pk>/',views.Delete_Syllabus_View.as_view(),name="Delete_Syllabus"),
]
