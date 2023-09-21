from django.urls import include,path
from .views import *


urlpatterns = [

    # path('',views.student,name='student'),
    # path('crud',views.crud,name='crud'),
    # path('javascript',views.javascript,name='javascript'),
    # path('',views.Fun,name='baxter'),
    # path('post',views.post_data,name='post')
    path('student', MyApiclass.as_view()),
    path('api_register',Generate_token.as_view()),

]