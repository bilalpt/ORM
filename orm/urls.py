from django.urls import include,path
from . import views


urlpatterns = [

    path('',views.student,name='student'),
    path('crud',views.crud,name='crud'),

]