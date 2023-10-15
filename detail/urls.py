from django.urls import path
from detail import views
app_name = "detail"
urlpatterns = [
    path('search/',views.search,name="search"),
    path('<slug:slug>/',views.detail_post,name="detail_post"),
    path('<slug:slug>/',views.category,name="category"),
]
