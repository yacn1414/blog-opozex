from django.urls import path
from authenticate import views
app_name = "auth"
urlpatterns = [
    path("login/",views.login,name="login")
]
