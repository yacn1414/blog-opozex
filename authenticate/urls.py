from django.urls import path
from authenticate import views
app_name = "auth"
urlpatterns = [
    path("1414/",views.login)
]
