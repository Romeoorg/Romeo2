from django.urls import path
from ye.views import myfunction2
from ye.views import myfunction1


urlpatterns = [

    path('',myfunction1,name='myfunction1'),
    path('myfunction2/<str:pk>/',myfunction2,name='myfunction2'),
]