from django.urls import include,path
from . import views


urlpatterns = [

    # path('',views.student,name='student'),
    # path('crud',views.crud,name='crud'),
    # path('javascript',views.javascript,name='javascript'),
    path('',views.Fun,name='baxter'),
    path('post',views.post_data,name='post')

]