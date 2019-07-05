from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_view,name ='home'),
    path('contact/',contact),
    path('about/',about),
    path('delete_student/<id>',delete_student),
    path('edit_student/<id>',edit_student),
    path('admin/', admin.site.urls),
    path('createstudent/',createstudent),

]