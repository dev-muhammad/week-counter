from django.urls import path
from .views import home, CalcView, APICalcView

urlpatterns = [
    path('', home, name='home'),
    path('<str:date>', CalcView.as_view()),
    path('api/<str:date>', APICalcView.as_view())
]